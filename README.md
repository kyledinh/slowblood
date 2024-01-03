# SLOWBLOOD 
> Tools for ML/LLM 

<br><br>
## Table of Contents

- [Software Requirements](#software-requirements)
- [pypi](#pypi)

<br><hr><br>

## Software Requirements

Software | Version | Desc
---------|---------|--------------------------
conda    |         | `conda create --name slowblood python==3.10`
python   | 3.10 +  |
pip      |         | `apt install python3-pip`
make     |         |

### Conda commands

- `conda env list`
- `conda activate slowblood`
- `conda deactivate`

<br><hr><br>

## Pypi 
- `make check` - Inspect for install versions
- `make setup` - Setup files and directories (.env)
- `make pkg-build` - Builds a Python package with version in setup.cfg  
- `make pkg-push` - Push the Python package to Pypi for pip installation 

<br><hr><br>

## Resources
- https://huggingface.co/Slowblood
- https://huggingface.co/
- https://style-guides.readthedocs.io/en/latest/makefile.html
- https://packaging.python.org/en/latest/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
