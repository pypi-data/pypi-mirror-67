from setuptools import setup

setup(name='hdproc',
      version='0.32',
      description='Implementation of Hierarchical LDA',
      url='http://github.com/datadiarist/hdproc',
      author='Andrew and Eduardo',
      author_email='andrew.carr@duke.edu',
      license='MIT',
      packages=['hdproc'],
      install_requires=[
          'cppimport',
      ],
      zip_safe=False)
