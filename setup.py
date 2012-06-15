from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='vtv.pruebaluis',
      version=version,
      description="descripcion corta",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone4',
      author='luis eduardo florez bautista',
      author_email='lflorez@vtv.gob.ve',
      url='https://github.com/lefway/vtv.pruebaluis',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['vtv'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'collective.autopermission',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],

      )
