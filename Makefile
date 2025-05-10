

setup-deps:
	python -m pip install hatch pre-commit
	pre-commit install

fmt: 
	hatch fmt

test:
	hatch test

pre-commit:
	pre-commit run --all-files

types:
	hatch run types:check

cli:
	hatch run cli:l2d