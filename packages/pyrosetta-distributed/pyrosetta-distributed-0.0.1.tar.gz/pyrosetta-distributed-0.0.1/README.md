# pyrosetta-distributed
A module that enables the distributed and pydata integration features of PyRosetta

## How to build package for release and upload to PyPI
```
pip install --user --upgrade setuptools wheel twine
python setup.py sdist bdist_wheel
twine upload dist/*
```
