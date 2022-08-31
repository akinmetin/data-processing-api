'''
This module includes the Utils class that
includes required functions for validation
'''
from datetime import datetime
import logging as _logging

_logging.basicConfig(
    format='%(asctime)s - [%(levelname)s] %(funcName)s - %(message)s',
    level='DEBUG')
LOGGER = _logging.getLogger(__name__)


def validate_date(date_from: str, date_to: str) -> bool:
    '''
    Takes date_from and date_to string parameters and returns
    boolean `True` or `False` value regarding the result of validation
    '''
    if date_from is None or date_to is None:
        LOGGER.warning("Unexpected type of date boundries: [%s, %s]",
                       date_from, date_to)
        return

    # length of the string date should be always 10, eg. "2021-04-19"
    if len(date_from) != 10 or len(date_to) != 10:
        return

    try:
        datetime_from = datetime.strptime(date_from, '%Y-%m-%d').timestamp()
        datetime_to = datetime.strptime(date_to, '%Y-%m-%d').timestamp()

        if datetime_from > datetime_to:
            LOGGER.warning(
                "Lower limit cannot be bigger than bigger limit: %f < %f",
                datetime_from, datetime_to)
            return False
        return True
    except ValueError:
        LOGGER.warning("Provided date format is not supported: %s or %s",
                       date_from, date_to)
    except Exception as exc:
        LOGGER.warning("Unhandled exception is occured: %s", str(exc))
