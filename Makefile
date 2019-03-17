.phony: tar publish

# https://packaging.python.org/tutorials/packaging-projects/

tar:
	rm -rf dist
	pip install --upgrade setuptools wheel
	python3 setup.py sdist bdist_wheel

publish:
	twine upload dist/*

test:
	python3 test.py 1
