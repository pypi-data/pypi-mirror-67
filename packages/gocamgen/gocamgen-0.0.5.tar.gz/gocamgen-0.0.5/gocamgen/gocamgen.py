from ontobio.rdfgen.assoc_rdfgen import CamRdfTransform, TurtleRdfWriter, genid, prefix_context
from ontobio.vocabulary.relations import OboRO, Evidence
from ontobio.vocabulary.upper import UpperLevel
# from ontobio.util.go_utils import GoAspector
# from ontobio.ontol_factory import OntologyFactory
from prefixcommons.curie_util import expand_uri, contract_uri
from rdflib.namespace import OWL, RDF
from rdflib import Literal
from rdflib.term import URIRef
from rdflib.namespace import Namespace
import rdflib
# import networkx
# import logging
# import argparse
import datetime
import os.path as path
import logging
from gocamgen.triple_pattern_finder import TriplePattern, TriplePatternFinder
from gocamgen.subgraphs import AnnotationSubgraph
from gocamgen.collapsed_assoc import CollapsedAssociationSet, CollapsedAssociation
from gocamgen.utils import sort_terms_by_ontology_specificity, ShexHelper, ShexException


# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel("INFO")

ro = OboRO()
evt = Evidence()
upt = UpperLevel()
LEGO = Namespace("http://geneontology.org/lego/")
LAYOUT = Namespace("http://geneontology.org/lego/hint/layout/")
PAV = Namespace('http://purl.org/pav/')
DC = Namespace("http://purl.org/dc/elements/1.1/")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
GOREL = Namespace("http://purl.obolibrary.org/obo/GOREL_")

# Stealing a lot of code for this from ontobio.rdfgen:
# https://github.com/biolink/ontobio


def expand_uri_wrapper(id):
    c = prefix_context
    c['GOREL'] = "http://purl.obolibrary.org/obo/GOREL_"
    uri = expand_uri(id, cmaps=[c])
    return uri

def contract_uri_wrapper(id):
    uri = contract_uri(id, cmaps=[prefix_context])
    return uri

HAS_SUPPORTING_REFERENCE = URIRef(expand_uri_wrapper("dc:source"))
ENABLED_BY = URIRef(expand_uri_wrapper(ro.enabled_by))
ENABLES = URIRef(expand_uri_wrapper(ro.enables))
INVOLVED_IN = URIRef(expand_uri_wrapper(ro.involved_in))
PART_OF = URIRef(expand_uri_wrapper(ro.part_of))
OCCURS_IN = URIRef(expand_uri_wrapper(ro.occurs_in))
COLOCALIZES_WITH = URIRef(expand_uri_wrapper(ro.colocalizes_with))
CONTRIBUTES_TO = URIRef(expand_uri_wrapper("RO:0002326"))
MOLECULAR_FUNCTION = URIRef(expand_uri_wrapper(upt.molecular_function))
REGULATES = URIRef(expand_uri_wrapper("RO:0002211"))
LOCATED_IN = URIRef(expand_uri_wrapper("RO:0001025"))

# RO_ONTOLOGY = OntologyFactory().create("http://purl.obolibrary.org/obo/ro.owl")  # Need propertyChainAxioms to parse (https://github.com/biolink/ontobio/issues/312)
INPUT_RELATIONS = {
    #TODO Create rule for deciding (MOD-specific?) whether to convert has_direct_input to has input
    # "has_direct_input": "RO:0002400",
    "has_direct_input": "RO:0002233",
    "has input": "RO:0002233",
    "has_input": "RO:0002233",
    "occurs_in": "BFO:0000066"
}
ACTS_UPSTREAM_OF_RELATIONS = {
    "acts_upstream_of": "RO:0002263",
    "acts_upstream_of_or_within": "RO:0002264",
    "acts upstream of or within, positive effect": "RO:0004032",
    "acts upstream of or within, negative effect": "RO:0004033",
    "acts_upstream_of_positive_effect": "RO:0004034",
    "acts_upstream_of_negative_effect": "RO:0004035",
}
HAS_REGULATION_TARGET_RELATIONS = {
    # WB:WBGene00013591 involved_in GO:0042594
    "has_regulation_target": ""
}


SHEX_HELPER = ShexHelper()


def has_regulation_target_bucket(ontology, term):
    ancestors = ontology.ancestors(term, reflexive=True)
    buckets = []
    if "GO:0065009" in ancestors:
        buckets.append("a")
    if "GO:0010468" in ancestors:
        buckets.append("b")
    if "GO:0002092" in ancestors or "GO:0042176" in ancestors:
        buckets.append("c")
    if "GO:0019538" in ancestors or "GO:0032880" in ancestors:
        buckets.append("d")
    return buckets


now = datetime.datetime.now()


class Annoton():
    def __init__(self, subject_id, assocs, connections=None):
        self.enabled_by = subject_id
        self.annotations = assocs
        self.connections = connections
        self.individuals = {}


