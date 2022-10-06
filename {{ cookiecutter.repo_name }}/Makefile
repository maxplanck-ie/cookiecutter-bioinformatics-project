.PHONY: clean data lint requirements fetch_data pipeline

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = {{ cookiecutter.repo_name }}

ifeq (,$(shell which conda))
HAS_CONDA=False
else
HAS_CONDA=True
endif

CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate

# use this function to load modules on the cluster
# usage in Makefile: $(call module-load,snakemake) && snakemake -j1 ...
define module-load
        eval `/usr/bin/modulecmd bash load $(1)`
endef


#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements: test_environment
	#python3 -m pip install -U pip setuptools wheel
	#python3 -m pip install -r requirements.txt

## Make Dataset
data:
	fetch_data
	pipeline

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	eval "$(conda shell.bash hook)"
	conda activate $(PROJECT_NAME)
	flake8 src

## Fetch the raw data, either from local or remote sources. IMPLEMENT ME!
fetch_data:
	echo "Implement fetch of data"
	# some suggested commands
	# ln -s --relative /path/to/your/data data/
	# wget https://url.com/of/your/data

## Set up python interpreter environment
create_environment:
ifeq (True,$(HAS_CONDA))
	@echo ">>> Detected conda, creating conda environment."
	conda env create -f environment.yaml
	@echo ">>> New conda env created. Activate with: "
	@echo "conda activate $(PROJECT_NAME)"
else
	@echo "Error: conda not detected. Exiting. "
	exit 1
endif

## Test python environment is setup correctly
test_environment:
	eval "$(conda shell.bash hook)"
	conda activate $(PROJECT_NAME)
	python3 test_environment.py

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

## Execute the data pipeline. IMPLEMENT ME!
pipeline:
	echo "Implement running of pipeline"	
	# suggested commands as follows
	#module load snakemake # specific to MPI-IE infrastructure
	#snakemake -s workflow/Snakefile -j 1 --workdir workflow --profile /path/to/mpi-ie-slurm/mpi-ie-slurm all

#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
