'''
This module includes the DataProcessor class that includes
the necessary data analysis functions to analyze data
'''
import os
import logging
import pandas as pd

logging.basicConfig(format='%(asctime)s - [%(levelname)s] %(funcName)s - %(message)s',
                    level='DEBUG')
LOGGER = logging.getLogger(__name__)


class DataProcessor():
    '''
    This class includes the required data processing functions to process APPLE's stock data.
    '''
    def __init__(self) -> None:
        # read the related csv file
        self.df: pd.DataFrame = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "AAPL.csv"))
        LOGGER.info("APPL.csv data source is initialized")

    def get_latest_day(self) -> dict:
        '''
        Returns the latest stock data as json inside of a list format
        example output: [{'Date': '2021-06-22', 'Open': 132.130005, ...}]
        '''
        LOGGER.info(f"Source data shape: {self.df.shape}")

        # get the latest entry
        df = self.df.iloc[-1:]

        LOGGER.info(f"Processed data shape: {df.shape}")
        return df.to_dict('records')

    def get_latest_day_average(self) -> dict:
        '''
        Returns the latest stock data's average value as json inside of a list format
        example output:
        [
            {'Date': '2021-06-22', 'Average': 132.8499985}
        ]
        '''
        LOGGER.info(f"Source data shape: {self.df.shape}")

        # get the latest entry
        df = self.df.iloc[-1:]

        # create a new column called 'Average' and set the mean of 'High' and 'Low'
        df = df.assign(Average=df.loc[:, ["High", "Low"]].mean(axis=1))
        LOGGER.info(f"Data shape before the dropping columns: {df.shape}")

        # drop the not needed columns
        df = df.drop(['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1)
        LOGGER.info(f"Processed data shape: {df.shape}")
        return df.to_dict('records')

    def get_historical_data(self, date_from: str, date_to: str) -> dict:
        '''
        Returns the historical stock data as json inside of a list format
        example output for the boundary ["2021-05-19", "2021-05-28"]:
        [
            {'Date': '2021-05-19', 'Open': 123.160004, ..},
            ...
            {'Date': '2021-05-28', 'Open': 125.57, ..}
        ]
        '''
        LOGGER.info(f"Source data shape: {self.df.shape}")
        LOGGER.info(f"Data will be processed from {date_from} to {date_to}")

        # select the rows starting from 'date_from' value to 'date_to' value with including boundaries
        try:
            df = self.df.iloc[int(self.df[self.df['Date'].str.match(date_from)].index[0]):int(self.df[self.df['Date'].str.match(date_to)].index[0]) + 1]
            LOGGER.info(f"Processed data shape: {df.shape}")
            return df.to_dict('records')
        except IndexError:
            return {"error": "please select a different date boundaries that are not starting and ending on a weekend day"}

    def get_historical_data_average(self, date_from: str, date_to: str) -> dict:
        '''
        Returns the historical stock data's average as json inside of a list format
        example output for the boundary ["2021-05-19", "2021-05-28"]:
        [
            {'Date': '2021-05-19', 'Average': 123.8899995},
            ...
            {'Date': '2021-05-28', 'Average': 125.175003}
        ]
        '''
        # select the rows starting from 'date_from' value to 'date_to' value with including boundaries
        try:
            df = self.df.iloc[int(self.df[self.df['Date'].str.match(date_from)].index[0]):int(self.df[self.df['Date'].str.match(date_to)].index[0]) + 1]
        except IndexError:
            return {"error": "please select a different date boundaries that are not starting and ending on a weekend day"}

        # create a new column called 'Average' and set the mean of 'High' and 'Low'
        df = df.assign(Average=df.loc[:, ["High", "Low"]].mean(axis=1))

        # drop the not needed columns
        df = df.drop(['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1)
        return df.to_dict('records')

    def get_average_highest(self):
        '''
        Returns the stock data that has the highest average value in a day as json inside of a list format
        example output:
        [
            {'Date': '2021-01-26', 'High': 144.300003, 'Low': 141.369995, ..., 'Average': 142.83499899999998}
        ]
        '''
        LOGGER.info(f"Source data shape: {self.df.shape}")
        # create a new column called 'Average' and set the mean of 'High' and 'Low'
        df = self.df.assign(Average=self.df.loc[:, ["High", "Low"]].mean(axis=1))

        # getting the row with the highest daily value in filtered rows
        df: pd.DataFrame = df[df["Average"] == df["Average"].max()]
        LOGGER.info(f"Processed data shape: {df.shape}")
        return df.to_dict('records')

    def get_average_lowest(self):
        '''
        Returns the stock data that has the lowest average value in a day as json inside of a list format
        example output:
        [
            {'Date': '1982-07-08', 'High': 0.049665, 'Low': 0.049107, ..., 'Average': 0.049386}
        ]
        '''
        LOGGER.info(f"Source data shape: {self.df.shape}")
        # create a new column called 'Average' and set the mean of 'High' and 'Low'
        df = self.df.assign(Average=self.df.loc[:, ["High", "Low"]].mean(axis=1))

        # getting the row with the highest daily value in filtered rows
        df: pd.DataFrame = df[df["Average"] == df["Average"].min()]
        LOGGER.info(f"Processed data shape: {df.shape}")
        return df.to_dict('records')
