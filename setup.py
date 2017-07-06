from setuptools import setup

__name__ = "lb_colloids"
__author__ = "Joshua D Larsen"
__version__ = "0.1"

long_description = """PhD project of Joshua D Larsen at the University of Arizona
  Department of Soil Water and Environmental Sciences. This python package contains classes
  and functions to build and run lattice Boltzmann computation fluid dynamics models on two
  dimensional images of geological materials. The Colloids portion contains modeling tools to
  simulate the chemical and physical dynamics of colloid transport in the lattice boltzmann domain
  post CFD simulation. This project is open source, and I invite collaboration to make this tool
  better! Publication of this work is in progress. Relevent pubs will be listed appropriately. Documentation
  of physical and chemical equations can be located in the doc-strings."""

setup(name=__name__,
      author=__author__,
      author_email='jdlarsen@email.arizona.edu',
      version=__version__,
      description="A D2Q9 lattice Boltzmann modeling tool to simulate colloid transport",
      long_description=long_description,
      install_requires=['numpy', 'matplotlib', 'pandas', 'scipy'],
      python_requires="=2.7.*"
      )
