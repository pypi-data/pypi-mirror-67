from setuptools import setup, Extension

test_module=Extension('hdproc',
 sources=['hdproc/hdp_preproc.cpp'],
 language='c++'
)

setup(name='hdproc',
      version='0.38',
      description='Implementation of Hierarchical LDA',
      url='http://github.com/datadiarist/hdproc',
      author='Andrew and Eduardo',
      author_email='andrew.carr@duke.edu',
      license='MIT',
      packages=['hdproc'],
      install_requires=[
      'cppimport',
      ],
      ext_modules=[test_module],
      zip_safe=False)
