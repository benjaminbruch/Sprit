import sqlite3
import pandas as pd
import numpy as np
import os
from sprit.resources import helper


class StationDataAnalyticsModel:
    def __init__(self):
        # Determine the directory of the currently running script
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Combine the base directory with the relative path to the database file
        db_path = helper.find_data_file("tk_hist.db", os.path.join(base_dir, "../data/"))

        self.db_path = db_path
        self.conn = None

        self.connect_to_hist_database()

        # Set initial prices and dates for demonstration purposes
        self.prices = np.random.uniform(1.00, 1.00, 15)
        # Set the start and end dates
        start_date = pd.Timestamp.today() - pd.DateOffset(days=14)
        end_date = pd.Timestamp.today()
        # Generate the date range
        self.dates = pd.date_range(start=start_date, end=end_date)
        self.average_price = "1.00"
        self.is_recommended = True

    def connect_to_hist_database(self):
        """
        Establish a connection to the historical database.
        Returns True if the connection is successful, otherwise False with an error message.
        """
        try:
            self.conn = sqlite3.connect(self.db_path)
        except sqlite3.OperationalError as e:
            print("Unable to connect to the database:", e)
            return False
        return True

    def close_connection(self):
        """
        Closes the connection to the database.
        """
        if self.conn:
            self.conn.close()

    def retrieve_data(self, station_uuid, fuel_type):
        """
        Retrieves data for the specified fuel station.
        The data is read using the Pandas function "read_sql_query()" and stored in a Pandas DataFrame.

        Parameters:
            - station_uuid (str): Unique fuel station ID

        Returns:
            - df (Pandas.DataFrame): DataFrame for the selected fuel station
        """
        if not self.conn:
            print("Database connection is missing.")
            return None

        # SQL query to get date & price for the selected station.
        query = f"SELECT date, {fuel_type} FROM prices INNER JOIN stations ON prices.station_id = stations.id WHERE stations.station_uuid = '{station_uuid}'"
        df = pd.read_sql_query(query, self.conn)  # Create the DataFrame

        return df

    def process_data(self, df, fuel_type):
        """
        Analyzes data from the database/Pandas DataFrame.
        Creates a new two-dimensional cube containing the daily average price trend.

        Parameters:
            - df (Pandas.DataFrame): DataFrame of the selected fuel station
            - fuel_type (str): Type of fuel

        Returns:
            - (dates, prices): Tuple containing dates and prices for data visualization
        """
        df['date'] = pd.to_datetime(df['date'])  # Convert "date" field to simple date format
        dates = df.groupby(df['date'].dt.date)[fuel_type].mean().index  # Get unique dates
        prices = df.groupby(df['date'].dt.date)[fuel_type].mean()

        return dates, prices

    def calc_avg_price(self, prices):
        """
        Calculates the average price from a list of prices.

        Parameters:
            - prices (list): List of prices

        Returns:
            - avg_price (float): The average price
        """
        price_list = [format(price, '.2f') for price in prices]
        avg_price_list = price_list[-8:] if len(price_list) >= 8 else price_list # Use the last 8 elements
        avg_price_list = [float(price) for price in avg_price_list[:-1]] # Convert to float and remove the last item

        avg_price = float(np.median(avg_price_list)) if avg_price_list else None
        avg_price = format(avg_price, '.2f')

        return avg_price

    def calc_todays_price(self, prices):
        """
        Calculates today's price from a list of prices.

        Parameters:
            - prices (list): List of prices

        Returns:
            - todays_price (float): Today's price
        """
        price_list = [format(price, '.2f') for price in prices]
        todays_price = float(price_list[-1]) if price_list else None

        return todays_price

    def suggest_result(self, prices):
        """
        Suggests whether to recommend based on the comparison of today's price with the average price.

        Parameters:
            - prices (list): List of prices

        Returns:
            - suggestion (bool): Recommendation based on price comparison
        """
        price_list = [format(price, '.2f') for price in prices]
        avg_price_list = price_list[-8:] if len(price_list) >= 8 else price_list
        avg_price_list = [float(price) for price in avg_price_list[:-1]]
        avg_price = float(np.median(avg_price_list)) if avg_price_list else None

        todays_price = float(price_list[-1]) if price_list else None
        suggestion = todays_price <= avg_price if todays_price is not None and avg_price is not None else None

        return suggestion

    def update_data(self, station_uuid, fuel_type):
        df = self.retrieve_data(station_uuid, fuel_type)
        self.dates, self.prices = self.process_data(df, fuel_type)
        self.average_price = str(self.calc_avg_price(self.prices))
        self.is_recommended = self.suggest_result(self.prices)