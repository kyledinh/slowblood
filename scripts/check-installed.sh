#!/bin/bash
# Checks for installed software packages 

function fn_check_conda {
  if command -v conda >/dev/null 2>&1; then
    conda --version
  else
    echo "!!! Conda is recommended to manage pip and dependencies. https://conda.io/projects/conda/en/latest/user-guide/getting-started.html#managing-python."; 
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

## MAIN
echo "Checking installed software packages:"
echo "docker, conda, make"
echo

fn_check_docker
fn_check_conda
fn_check_make
fn_check_python