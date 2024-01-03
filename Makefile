export SHELL := /bin/bash

## VARS AND ENVS
REPO_DIR ?= $(shell pwd | xargs echo -n)

## MAIN ####
.PHONY: check setup pkg-build pkg-push

# list the targets for this Makefile
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | sort"

check:
	@echo "Python3: $(shell python3 --version)"
	@echo "PIP: $(shell pip3 --version)"
	@echo "REPO_DIR: $(REPO_DIR)"
	@cd scripts && ./check-cpu.sh
	@echo $(ARG)

setup:
	@echo "SETUP:"
	@cd scripts && ./setup-init.sh


## pypi slowblood package targets 
pkg-build:
	@echo "Building pypi gpt-prive package"
	@cd pypi && python -m build 

pkg-push:
	@echo "Pusing gpt-prive package to pypi"
	@cd pypi && python -m twine upload --repository pypi dist/* 


## RUNPOD
deploy-codellama:
	@echo "Deploy a 13B CodeLlama with 32K Context LLM to Run Pod"
	python cli-deploy-to-runpod-codellama-13B.py

deploy-notebook:
	@echo "Deploy a Python Notebook Server to Run Pod"
	@echo "!!!!! DOES NOT WORK YET, need to find the correct Docker image to run the Jupyter Notebook and env settings!!!!!!"
	@echo "TRY MANUALLY:"
	open https://www.runpod.io/console/gpu-secure-cloud
#python cli-deploy-to-runpod-notebook.py	