from setuptools import setup

setup(
  name='comandarr',
  version='0.1',
  packages=['comandarr'],
  license='Creative Commons',
  long_description=open('README.md').read(),
  setup_requires=['pytest-runner'],
  tests_require=['pytest'],
)

# To create a Python package that can be installed via pip run the following
# commands in the terminal.
# python setup.py resiter
# python setup.py sdist upload

# REFERENCE: https://marthall.github.io/blog/how-to-package-a-python-app/
