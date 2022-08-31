'''
This module includes the DataProcessor class that includes
the necessary data analysis functions to analyze data
'''
import os as _os
import logging as _logging
import typing as _typing

import pandas as _pd

_logging.basicConfig(
    format='%(asctime)s - [%(levelname)s] %(funcName)s - %(message)s',
    level='DEBUG')
LOGGER = _logging.getLogger(__name__)


class DataProcessor():
    '''
    This class includes the required data processing functions to process
    APPLE's stock data.
    '''
    def __init__(self) -> None:
        '''
        Initialize dataframe and create reused columns
        '''
        self.df: _pd.DataFrame = _pd.read_csv(
            _os.path.join(_os.path.dirname(
                _os.path.abspath(__file__)), "data", "AAPL.csv"))

        # create new col. called 'Average' and set the mean of 'High' and 'Low'
        self.df = self.df.assign(
            Average=self.df.loc[:, ["High", "Low"]].mean(axis=1))

        LOGGER.info("APPL.csv data source is initialized")
        LOGGER.info(f"Source data shape: {self.df.shape}")

    def get_latest_day(self) -> _typing.List[dict]:
        '''
        Get the latest day's stock data

        Example output:
        [
            {
                'Date': '2021-06-22',
                'Open': 132.130005,
                ...,
            }
        ]
        '''
        LOGGER.info(f"Source data shape: {self.df.shape}")

        # get the latest entry
        df = self.df.iloc[-1:]

        LOGGER.info(f"Processed data shape: {df.shape}")
        return df.to_dict('records')

    def get_latest_day_average(self) -> _typing.List[dict]:
        '''
        Returns the latest stock data's average value as json inside of
        a list format

        Example output:
        [
            {
                'Date': '2021-06-22',
                'Average': 132.8499985
            }
        ]
        '''
        LOGGER.info(f"Source data shape: {self.df.shape}")

        # get the latest entry
        df = self.df.iloc[-1:]

        # create a col. called 'Average' and set the mean of 'High' and 'Low'
        df = df.assign(Average=df.loc[:, ["High", "Low"]].mean(axis=1))
        LOGGER.info(f"Data shape before the dropping columns: {df.shape}")

        # drop the not needed columns
        df = df.drop(
            ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1)
        LOGGER.info(f"Processed data shape: {df.shape}")
        return df.to_dict('records')

    def select_rows(self, date_from: str, date_to: str) -> _pd.DataFrame:
        '''
        Select rows from 'date_from' to 'date_to' with incl. boundaries

        Args:
            date_from: Start date (YYYY-MM-DD)
            date_to: End date (YYYY-MM-DD)

        Returns:
            Filtered dataframe
        '''
        df = self.df.iloc[int(self.df[self.df['Date'].str.match(
            date_from)].index[0]):int(self.df[self.df['Date'].str.match(
                date_to)].index[0]) + 1]
        LOGGER.info(f"Processed data shape: {df.shape}")
        return df

    def get_historical_data(
            self, date_from: str, date_to: str) -> _typing.List[dict]:
        '''
        Returns the historical stock data as json inside of a list format

        Example output for the boundaries ["2021-05-19", "2021-05-28"]:
        [
            {
                'Date': '2021-05-19',
                'Open': 123.160004,
                ...
            },
            ...
            {
                'Date': '2021-05-28',
                'Open': 125.57,
                ..
            }
        ]
        '''
        res = self.select_rows(date_from, date_to)
        return res.to_dict('records')

    def get_historical_data_average(
            self, date_from: str, date_to: str) -> _typing.List[dict]:
        '''
        Returns the historical stock data's average as json inside of a list
        format

        Example output for the boundaries ["2021-05-19", "2021-05-28"]:
        [
            {
                'Date': '2021-05-19',
                'Average': 123.8899995
            },
            ...
            {
                'Date': '2021-05-28',
                'Average': 125.175003
            }
        ]
        '''
        df = self.select_rows(date_from, date_to)

        # create new col. called 'Average' and set the mean of 'High' and 'Low'
        df = df.assign(Average=df.loc[:, ["High", "Low"]].mean(axis=1))

        # drop the not needed columns
        df = df.drop(
            ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1)
        return df.to_dict('records')

    def get_average_highest(self) -> _typing.List[dict]:
        '''
        Get the stock data that has the highest average value in a day

        Example output:
        [
            {
                'Date': '2021-01-26',
                'High': 144.300003,
                'Low': 141.369995,
                ...,
                'Average': 142.83499899999998
            }
        ]
        '''
        # getting the row with the highest daily value in filtered rows
        df = self.df[self.df["Average"] == self.df["Average"].max()]
        LOGGER.info(f"Processed data shape: {df.shape}")
        return df.to_dict('records')

    def get_average_lowest(self) -> _typing.List[dict]:
        '''
        Get the stock data that has the lowest average value in a day

        Example output:
        [
            {
                'Date': '1982-07-08',
                'High': 0.049665,
                'Low': 0.049107,
                ...,
                'Average': 0.049386
            }
        ]
        '''
        # getting the row with the highest daily value in filtered rows
        df = self.df[self.df["Average"] == self.df["Average"].min()]

        LOGGER.info(f"Processed data shape: {df.shape}")
        return df.to_dict('records')
