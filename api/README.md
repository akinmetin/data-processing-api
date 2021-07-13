# Getting Started for API Server

These instructions will assist you to run the API server.

## Prerequisites

* Python 3.8.6 or above

## Installing & Preparation for Local Environment

1. Download the repository and extract it to any folder.
2. Create a virtual environment in the root folder with using ``python -m venv venv`` command.
3. Activate the virtual environment with using ``source venv/bin/activate`` for MacOS/Linux and ``venv\Scripts\activate`` for Windows.
4. Enter into ``api`` folder and install required python packages with using ``pip install -r requirements.txt``.

## Running Locally

1. Define environmental variable ``DEBUG_MODE=1`` to run the Flask API with DEBUG mode or set ``DEBUG_MODE=0`` to run the Flask API without DEBUG mode. You can set your environmental variable with putting this into ``.env`` file in the folder or exporting with ``export DEBUG_MODE=1`` for MacOS/Linux systems.
2. Execute ``python app.py`` command.

## Creating and Running Flask API Server on PythonAnywhere

1. [Signup or Login](https://www.pythonanywhere.com/) to the platfrom.
2. Click ``Web`` tab in the homepage.
3. Click ``Add a new web app`` button on the left side.
4. Select the following options in the Quickstart Setup Wizard:
    - Select a Python Web framework: **Flask**
    - Select a Python version: **Python 3.8**
    - Path: **/home/<your_username>/api/app.py** (enter the path that you are planning deploy your application)
5. Click ``Files`` tab in the homepage.
6. Go to the directory that you have speficied during the Quickstart Setup Wizard and includes ``app.py`` file.
7. Upload your files into this folder with the same hierarchy as in your ``/api`` folder.

    **Note:** If you are initializing your Flask object (``app = create_app()``) under ``if __name__ == '__main__':``, you need to move this to the global scope since PythonAnywhere is not executing the ``app.py`` file directly and their WSGI server is trying to import the ``app`` variable from this file to another file.

8. Click ``Web`` tab in the homepage and then click green ``reload <your_app_url>`` button.
9. You are ready to go! You can use the url that is written inside the green reload button.

### Allowed API HTTP(s) requests
| Request Type | Use                                 |
| ------------ |:----------------------------------- |
| GET          | Get a resource or list of resources |

## API Endpoints

* PythonAnywhere API Endpoint: ``https://metinakin.pythonanywhere.com``

| Request Type      | Endpoint                    | What it does                                                 |
| ----------------- |:--------------------------- |:------------------------------------------------------------ |
| ``GET``           | /latest                     | Returns the latest stock data                                |
| ``GET``           | /latest/average             | Returns the latest stock data's average value                |
| ``GET``           | /historical                 | Returns the historical stock data                            |
| ``GET``           | /historical/average         | Returns the historical stock data's average value            |
| ``GET``           | /average/highest            | Returns the stock data that has the highest average value    |
| ``GET``           | /average/lowest             | Returns the stock data that has the lowest average value     |

### Description of Usual Server Responses

*   200 OK - the request was successful.
*   201 Created - the request was successful and a resource was created.
*   204 No Content - the request was successful but there is no representation to return (i.e. the response is empty).
*   400 Bad Request - the request could not be understood or was missing required parameters.
*   401 Unauthorized - authentication failed or user doesn't have permissions for requested operation.
*   403 Forbidden - access denied.
*   404 Not Found - resource was not found.
*   405 Method Not Allowed - requested method is not supported for resource.
*   500 Internal Server Error - the server encountered an unexpected condition which prevented it from fulfilling the request.

## Development

* ``flake8`` and ``pylint`` libraries are used for coding standards and quality testing.

## Testing
1. Execute ``python -m unittest discover -s tests/`` for running all the test files at once or ``python -m unittest tests/<file_name>.py`` for running each test file seperately.

## Coverage

1. Enter into ``api`` folder and execute ``coverage run -m unittest discover -s tests/ -p test_*.py``
2. Execute ``coverage report -m`` command to get the coverage report.

| File Name              | Coverage                       |
| ---------------------- |:------------------------------ |
| ``app.py``             | ``88%``                        |
| ``data_processor.py``  | ``100%``                       |
| ``utils.py``           | ``89%``                        |

### Resources for Flask

* https://flask.palletsprojects.com/en/2.0.x/
* https://flask.palletsprojects.com/en/2.0.x/testing/

### Resources for the Deployment on PythonAnywhere
* https://help.pythonanywhere.com/pages/Flask/

### Resources for Data Analyzing

* https://www.kaggle.com/varpit94/apple-stock-data-updated-till-22jun2021
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
* https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.assign.html
