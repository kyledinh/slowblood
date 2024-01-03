export SHELL := /bin/bash

## VARS AND ENVS
REPO_DIR ?= $(shell pwd | xargs echo -n)

## MAIN ####
.PHONY: check setup pkg-build pkg-push

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