class GoCamEvidence:
    DEFAULT_CONTRIBUTOR = "http://orcid.org/0000-0002-6659-0416"

    def __init__(self, code, references, contributors=[], date="", comment="", with_from=None):
        self.evidence_code = code
        self.references = references
        self.date = date
        self.contributors = contributors
        self.comment = comment
        self.with_from = with_from
        self.id = None

    @staticmethod
    def create_from_annotation(annot):
        evidence_code = annot["evidence"]["type"]
        references = annot["evidence"]["has_supporting_reference"]
        annot_date = "{0:%Y-%m-%d}".format(datetime.datetime.strptime(annot["date"], "%Y%m%d"))
        source_line = annot["source_line"].rstrip().replace("\t", " ")
        # contributors = handle_annot_properties() # Need annot_properties to be parsed w/ GpadParser first
        contributors = []
        if "annotation_properties" in annot and "contributor" in annot["annotation_properties"]:
            contributors = annot["annotation_properties"]["contributor"]
        if len(contributors) == 0:
            contributors = [GoCamEvidence.DEFAULT_CONTRIBUTOR]

        return GoCamEvidence(evidence_code, references,
                           contributors=contributors,
                           date=annot_date,
                           comment=source_line)

    @staticmethod
    def create_from_collapsed_association(collapsed_association: CollapsedAssociation):
        evidences = []
        for line in collapsed_association:
            evidence = GoCamEvidence.create_from_annotation(line.as_dict())
            if line.with_from:
                evidence.with_from = ",".join(line.with_from)
            evidences.append(evidence)
        return evidences


