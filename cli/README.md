# Getting Started for CLI

These instructions will assist you to get the best experience with the CLI.

## Prerequisites

* Python 3.8.6 or above

## Installing & Preparation

1. Download the repository and extract it to any folder.
2. Create a virtual environment in the root folder with using ``python -m venv venv`` command.
3. Activate the virtual environment with using ``source venv/bin/activate`` for MacOS/Linux and ``venv\Scripts\activate`` for Windows.
4. Enter into ``cli`` folder and install required python packages with using ``pip install -r requirements.txt``.

## Running

1. Define environmental variable ``API_STAGE=prod`` to use the API that is hosted in PythonAnywhere. Otherwise, set ``API_STAGE=dev`` to use your local Flask API server. You can set your environmental variable with putting this into ``.env`` file in the folder or exporting with ``export API_STAGE=prod`` for MacOS/Linux systems.
2. Execute ``python interface.py --help`` command firstly to list available endpoints and required arguments for each endpoint.
3. Example usage: ``python interface.py --endpoint historical --date-from 2021-05-19 --date-to 2021-05-28``

## Testing
1. Execute ``pytest test_interface.py`` command.

### Resources

* https://click.palletsprojects.com/en/8.0.x/
* https://pymbook.readthedocs.io/en/latest/click.html
* https://click.palletsprojects.com/en/8.0.x/testing/
* https://stackoverflow.com/questions/26767104/testing-click-python-applications
