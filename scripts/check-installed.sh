#!/bin/bash
# Checks for installed software packages 

function fn_check_conda {
  if command -v conda >/dev/null 2>&1; then
    conda --version
  else
    echo "!!! Conda is recommended to manage pip and dependencies. https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-python."; 
  fi
}

function fn_check_cuda {
  if command -v nvcc >/dev/null 2>&1; then
    nvcc --version
  else
    echo "!!! CUDA is not installed."; 
  fi
}

function fn_check_docker {
  if command -v docker >/dev/null 2>&1; then
    docker --version
  else
    echo "!!! docker required, but it's not installed."; 
  fi
}

function fn_check_make {
  if command -v make >/dev/null 2>&1; then
    make --version
  else
    echo "!!! make required, but it's not installed."; 
  fi
}

function fn_check_python {
  if command -v python >/dev/null 2>&1; then
    python --version
  else
    echo "!!! python required, but it's not installed."; 
  fi
}

function fn_check_pypi_module {
  MODULE=$1
  MODULE_VERSION=$(pip list | grep $MODULE)
  if [[ $MODULE_VERSION ]]; then
    echo "$MODULE_VERSION is installed."
  else
    echo "NOT installed: $MODULE"
  fi
}


## MAIN
echo; echo;
echo "#####################################" 
echo "Checking installed software packages:"
echo "docker, conda, cuda, make, python and pip dependencies"
echo

fn_check_docker
fn_check_conda
fn_check_cuda
fn_check_make
fn_check_python

echo
echo "Slowblood installed module dependencies: "
fn_check_pypi_module build 
fn_check_pypi_module twine
echo 
fn_check_pypi_module gpt4all 
fn_check_pypi_module huggingface_hub 
fn_check_pypi_module python-dotenv 
fn_check_pypi_module runpod 
fn_check_pypi_module transformers 