.PHONY: run test format format-check security setup

run:
	python main.py

test:
	python -m unittest unittests.py
	python -m doctest main.py

format:
	black .

format-check:
	black --check .

security:
	safety check -r requirements.txt

setup:
	pip install -r requirements.txt