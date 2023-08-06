import setuptools

with open("pyrosetta_distributed/requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrosetta-distributed",
    version="0.0.1",
    author="Brian D. Weitzner",
    author_email="bweitzner@lyell.com",
    description="Enables the distributed and pydata integration features of PyRosetta",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RosettaCommons/pyrosetta-distributed/",
    packages=["pyrosetta_distributed"],
    install_requires=install_requires,
    python_requires='>3.3',
    license="MIT License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
