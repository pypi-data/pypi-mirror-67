# Parse GAF file, get assocs
# Create class that accepts list of assocs and creates a model, with connections if len(assocs) > 1
# Interpret extensions field - may require calculating aspect of term; also, determining if GP

from gocamgen import GoCamModel, AssocGoCamModel, CamTurtleRdfWriter, Annoton
from ontobio.rdfgen.assoc_rdfgen import SimpleAssocRdfTransform, CamRdfTransform
from ontobio.io.gafparser import GafParser

parser = GafParser()
assocs = parser.parse("resources/gene_association.pombase_one", skipheader=True)

print(len(assocs))

model = AssocGoCamModel("test_from_assocs", assocs)
model.translate()
# model = GoCamModel("test")
# model.declare_class(assocs[0]["subject"]["id"])




