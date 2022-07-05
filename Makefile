install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py lib

test:
	python -m pytest -vv --cov=lib test_*.py

format:
	black *.py lib/*.py

all: install post-install lint test format deploy


