# CUSIP Generator

CUSIP generator API, built in Flask.

## Requirements

* Mac OS X, Windows, Linux
* Python 3.6 or newer
* pip
* virtualenv

## Quick start

### Setting up virtual environment

Assuming that you have `virtualenv` installed locally. Instructions here are for Mac/Linux. YMMV.

Refer to the official [documentation](https://virtualenv.pypa.io/en/stable/installation/) for installation instructions if needed.

Create your virtual environment:

`python3 -m venv [venv_name]`

Activate your virtual env:

`source [virtual_env_directory]/[venv_name]/bin/activate`

Install the required dependencies: `pip install -r requirements.txt`

## Running the application

Run `FLASK_APP=app.py flask run` to run the application locally.

## Tests

Run `pytest` to test the API and its endpoints.

Run `pytest --pyargs [module_name]` to run specific tests. 

Here, we can run `pytest --pyargs cusip` to run the tests for CUSIP generation only.
