import os
import click
import requests


ENDPOINTS = ["latest", "latest/average", "historical", "historical/average",
             "average/highest", "average/lowest"]
PARAMETER_REQUIRED_ENDPOINTS = ["historical", "historical/average"]


def validate_inputs(endpoint: str, date_from: str, date_to: str):
    if endpoint in ENDPOINTS:
        if endpoint in PARAMETER_REQUIRED_ENDPOINTS:
            if date_from is None or date_to is None:
                click.echo("Please define the required parameters for this endpoint! For more info: `python interface.py --help`")
                return False
            else:
                return True
        else:
            return True
    else:
        click.echo("Please define or check the endpoint. For more info: `python interface.py --help`")


def get_response(endpoint, date_from: str, date_to: str):
    if os.environ['API_STAGE'] == 'prod':
        url = 'https://metinakin.pythonanywhere.com/{}'.format(endpoint)
    else:
        url = 'http://127.0.0.1:5000/{}'.format(endpoint)

    if date_from and date_to:
        query_params = {
            'from': date_from,
            'to': date_to,
        }
    else:
        query_params = {}

    response = requests.get(url, params=query_params)

    return response.json()


@click.command()
@click.option(
    '--endpoint', default=None, help='API endpoint to the related call',
)
@click.option(
    '--date-from', default=None, help='format: 2021-05-19',
)
@click.option(
    '--date-to', default=None, help='format: 2021-05-28',
)
def main(endpoint, date_from, date_to):
    '''
    - This CLI enables you to query data from the API\n
    - Available endpoints and required arguments:\n
    \tlatest\n
    \tlatest/average\n
    \thistorical --date-from DATE --date-to DATE\n
    \thistorical/average --date-from DATE --date-to DATE\n
    \taverage/highest\n
    \taverage/lowest\n
    '''
    if validate_inputs(endpoint, date_from, date_to):
        results = get_response(endpoint, date_from, date_to)

        if "error" in results:
            click.echo(results["error"])
        else:
            for result in results:
                for key, value in result.items():
                    click.echo(str(key) + " " + str(value))
                click.echo("------------------------")
    else:
        raise click.Abort()


if __name__ == "__main__":
    main()
