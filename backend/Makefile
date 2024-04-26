lint:
	ruff check --diff . 
	@echo
	ruff format --diff .
	@echo
	mypy .

format:
	ruff check --silent --exit-zero --fix .
	@echo 
	ruff format .

audit: 
	pip-audit

pytest:
	pytest .
