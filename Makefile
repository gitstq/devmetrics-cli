# DevMetrics-CLI Makefile

.PHONY: help install test clean lint format build publish

help:
	@echo "DevMetrics-CLI - Available commands:"
	@echo "  make install    - Install package in development mode"
	@echo "  make test       - Run tests"
	@echo "  make clean      - Clean build artifacts"
	@echo "  make build      - Build distribution packages"
	@echo "  make run        - Run devmetrics with sample data"

install:
	pip install -e .

test:
	python -m pytest tests/ -v

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python setup.py sdist bdist_wheel

run:
	python devmetrics.py

run-json:
	python devmetrics.py --json