class GoCamModel():
    # TODO: Not using anymore maybe get rid of?
    relations_dict = {
        "has_direct_input": "RO:0002400",
        "has input": "RO:0002233",
        "has_regulation_target": "RO:0002211",  # regulates
        "regulates_activity_of": "RO:0002578",  # directly regulates
        "with_support_from": "RO:0002233",  # has input
        "directly_regulates": "RO:0002578",
        "directly_positively_regulates": "RO:0002629",
        "directly_negatively_regulates": "RO:0002630",
        "colocalizes_with": "RO:0002325",
        "contributes_to": "RO:0002326",
        "part_of": "BFO:0000050",
        "acts_upstream_of": "RO:0002263",
        "acts_upstream_of_negative_effect": "RO:0004035",
        "acts_upstream_of_or_within": "RO:0002264",
        "acts_upstream_of_positive_effect": "RO:0004034",
        "acts upstream of, negative effect": "RO:0004035",
        "acts_upstream_of_or_within_negative_effect": "RO:0004033",
        "acts_upstream_of_or_within_positive_effect": "RO:0004032",
        "located_in": "RO:0001025",
    }

    def __init__(self, modeltitle, connection_relations=None):
        cam_writer = CamTurtleRdfWriter(modeltitle)
        self.writer = AnnotonCamRdfTransform(cam_writer)
        self.modeltitle = modeltitle
        self.classes = []
        self.individuals = {}   # Maintain entity-to-IRI dictionary. Prevents dup individuals but we may want dups?
        # TODO: Refactor to make graph more prominent
        self.graph = self.writer.writer.graph
        if connection_relations is None:
            self.connection_relations = GoCamModel.relations_dict
        else:
            self.connection_relations = connection_relations
        self.declare_properties()

    def write(self, filename):
        if path.splitext(filename)[1] != ".ttl":
            filename += ".ttl"
        with open(filename, 'wb') as f:
            self.writer.writer.serialize(destination=f)

    def declare_properties(self):
        # AnnotionProperty
        self.writer.emit_type(URIRef("http://geneontology.org/lego/evidence"), OWL.AnnotationProperty)
        self.writer.emit_type(URIRef("http://geneontology.org/lego/hint/layout/x"), OWL.AnnotationProperty)
        self.writer.emit_type(URIRef("http://geneontology.org/lego/hint/layout/y"), OWL.AnnotationProperty)
        self.writer.emit_type(URIRef("http://purl.org/pav/providedBy"), OWL.AnnotationProperty)
        self.writer.emit_type(URIRef("http://purl.org/dc/elements/1.1/contributor"), OWL.AnnotationProperty)
        self.writer.emit_type(URIRef("http://purl.org/dc/elements/1.1/date"), OWL.AnnotationProperty)
        self.writer.emit_type(URIRef("http://purl.org/dc/elements/1.1/source"), OWL.AnnotationProperty)

    def declare_class(self, class_id):
        if class_id not in self.classes:
            self.writer.emit_type(URIRef(expand_uri_wrapper(class_id)), OWL.Class)
            self.classes.append(class_id)

    def declare_individual(self, entity_id):
        entity = genid(base=self.writer.writer.base + '/')
        # TODO: Make this add_to_graph
        self.writer.emit_type(entity, self.writer.uri(entity_id))
        self.writer.emit_type(entity, OWL.NamedIndividual)
        self.individuals[entity_id] = entity
        return entity

    def add_axiom(self, statement, evidence=None):
        (source_id, property_id, target_id) = statement
        stmt_id = self.find_bnode(statement)
        if stmt_id is None:
            stmt_id = self.writer.blanknode()
            self.writer.emit_type(stmt_id, OWL.Axiom)
        self.writer.emit(stmt_id, OWL.annotatedSource, source_id)
        self.writer.emit(stmt_id, OWL.annotatedProperty, property_id)
        self.writer.emit(stmt_id, OWL.annotatedTarget, target_id)

        if evidence:
            self.add_evidence(stmt_id, evidence)

        return stmt_id

    def create_axiom(self, subject_id, relation_uri, object_id):
        subject_uri = subject_id if subject_id.__class__.__name__ == "URIRef" else self.declare_individual(subject_id)
        object_uri = object_id if object_id.__class__.__name__ == "URIRef" else self.declare_individual(object_id)
        axiom_id = self.add_axiom(self.writer.emit(subject_uri, relation_uri, object_uri))
        return axiom_id

    # TODO: Explicitly type subject, object parameters. Are they Class ID URIs or instance URIs?
    # def find_or_create_axiom_by_class_id_uri
    # def find_or_create_axiom_by_instance_uri
    def find_or_create_axiom(self, subject_id : str, relation_uri : URIRef, object_id : str, annoton=None,
                             exact_length=False):
        # Maybe overkill but gonna try using find_pattern_recursive to find only one triple
        # TODO: Replace the TriplePattern stuff w/ SPARQL but need 'exact_length' to work
        pattern = TriplePattern([(subject_id, relation_uri, object_id)])
        found_triples = TriplePatternFinder().find_pattern_recursive(self, pattern, exact_length=True)
        # found_triples = self.triples_by_ids(subject_id, relation_uri, object_id)
        if len(found_triples) > 0:
            # Gonna be a list of "triple-chains", itself a list of triples, and each triple is sort like a 3-index list.
            # So we just want the first triple from the first chain:
            found_triple = found_triples[0][0]
            subject_uri = found_triple[0]
            object_uri = found_triple[2]
            axiom_id = self.find_bnode(found_triple)
        else:
            # subject_uri = self.declare_individual(subject_id)
            subject_uri = subject_id if subject_id.__class__.__name__ == "URIRef" else self.declare_individual(subject_id)
            object_uri = object_id if object_id.__class__.__name__ == "URIRef" else self.declare_individual(object_id)
            # TODO Can emit() be changed to emit_axiom()?
            axiom_id = self.add_axiom(self.writer.emit(subject_uri, relation_uri, object_uri))
        if annoton and relation_uri == ENABLED_BY:
            annoton.individuals[subject_id] = subject_uri
            annoton.individuals[object_id] = object_uri
        return axiom_id

    def add_evidence(self, axiom, evidence: GoCamEvidence):
        # Try finding existing evidence object containing same type and references
        # ev_id = self.writer.find_or_create_evidence_id(ev)
        ev_id = self.writer.create_evidence(evidence)
        self.writer.emit(axiom, URIRef("http://geneontology.org/lego/evidence"), ev_id)
        ### Emit ev fields to axiom here TODO: Couple evidence and axiom emitting together
        self.writer.emit(axiom, DC.date, Literal(evidence.date))
        self.writer.emit(axiom, RDFS.comment, Literal(evidence.comment))
        for c in evidence.contributors:
            self.writer.emit(axiom, DC.contributor, Literal(c))

    def add_connection(self, gene_connection, source_annoton):
        # Switching from reusing existing activity node from annoton to creating new one for each connection - Maybe SPARQL first to check if annoton activity already used for connection?
        # Check annoton for existing activity.
        # if gene_connection.object_id in source_annoton.individuals:
        #     # If exists and activity has connection relation,
        #     # Look for two triples: (gene_connection.object_id, ENABLED_BY, source_annoton.enabled_by) and (gene_connection.object_id, connection_relations, anything)
        # Annot MF should be declared by now - don't declare object_id if object_id == annot MF?
        if gene_connection.gp_b not in self.individuals:
            return
        source_id = None
        uri_list = self.uri_list_for_individual(gene_connection.object_id)
        for u in uri_list:
            if gene_connection.relation in self.connection_relations:
                rel = URIRef(expand_uri_wrapper(self.connection_relations[gene_connection.relation]))
                # Annot MF should be declared by now - don't declare object_id if object_id == annot MF?
                try:
                    annot_mf = source_annoton.molecular_function["object"]["id"]
                except:
                    annot_mf = ""
                if self.writer.writer.graph.__contains__((u,rel,None)) and gene_connection.object_id != annot_mf:
                    source_id = self.declare_individual(gene_connection.object_id)
                    source_annoton.individuals[gene_connection.object_id] = source_id
                    break

        if source_id is None:
            try:
                source_id = source_annoton.individuals[gene_connection.object_id]
            except KeyError:
                source_id = self.declare_individual(gene_connection.object_id)
                source_annoton.individuals[gene_connection.object_id] = source_id
        # Add enabled by stmt for object_id - this is essentially adding another annoton connecting gene-to-extension/with-MF to the model
        self.writer.emit(source_id, ENABLED_BY, source_annoton.individuals[source_annoton.enabled_by])
        self.writer.emit_axiom(source_id, ENABLED_BY, source_annoton.individuals[source_annoton.enabled_by])
        property_id = URIRef(expand_uri_wrapper(self.connection_relations[gene_connection.relation]))
        target_id = self.individuals[gene_connection.gp_b]
        # Annotate source MF GO term NamedIndividual with relation code-target MF term URI
        self.writer.emit(source_id, property_id, target_id)
        # Add axiom (Source=MF term URI, Property=relation code, Target=MF term URI)
        self.writer.emit_axiom(source_id, property_id, target_id)

    def uri_list_for_individual(self, individual):
        uri_list = []
        graph = self.writer.writer.graph
        for t in graph.triples((None,None,self.writer.uri(individual))):
            uri_list.append(t[0])
        return uri_list

    def triples_by_ids(self, subject, relation_uri, object_id):
        graph = self.writer.writer.graph

        triples = []
        if subject.__class__.__name__ == "URIRef" or subject is None:
            subjects = [subject]
        else:
            subjects = self.uri_list_for_individual(subject)
        if object_id.__class__.__name__ == "URIRef" or object_id is None:
            objects = [object_id]
        else:
            objects = self.uri_list_for_individual(object_id)
        for object_uri in objects:
            for subject_uri in subjects:
                # if (subject_uri, relation_uri, object_uri) in graph:
                #     triples.append((subject_uri, relation_uri, object_uri))
                for t in graph.triples((subject_uri, relation_uri, object_uri)):
                    triples.append(t)
        return triples

    def individual_label_for_uri(self, uri):
        ind_list = []
        graph = self.writer.writer.graph
        for t in graph.triples((uri, RDF.type, None)):
            if t[2] != OWL.NamedIndividual: # We know OWL.NamedIndividual triple does't contain the label so don't return it
                ind_list.append(t[2])
        return ind_list

    def class_for_uri(self, uri):
        try:
            class_curie = contract_uri_wrapper(self.individual_label_for_uri(uri)[0])[0]
            return class_curie
        except:
            return None

    def axioms_for_source(self, source, property_uri=None):
        if property_uri is None:
            property_uri = OWL.annotatedSource
        axiom_list = []
        graph = self.writer.writer.graph
        for uri in self.uri_list_for_individual(source):
            for t in graph.triples((None, property_uri, uri)):
                axiom_list.append(t[0])
        return axiom_list

    def find_bnode(self, triple):
        (subject,predicate,object_id) = triple
        s_triples = self.writer.writer.graph.triples((None, OWL.annotatedSource, subject))
        s_bnodes = [s for s,p,o in s_triples]
        p_triples = self.writer.writer.graph.triples((None, OWL.annotatedProperty, predicate))
        p_bnodes = [s for s,p,o in p_triples]
        o_triples = self.writer.writer.graph.triples((None, OWL.annotatedTarget, object_id))
        o_bnodes = [s for s,p,o in o_triples]
        bnodes = set(s_bnodes) & set(p_bnodes) & set(o_bnodes)
        if len(bnodes) > 0:
            return list(bnodes)[0]

    def triples_involving_individual(self, ind_id, relation=None):
        # "involving" meaning individual (URI) is either subject or object
        graph = self.writer.writer.graph
        found_triples = list(graph.triples((ind_id, relation, None)))
        for t in graph.triples((None, relation, ind_id)):
            if t not in found_triples:
                found_triples.append(t)
        return found_triples


