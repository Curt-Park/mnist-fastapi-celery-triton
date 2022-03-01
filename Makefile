PYTHON=3.9
N_PROC=8
CONDA_CH=conda-forge defaults
BASENAME=$(shell basename $(CURDIR))
NVCC_USE=$(notdir $(shell which nvcc 2> NULL))

env:
	conda create -n $(BASENAME)  python=$(PYTHON)

setup:
	conda install --file requirements.txt $(addprefix -c ,$(CONDA_CH))
	pip install -r requirements-pip.txt  # separated for M1 chips

ifeq ($(NVCC_USE),nvcc)
	conda install -y --file requirements-gpu.txt $(addprefix -c ,$(CONDA_CH))
endif

broker:
	redis-server

worker:
	# auto-restart for script modifications
	PYTHONPATH=src watchmedo auto-restart \
		--directory=src/worker \
		--pattern=*.py \
		--recursive -- \
		celery -A worker.celery worker -P processes -c $(N_PROC) -l INFO

api:
	PYTHONPATH=src uvicorn api.server:app --reload --host 0.0.0.0 --port 8000

dashboard:
	sh -c "./wait_for_workers.sh"
	PYTHONPATH=src celery -A worker.celery flower --port=5555


# For developers
setup-dev:
	conda install --file requirements-dev.txt $(addprefix -c ,$(CONDA_CH))
	pre-commit install

format:
	black .
	isort .

lint:
	pytest src --flake8 --pylint --mypy

utest:
	PYTHONPATH=src pytest test/utest --cov=src --cov-report=html --cov-report=term --cov-config=setup.cfg

cov:
	open htmlcov/index.html
