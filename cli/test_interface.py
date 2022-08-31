from click.testing import CliRunner
from interface import main


def test_endpoint_with_parameters():
    runner = CliRunner()
    result = runner.invoke(
        main, ['--endpoint', 'historical', '--date-from', '2021-05-19',
               '--date-to', '2021-05-28'])
    print(result.output)
    assert result.exit_code == 0
    assert len(result.output) >= 200


def test_endpoint_with_wrong_parameters():
    runner = CliRunner()
    result = runner.invoke(
        main, ['--endpoint', 'historical', '--date-from', '2021-05-28',
               '--date-to', '2021-05-19'])
    print(result.output)
    assert result.exit_code == 0
    assert result.output == 'please check time range field(s)!\n'


def test_endpoint_without_parameters():
    runner = CliRunner()
    result = runner.invoke(main, ['--endpoint', 'latest'])
    assert result.exit_code == 0
    assert len(result.output) >= 80
