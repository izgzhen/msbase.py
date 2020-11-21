.phony: tar publish

# https://packaging.python.org/tutorials/packaging-projects/
#

PIP:=.venv/bin/pip
PYTHON:=.venv/bin/python
TWINE:=.venv/bin/twine

PYFILES := $(shell find msbase -name "*.py") test.py

check:
	ck $(PYFILES)

tar:
	rm -rf dist
	$(PIP) install --upgrade setuptools wheel
	$(PYTHON) setup.py sdist bdist_wheel

publish: tar
	$(TWINE) upload dist/*

test: check
	$(PYTHON) test.py 1

venv:
	python3 -m venv .venv