class AssocGoCamModel(GoCamModel):
    ENABLES_O_RELATION_LOOKUP = {}

    def __init__(self, modeltitle, assocs, connection_relations=None):
        GoCamModel.__init__(self, modeltitle, connection_relations)
        self.associations = CollapsedAssociationSet(assocs)
        self.ontology = None
        self.ro_ontology = None
        self.gorel_ontology = None
        self.extensions_mapper = None
        self.default_contributor = "http://orcid.org/0000-0002-6659-0416"
        self.graph.bind("GOREL", GOREL)  # Because GOREL isn't in context.jsonld's

    def translate(self):

        self.associations.go_ontology = self.ontology
        self.associations.collapse_annotations()

        for a in self.associations:

            term = a.object_id()

            # Add evidences tied to axiom_ids
            evidences = GoCamEvidence.create_from_collapsed_association(a)

            annotation_extensions = a.annot_extensions()

            # Translate extension - maybe add function argument for custom translations?
            if not annotation_extensions:
                annot_subgraph = self.translate_primary_annotation(a)
                # For annots w/o extensions, this is where we write subgraph to model
                annot_subgraph.write_to_model(self, evidences)
            else:
                aspect = self.extensions_mapper.go_aspector.go_aspect(term)

                # TODO: Handle deduping in collapsed_assoc - need access to extensions_mapper.dedupe_extensions
                annotation_extensions = self.extensions_mapper.dedupe_extensions(annotation_extensions)

                # Split on those multiple occurs_in(same NS) extensions
                # TODO: Cleanup/refactor this splitting into separate method
                extension_sets_to_remove = []
                for uo in annotation_extensions:
                    # Grab occurs_in's
                    # Make a new uo if situation found
                    occurs_in_exts = [ext for ext in uo['intersection_of'] if ext["property"] == "occurs_in"]
                    # onto_grouping = {
                    #     "CL": [{}, {}],
                    #     "EMAPA": [{}]
                    # }
                    onto_grouping = {}
                    for ext in occurs_in_exts:
                        ont_prefix = ext["filler"].split(":")[0]
                        if ont_prefix not in onto_grouping:
                            onto_grouping[ont_prefix] = []
                        onto_grouping[ont_prefix].append(ext)
                    for ont_prefix, exts in onto_grouping.items():
                        if len(exts) > 1:
                            if uo not in extension_sets_to_remove:
                                extension_sets_to_remove.append(uo)  # Remove original set when we're done splitting
                            for ext in exts:
                                # Create new 'intersection_of' list
                                new_exts_list = []
                                # Add ext to this new list if its prefix is not ont_prefix
                                for int_of_ext in uo['intersection_of']:
                                    if int_of_ext["property"] != "occurs_in" or int_of_ext["filler"].split(":")[0] != ont_prefix:
                                        # Add the extensions that don't currently concern us
                                        new_exts_list.append(int_of_ext)
                                # Then add occurs_in ext in current iteration
                                new_exts_list.append(ext)
                                annotation_extensions.append({"intersection_of": new_exts_list})
                # Remove original, un-split extension from list so it isn't translated
                [annotation_extensions.remove(ext_set) for ext_set in extension_sets_to_remove]

                for uo in annotation_extensions:
                    int_bits = []
                    for rel in uo["intersection_of"]:
                        int_bits.append("{}({})".format(rel["property"], rel["filler"]))
                    ext_str = ",".join(int_bits)

                    annot_subgraph = self.translate_primary_annotation(a)

                    intersection_extensions = self.extensions_mapper.dedupe_extensions(uo['intersection_of'])
                    is_cool = self.extensions_mapper.annot_following_rules(intersection_extensions, aspect, term)
                    # is_cool = True  # Open the flood gates
                    if is_cool:
                        logger.debug("GOOD: {}".format(ext_str))
                        # Nesting repeated extension relations (i.e. occurs_in, part_of)
                        ext_rels_to_nest = ['occurs_in', 'part_of']  # Switch to turn on/off extension nesting
                        for ertn in ext_rels_to_nest:
                            nest_exts = [ext for ext in intersection_extensions if ext["property"] == ertn]
                            if len(nest_exts) > 1:
                                # Sort by specific term to general term
                                sorted_nest_ext_terms = sort_terms_by_ontology_specificity(
                                    [ne["filler"] for ne in nest_exts])
                                # Translate
                                loc_subj_n = annot_subgraph.get_anchor()
                                loc_subj_term = AnnotationSubgraph.node_class(loc_subj_n)
                                for idx, ne_term in enumerate(sorted_nest_ext_terms):
                                    # location_relation could be part_of, occurs_in, or located_in
                                    # Figure out what types of classes these are
                                    # Use case here is matching to ShEx shape class
                                    subj_shape = SHEX_HELPER.shape_from_class(loc_subj_term,
                                                                              self.extensions_mapper.go_aspector)
                                    loc_obj_n = annot_subgraph.add_instance_of_class(ne_term)
                                    obj_shape = SHEX_HELPER.shape_from_class(ne_term,
                                                                             self.extensions_mapper.go_aspector)
                                    # location_relation = "BFO:0000050"  # part_of
                                    try:
                                        location_relation = SHEX_HELPER.relation_lookup(subj_shape, obj_shape)
                                    except ShexException as ex:
                                        raise ShexException(ex.message + f" for {loc_subj_term} to {ne_term}")
                                    if idx == 0 and ertn == "occurs_in":
                                        location_relation = "BFO:0000066"  # occurs_in - because MF -> @<AnatomicalEntity> OR @<CellularComponent>
                                    annot_subgraph.add_edge(loc_subj_n, location_relation, loc_obj_n)

                                    loc_subj_term = ne_term  # For next iteration
                                    loc_subj_n = loc_obj_n  # For next iteration
                                # Remove from intersection_extensions because this is now already translated
                                [intersection_extensions.remove(ext) for ext in nest_exts]
                        for rel in intersection_extensions:
                            ext_relation = rel["property"]
                            ext_target = rel["filler"]
                            if ext_relation not in list(INPUT_RELATIONS.keys()) + list(HAS_REGULATION_TARGET_RELATIONS.keys()):
                                # No RO term yet. Try looking up in RO
                                relation_term = self.translate_relation_to_ro(ext_relation)
                                if relation_term:
                                    # print("Ext relation {} auto-mapped to {} in {}".format(ext_relation, relation_term, a.subject_id()))
                                    INPUT_RELATIONS[ext_relation] = relation_term
                            if ext_relation in INPUT_RELATIONS:
                                ext_target_n = annot_subgraph.add_instance_of_class(ext_target)
                                # Need to find what mf we're talking about
                                anchor_n = annot_subgraph.get_anchor()
                                annot_subgraph.add_edge(anchor_n, INPUT_RELATIONS[ext_relation], ext_target_n)
                            elif ext_relation in HAS_REGULATION_TARGET_RELATIONS:
                                buckets = has_regulation_target_bucket(self.ontology, term)
                                if len(buckets) > 0:
                                    bucket = buckets[0]  # Or express all buckets?
                                    # Four buckets
                                    if bucket in ["a", "d"]:
                                        regulates_rel, regulated_mf = self.get_rel_and_term_in_logical_definitions(term)
                                        if regulates_rel and regulated_mf:
                                            # [GP-A]<-enabled_by-[root MF]-regulates->[molecular function Z]-enabled_by->[GP-B]
                                            ext_target_n = annot_subgraph.add_instance_of_class(ext_target)
                                            regulated_mf_n = annot_subgraph.add_instance_of_class(regulated_mf)
                                            annot_subgraph.add_edge(regulated_mf_n, ro.enabled_by, ext_target_n)
                                            anchor_n = annot_subgraph.get_anchor()
                                            annot_subgraph.add_edge(anchor_n, regulates_rel, regulated_mf_n)
                                            # TODO: Suppress/delete (GP-A)<-enabled_by-(root MF)-part_of->(term) aka involved_in_translated
                                            # Remove (anchor_uri, None, term)
                                            # Is this anchor_uri always going to the root_mf?
                                            # Will the term individual be used for anything else?
                                            #   Other comma-delimited extensions on same annotation?
                                            # has_during? occurs_in?
                                            # WB:WBGene00001173 GO:0051343 ['has_regulation_target', 'occurs_in'] ['a']
                                            # WB:WBGene00006652 GO:0045944 ['has_regulation_target', 'occurs_in'] ['b']
                                            # WB:WBGene00003639 GO:0036003 ['happens_during', 'has_regulation_target'] ['b']
                                            # Other comma-delimited extensions (e.g. happens_during, has_input) need this triple?
                                            # WB:WBGene00002335 GO:1902685 ['has_regulation_target', 'occurs_in'] ['d']
                                        else:
                                            logger.warning("Couldn't get regulates relation and/or regulated term from LD of: {}".format(term))
                                    elif bucket in ["b", "c"]:
                                        regulates_rel, regulated_term = self.get_rel_and_term_in_logical_definitions(term)
                                        if regulates_rel:
                                            # find 'Y subPropertyOf regulates_rel' in RO where Y will be `causally
                                            # upstream of` relation
                                            # Ex. GO:0045944 -> RO:0002213 -> RO:0002304
                                            # edges(RO:0002213) only returns subProperties. Need superProperties
                                            # Gettin super properties
                                            causally_upstream_relation = self.get_causally_upstream_relation(regulates_rel)
                                            # GP-A<-enabled_by-[root MF]-part_of->[regulation of Z]-has_input->GP-B,-causally upstream of (positive/negative effect)->[root MF]-enabled_by->GP-B
                                            ext_target_n = annot_subgraph.add_instance_of_class(ext_target)
                                            anchor_n = annot_subgraph.get_anchor()  # TODO: Gotta find MF. MF no longer anchor if primary term is BP
                                            annot_subgraph.add_edge(anchor_n, INPUT_RELATIONS["has input"], ext_target_n)
                                            root_mf_b_n = annot_subgraph.add_instance_of_class(upt.molecular_function)
                                            annot_subgraph.add_edge(anchor_n, causally_upstream_relation, root_mf_b_n)
                                            annot_subgraph.add_edge(root_mf_b_n, ro.enabled_by, ext_target_n)
                                            # WB:WBGene00001574 GO:1903363 ['happens_during', 'has_regulation_target'] ['c', 'd']
                                        else:
                                            logger.warning("Couldn't get regulates relation from LD of: {}".format(term))
                            # else:
                            #     # No RO term yet. Try looking up in RO
                            #     relation_term = self.translate_relation_to_ro(ext_relation)
                            #     INPUT_RELATIONS[ext_relation] = relation_term

                    else:
                        logger.debug("BAD: {}".format(ext_str))
                    # For annots w/ extensions, this is where we write subgraph to model
                    annot_subgraph.write_to_model(self, evidences)
        self.extensions_mapper.go_aspector.write_cache()

    def translate_primary_annotation(self, annotation: CollapsedAssociation):
        gp_id = annotation.subject_id()
        term = annotation.object_id()
        annot_subgraph = AnnotationSubgraph(annotation)

        for q in annotation.qualifiers():
            if q == "enables":
                
                # activity = Activity(term_n, "fake_label")
                # gene_product = GeneProduct(gp_id)
                # aa = ActivityAssociation(activity, gene_product)
                # aa.set_evidence()
                # activity.set_activity_association(aa)

                term_n = annot_subgraph.add_instance_of_class(term, is_anchor=True)
                enabled_by_n = annot_subgraph.add_instance_of_class(gp_id)
                annot_subgraph.add_edge(term_n, "RO:0002333", enabled_by_n)
            elif q == "involved_in":
                # mf_n = annot_subgraph.add_instance_of_class(upt.molecular_function, is_anchor=True)
                mf_n = annot_subgraph.add_instance_of_class(upt.molecular_function)
                enabled_by_n = annot_subgraph.add_instance_of_class(gp_id)
                # term_n = annot_subgraph.add_instance_of_class(term)
                term_n = annot_subgraph.add_instance_of_class(term, is_anchor=True)
                annot_subgraph.add_edge(mf_n, "RO:0002333", enabled_by_n)
                annot_subgraph.add_edge(mf_n, "BFO:0000050", term_n)
            elif q in ACTS_UPSTREAM_OF_RELATIONS:
                # Look for existing GP <- enabled_by [root MF] -> causally_upstream_of BP
                causally_relation = self.get_causally_upstream_relation(ACTS_UPSTREAM_OF_RELATIONS[q])
                # mf_n = annot_subgraph.add_instance_of_class(upt.molecular_function, is_anchor=True)
                mf_n = annot_subgraph.add_instance_of_class(upt.molecular_function)
                enabled_by_n = annot_subgraph.add_instance_of_class(gp_id)
                # term_n = annot_subgraph.add_instance_of_class(term)
                term_n = annot_subgraph.add_instance_of_class(term, is_anchor=True)
                annot_subgraph.add_edge(mf_n, "RO:0002333", enabled_by_n)
                annot_subgraph.add_edge(mf_n, causally_relation, term_n)
            elif q == "NOT":
                # Try it in UI and look at OWL
                pass
            else:
                # TODO: should check that existing axiom/triple isn't connected to anything else; length matches exactly
                enabled_by_n = annot_subgraph.add_instance_of_class(gp_id)
                term_n = annot_subgraph.add_instance_of_class(term, is_anchor=True)
                # annot_subgraph.add_edge(enabled_by_n, self.relations_dict[q], term_n)
                if q == "part_of" and SHEX_HELPER.shape_from_class(term, self.extensions_mapper.go_aspector) == "CellularComponent":
                    # Using shex_shape function should exclude AnatomicalEntity from getting located_in
                    q = "located_in"
                if q not in self.relations_dict:
                    relation = self.translate_relation_to_ro(q)
                else:
                    relation = self.relations_dict[q]
                annot_subgraph.add_edge(enabled_by_n, relation, term_n)

        with_froms = annotation.with_from()
        if with_froms:
            for wf in with_froms:
                wf_n = annot_subgraph.add_instance_of_class(wf)
                annot_subgraph.add_edge(annot_subgraph.get_anchor(), "RO:0002233", wf_n)

        return annot_subgraph

    def translate_relation_to_ro(self, relation_label):
        # Also check in GO_REL and use xref to RO
        for n in self.ro_ontology.nodes():
            node_label = self.ro_ontology.label(n)
            if node_label == relation_label.replace("_", " "):
                return n
        for n in self.gorel_ontology.nodes():
            node_label = self.gorel_ontology.label(n)
            if node_label == relation_label:
                gorel_node = self.gorel_ontology.node(n)
                # What we want will likely be in xref:
                xrefs = gorel_node['meta'].get('xrefs')
                if xrefs and len(xrefs) > 0:
                    for xref in xrefs:
                        val = xref['val']
                        if val.startswith('RO') or val.startswith('BFO'):
                            # print("{} xref'd to {}".format(n, val))
                            return val
                    fallback_rel = xrefs[0]['val']  # default to the the first xref - usually GOREL
                    self.writer.emit_type(URIRef(expand_uri_wrapper(fallback_rel)), OWL.ObjectProperty)
                    self.writer.emit(URIRef(expand_uri_wrapper(fallback_rel)), RDFS.label, Literal(relation_label))
                    return fallback_rel
                # print(gorel_node)  # No such luck so far getting matches

    def get_restrictions(self, term):
        lds = self.ontology.logical_definitions(term)
        restrictions = []
        for ld in lds:
            for r in ld.restrictions:
                if r[0] in self.ro_ontology.descendants("RO:0002211", reflexive=True):
                    restrictions.append(r)
        return restrictions

    def get_rel_and_term_in_logical_definitions(self, term):
        term_restrictions = self.get_restrictions(term)
        if len(term_restrictions) > 0:
            first_restriction = term_restrictions[0]
            regulates_rel = first_restriction[0]
            regulated_term = first_restriction[1]
            return regulates_rel, regulated_term
        else:
            return None, None

    def get_causally_upstream_relation(self, relation):
        regulates = "RO:0002211"
        causally_upstream_relations = []
        if relation == regulates or regulates in self.ro_ontology.ancestors(relation):
            for p in self.ro_ontology.parents(relation,
                                              relations=['subPropertyOf']):
                # For GO:0045944 this is grabbing both RO:0002304 and RO:0002211
                # Need specifically RO:0002304; how to specify?
                #   regulates_rel will only ever be regulates, positively regulates, or
                #   negatively regulates. If regulates in parents, grab other term
                if not p == regulates:
                    causally_upstream_relations.append(p)
        # input relations could have some unique logical difference (e.g. positively_regulates vs acts_upstream_of)
        else:
            if relation in self.ENABLES_O_RELATION_LOOKUP:
                return self.ENABLES_O_RELATION_LOOKUP[relation]
            else:
                causally_upstream_relation = self.ro_ontology.get_property_chain_axioms(relation)[0].chain_predicate_ids[1]  # always 2nd idx?
                self.ENABLES_O_RELATION_LOOKUP[relation] = causally_upstream_relation
                return causally_upstream_relation
        if len(causally_upstream_relations) > 0:
            return causally_upstream_relations[0]
        else:
            return None


