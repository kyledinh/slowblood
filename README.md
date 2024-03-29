# SLOWBLOOD 
> Tools for ML/LLM 

<br><br>
## Table of Contents

- [Software Requirements](#software-requirements)
- [pypi](#pypi)
- [Deploying Environments with GPUs](#deploying-environments)

<br><hr><br>

## Software Requirements

Software | Version | Desc
---------|---------|--------------------------
conda    |         | `conda create --name slowblood python==3.10`
python   | 3.10.12 | `python --version`
pip      |         | `apt install python3-pip`
make     |         |

### Conda commands

- `make conda` - (run once to create the "slowblood" environment)
- `conda env list`
- `conda activate slowblood`
- `conda deactivate`

<br><hr><br>

## Pypi 
> Commands to build and push the `slowblood` python package, make sure to update the version in `setup.cfg`

- `make check` - Inspect for install versions
- `make setup` - Setup files and directories (.env)
- `make pkg-build` - Builds a Python package with version in setup.cfg  
- `make pkg-push` - Push the Python package to Pypi for pip installation 

<br>


### Required Dependencies 
- build, twine

### Build
- Update `src/*` and update `setup.conf`
- Builds to `dist/` directory
```
python -m build
```
- Push to PyPi with twine
```
python -m twine upload --repository pypi dist/*
```

### Setup
- Create API key in PyPI account
- Add to `~/.pypirc`
```
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
  username = __token__
  password = pypi-AgszLCJ-Cut-And-P@aste-The-API-K#y-From-Your-AccountlZ7-mow

[testpypi]
repository = https://test.pypi.org/legacy/
```

<br><hr><br>


## Deploying Environments 
> Helpful scripts and Make targets to deploy work environments with GPUs, using RunPod and its API.

- `make deploy-notebook` will deploy a Juptyer server 
- `make deploy-codellama` will deploy a CodeLlama 13B with 32K context window Inference Server to a RunPod
- `make list` - shows available Make targets 

<br><hr><br>

## Local Usage for Development, import from local file system

```
import sys
sys.path.append('/Users/kyle/src/github.com/kyledinh/slowblood')
from pypi.src import slowblood 

slowblood.help()
```

<br><hr><br>

## Resources
- https://huggingface.co/Slowblood
- https://huggingface.co/
- https://style-guides.readthedocs.io/en/latest/makefile.html
- https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
