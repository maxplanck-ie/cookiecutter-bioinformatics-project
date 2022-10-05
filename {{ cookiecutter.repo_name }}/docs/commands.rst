Commands
========

The Makefile contains the central entry points for common tasks related to this project.

Downloading data based on DOI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{% if 'zenodo' in cookiecutter.data_doi.lower() %}
* `make download_data` will use `zenodo_get` to download the data from Zenodo.
{% elif 'opendata' in cookiecutter.data_doi.lower() %}
* `make download_data` will use `cernopendata-client` to download the data from the CERN Open Data Portal.
{% else  %}
* `make download_data` needs to be implemented.
{% endif %}
