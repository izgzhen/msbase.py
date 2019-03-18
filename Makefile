.phony: tar publish

# https://packaging.python.org/tutorials/packaging-projects/
#

PIP:=.venv/bin/pip
PYTHON:=.venv/bin/python
TWINE:=.venv/bin/twine

tar:
	rm -rf dist
	$(PIP) install --upgrade setuptools wheel
	$(PYTHON) setup.py sdist bdist_wheel

publish:
	$(TWINE) upload dist/*

test:
	$(PYTHON) test.py 1
