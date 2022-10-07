{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

├── CITATION.cff       <- Contains metadata on how the project might eventually be published. 
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── config             <- Configuration options for the analysis. 
|   ├── config.yaml    <- Snakemake config file. 
|   └── samples.tsv    <- A metadata table for all the samples run in the analysis.  
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── environment.yaml   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `conda env export > environment.yaml`
│
├── img                <- A place to store images associated with the project/pipeline, e.g. a 
│                         a figure of the pipeline DAG. 
│
├── notebooks          <- Jupyter or Rmd notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── resources          <- Place for data. By default excluded from the git repository. 
│   ├── external       <- Data from third party sources.
│   └── raw_data       <- The original, immutable data dump.
│
├── results            <- Final output of the data processing pipeline. By default excluded from the git repository.
│ 
├── sandbox            <- A place to test scripts and ideas. By default excluded from the git repository.
│ 
├── scripts            <- A place for short shell or python scripts.
│ 
├── setup.py           <- Makes project pip installable (pip install -e .) so src can be importe
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
├── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
│
├── workflow           <- Place to store the main pipeline for rerunning all the analysis. 
│   ├── envs           <- Contains different conda environments in .yaml format for running the pipeline. 
│   ├── rules          <- Contains .smk files that are included by the main Snakefile, including common.smk for functions. 
│   ├── scripts        <- Contains different R or python scripts used by the script: directive in Snakemake.
│   ├── Snakefile      <- Contains the main entrypoint to the pipeline.
│ 
├── workspace          <- Space for intermediate results in the pipeline. By default excluded from the git repository.  

--------

<p><small>Project inspired by the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a> and
the <a target="_blank" href="https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html">Snakemake workflow template</a>. </small></p>
