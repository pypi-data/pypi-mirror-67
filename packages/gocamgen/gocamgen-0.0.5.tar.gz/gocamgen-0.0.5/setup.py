from setuptools import setup, find_packages

setup(
    name="gocamgen",
    version='0.0.5',
    # packages=["gocamgen"],
    packages=find_packages(),
    author="dustine32",
    author_email="debert@usc.edu",
    description="Python library for constructing GO-CAM model RDF",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/dustine32/gocamgen",
    install_requires=[
        "ontobio==1.13.1",
        "PyShEx==0.7.11"
    ]
)
