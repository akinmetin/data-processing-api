'''
This module includes the Utils class that
includes required functions for validation
'''
from datetime import datetime
import logging

logging.basicConfig(format='%(asctime)s - [%(levelname)s] %(funcName)s - %(message)s',
                    level='DEBUG')
LOGGER = logging.getLogger(__name__)


class Utils():
    '''
    This class includes the required validate_date() function
    to validate endpoint date from and date to parameters
    '''
    def __init__(self) -> None:
        pass

    def validate_date(self, date_from: str, date_to: str) -> bool:
        '''
        Takes date_from and date_to string parameters and returns
        boolean `True` or `False` value regarding the result of validation
        '''
        if date_from is None or date_to is None:
            LOGGER.warning("Unexpected type of date boundries!")
            return False

        # length of the string date should be always 10, eg. "2021-04-19"
        if len(date_from) == 10 and len(date_to) == 10:
            try:
                datetime_from = datetime.strptime(date_from, '%Y-%m-%d').timestamp()
                datetime_to = datetime.strptime(date_to, '%Y-%m-%d').timestamp()

                if datetime_from > datetime_to:
                    LOGGER.warning("Lower limit cannot be bigger than bigger limit!")
                    return False
            except ValueError:
                LOGGER.warning("Provided date format is not supported!")
                return False
            except Exception:
                LOGGER.warning("Unhandled exception is occured!")
                return False
            return True

        LOGGER.warning("Provided date format is not supported!")
        return False
