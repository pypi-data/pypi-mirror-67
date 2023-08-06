# Installation
## Requirements
* python versions >=2.7 or >=3.0
## PyPI
From user side, we recommend the installation via PyPI: 
```bash
pip install w7x
```
In this process all dependencies are resolved automatically.

## Git
If you want to keep on track very tightly to the project and or want to support development, clone the git to your <favourite_directory> and set the $PYTHONPATH variable.
```bash
cd favourite_directory
git clone https://gitlab.mpcdf.mpg.de/dboe/tfields.git  # clone the repository
git submodule update --init --recursive  # also clone all submodules (developer tools only. The code can run without this step.)
echo 'export PYTHONPATH=$PYTHONPATH:</path/to/my/facvourite_directory/w7x>' >> ~/.bashrc  # permanently set the $PYTHONPATH variable
source ~/.bashrc # make the PYTHONPATH change active
```


# Developers only:
## Testing and Coverage:
This code is tested. New versions are only published, if the code coverage lies above 80% with no failing unit test.
If you want to check any of this, you have to download the code via git (see above)
In the tfields directory, run
```bash
make test
```

To check the coverage, run
```bash
make coverage
```

## Git Hooks
To set up the shared git hooks, run
```bash
make init
```

## Publishing to PyPI
Publishing new versions of the code:
*Change the version number in tfields/__about__.py
*Then run
```bash
make publish
```


# About
This library is in active development. We are still in alpha status but things are progressing fast. If you wish to get an idea, what this library is capable of, have a look in tfields/core.py e.g. the Tensors class and read the Examples (all doctests included in unittesting). Also tfields/mesh3D.py could be an interesting point to start if you would like to work with 3D meshes.