class ReferencePreference:
    def __init__(self):
        # List order in python should be persistent
        self.order_of_prefix_preference = [
            "PMID",
            "GO_REF",
            "DOI"
        ]

    def pick(self, references):
        for pfx in self.order_of_prefix_preference:
            for ref in references:
                if ref.upper().startswith(pfx.upper()):
                    return ref


class CamTurtleRdfWriter(TurtleRdfWriter):
    def __init__(self, modeltitle):
        self.base = genid(base="http://model.geneontology.org")
        self.graph = rdflib.Graph(identifier=self.base)
        self.graph.bind("owl", OWL)
        self.graph.bind("obo", "http://purl.obolibrary.org/obo/")
        self.graph.bind("dc", DC)
        self.graph.bind("rdfs", RDFS)

        self.graph.add((self.base, RDF.type, OWL.Ontology))

        # Model attributes TODO: Should move outside init
        self.graph.add((self.base, URIRef("http://purl.org/pav/providedBy"), Literal("http://geneontology.org")))
        self.graph.add((self.base, DC.date, Literal(str(now.year) + "-" + str(now.month) + "-" + str(now.day))))
        self.graph.add((self.base, DC.title, Literal(modeltitle)))
        self.graph.add((self.base, DC.contributor, Literal("http://orcid.org/0000-0002-6659-0416"))) #TODO
        self.graph.add((self.base, URIRef("http://geneontology.org/lego/modelstate"), Literal("development")))
        self.graph.add((self.base, OWL.versionIRI, self.base))
        self.graph.add((self.base, OWL.imports, URIRef("http://purl.obolibrary.org/obo/go/extensions/go-lego.owl")))


