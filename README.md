# Cookiecutter Bioinformatics

_A logical, reasonably standardized, but flexible project structure for doing and sharing bioinformatics work._

This cookiecutter template was developed by the [Max Planck Institute of Immunobiology and Epigenetics Bioinformatics Core Facility](https://www.ie-freiburg.mpg.de/bioinformatics) with the aim of establishing a standardized project directory structure within the institute. It is a fork of [cookiecutter-fair-data-science](https://github.com/FAIR4HEP/cookiecutter-fair-data-science), with a healthy dose of [Snakemake workflow best practices](https://snakemake.readthedocs.io/en/stable/snakefiles/deployment.html#distribution-and-reproducibility) mixed in. There is less focus on building a python package that can train and run machine learning models, but rather on building bioinformatics workflows that can run on the MPI-IE cluster according to [FAIR principles](https://www.go-fair.org/fair-principles/). 

#### [Project homepage](https://github.com/dkoppstein/cookiecutter-bioinformatics-project)


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

On the MPI-IE infrastructure, you can also run `module load cookiecutter`. 

### To start a new project, run:
------------

    cookiecutter gh:maxplanck-ie/cookiecutter-bioinformatics-project


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
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
```

## Contributing

We welcome contributions! Feel free to fork and add pull requests. 

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    py.test tests
