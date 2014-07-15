from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='PaqueteNuevo',
      version=version,
      description="Ejemplo de nuevo paquete",
      long_description="""\
Ejemplo de nuevo paquete parte 2""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='package python egg conjuntos tostadas pipo',
      author='Nelson Bracho',
      author_email='brachoemil@gmail.com',
      url='https://github.com/nbrach/tostadaspipo',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