class AnnotonCamRdfTransform(CamRdfTransform):
    def __init__(self, writer=None):
        CamRdfTransform.__init__(self, writer)
        self.annotons = []
        self.classes = []
        self.evidences = []
        self.ev_ids = []
        self.bp_id = None

    # TODO Remove "find" feature
    def find_or_create_evidence_id(self, evidence):
        for existing_evidence in self.evidences:
            if evidence.evidence_code == existing_evidence.evidence_code and set(evidence.references) == set(existing_evidence.references):
                if existing_evidence.id is None:
                    existing_evidence.id = genid(base=self.writer.base + '/')
                    self.ev_ids.append(existing_evidence.id)
                return existing_evidence.id
        return self.create_evidence(evidence)

    def create_evidence(self, evidence):
        # Use/figure out standard for creating URIs
        # Find minerva code to generate URI, add to Noctua doc
        ev_id = genid(base=self.writer.base + '/')
        evidence.id = ev_id
        # ev_cls = self.eco_class(self.uri(evidence.evidence_code))
        # ev_cls = self.eco_class(evidence.evidence_code) # This is already ECO:##### due to a GPAD being used
        ev_cls = self.uri(evidence.evidence_code)
        self.emit_type(ev_id, OWL.NamedIndividual)
        self.emit_type(ev_id, ev_cls)
        self.emit(ev_id, DC.date, Literal(evidence.date))
        if evidence.with_from:
            self.emit(ev_id, URIRef("http://geneontology.org/lego/evidence-with"), Literal(evidence.with_from))
        for c in evidence.contributors:
            self.emit(ev_id, DC.contributor, Literal(c))
        ref_to_emit = ReferencePreference().pick(evidence.references)
        o = Literal(ref_to_emit)  # Needs to go into Noctua like 'PMID:####' rather than full URL
        self.emit(ev_id, HAS_SUPPORTING_REFERENCE, o)
        self.evidences.append(evidence)
        return evidence.id

    # Use only for OWLAxioms
    # There are two of these methods. AnnotonCamRdfTransform.find_bnode and GoCamModel.find_bnode. Which one is used?
    def find_bnode(self, triple):
        (subject,predicate,object_id) = triple
        s_triples = self.writer.graph.triples((None, OWL.annotatedSource, subject))
        s_bnodes = [s for s,p,o in s_triples]
        p_triples = self.writer.graph.triples((None, OWL.annotatedProperty, predicate))
        p_bnodes = [s for s,p,o in p_triples]
        o_triples = self.writer.graph.triples((None, OWL.annotatedTarget, object_id))
        o_bnodes = [s for s,p,o in o_triples]
        bnodes = set(s_bnodes) & set(p_bnodes) & set(o_bnodes)
        if len(bnodes) > 0:
            return list(bnodes)[0]

    def emit_axiom(self, source_id, property_id, target_id):
        stmt_id = self.blanknode()
        self.emit_type(stmt_id, OWL.Axiom)
        self.emit(stmt_id, OWL.annotatedSource, source_id)
        self.emit(stmt_id, OWL.annotatedProperty, property_id)
        self.emit(stmt_id, OWL.annotatedTarget, target_id)
        return stmt_id

    def find_annotons(self, enabled_by, annotons_list=None):
        found_annotons = []
        if annotons_list is not None:
            annotons = annotons_list
        else:
            annotons = self.annotons
        for annoton in annotons:
            if annoton.enabled_by == enabled_by:
                found_annotons.append(annoton)
        return found_annotons

    def add_individual(self, individual_id, annoton):
        obj_uri = self.uri(individual_id)
        if individual_id not in annoton.individuals:
            tgt_id = genid(base=self.writer.base + '/')
            annoton.individuals[individual_id] = tgt_id
            self.emit_type(tgt_id, obj_uri)
            self.emit_type(tgt_id, OWL.NamedIndividual)
        else:
            tgt_id = annoton.individuals[individual_id]
