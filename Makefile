export SHELL := /bin/bash

## VARS AND ENVS
REPO_DIR ?= $(shell pwd | xargs echo -n)

## MAIN ####
.PHONY: check setup pkg-build pkg-push

# list the targets for this Makefile
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | sort"

check:
	@echo "#####################################"
	@echo "Python3: $(shell python3 --version)"
	@echo "PIP: $(shell pip3 --version)"
	@echo "REPO_DIR: $(REPO_DIR)"
	@cd scripts && ./check-cpu.sh
	@cd scripts && ./check-installed.sh
	@echo $(ARG)

conda:
	conda create --name slowblood python=3.10.12

setup:
	@echo "SETUP:"
	@cd scripts && ./setup-init.sh


## pypi slowblood package targets 
pkg-build:
	@echo "Building pypi slowblood package"
	@rm -rf pypi/dist
	@cd pypi && python -m build 

pkg-push:
	@echo "Pusing slowblood package to pypi"
	@cd pypi && python -m twine upload --repository pypi dist/* --verbose

pkg-push-test:
	@echo "Pusing slowblood package to TEST pypi"
	@cd pypi && python -m twine upload --repository testpypi dist/* --verbose

## RUNPOD
# python cli-get-info-runpod.py
rp-info:
	@echo "Getting info and available GPUs"
	python -c "import slowblood;slowblood.runpod_get_available_gpus()"

deploy-codellama:
	@echo "Deploy a 13B CodeLlama with 32K Context LLM to Run Pod"
	python cli-deploy-to-runpod-codellama-13B.py

deploy-notebook:
	@echo "Deploy a Python Notebook Server to Run Pod"
	python cli-deploy-to-runpod-notebook.py	
	open https://www.runpod.io/console/pods

deploy-trelis-notebook:
	@echo "Deploy a Python Notebook Server to Run Pod"
	python cli-deploy-to-runpod-trelis-notebook.py	
	open https://www.runpod.io/console/pods
# open https://www.runpod.io/console/gpu-secure-cloud