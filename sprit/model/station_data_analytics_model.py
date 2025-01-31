import sqlite3
import pandas as pd
import numpy as np
from PIL import Image
from sprit.resources import helper


class StationDataAnalyticsModel:
    def __init__(self):
        # Combine the base directory with the relative path to the database file
        db_path = helper.find_data_file("tk_hist.db")

        self.db_path = db_path
        self.conn = None

        self.connect_to_hist_database()

        # Set initial prices and dates for demonstration purposes
        self.prices = np.random.uniform(1.00, 1.00, 8)
        # Set the start and end dates
        start_date = pd.Timestamp.today() - pd.DateOffset(days=7)
        end_date = pd.Timestamp.today()
        # Generate the date range
        self.dates = pd.date_range(start=start_date, end=end_date)
        self.average_price = "1.00"
        self.is_recommended = True

        # Join the base directory with the relative path to the icons
        self.thumb_up_path = helper.find_data_file("thumb_up_green.png")
        self.thumb_down_path = helper.find_data_file("thumb_down_red.png")
        self.recommendation_icon = Image.open(self.thumb_up_path)

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
        query = f"SELECT DISTINCT date, {fuel_type} FROM prices INNER JOIN stations ON prices.station_id = stations.id WHERE stations.station_uuid = '{station_uuid}'"
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
        # Convert "date" field to datetime format and sort by date in descending order
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date', ascending=False)

        # Group by date and get the mean fuel price, then get the last 7 records
        grouped = df.groupby(df['date'].dt.date)[fuel_type].mean()
        dates = grouped.index[-7:]
        prices = grouped.values[-7:]

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

    def suggest_result(self, prices, current_price):
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


        suggestion = current_price <= avg_price if current_price is not None and avg_price is not None else None

        return suggestion

    def get_recommendation_icon(self):
        """
        Returns the recommendation icon.
        """
        if self.is_recommended:
            self.recommendation_icon = Image.open(self.thumb_up_path)
        else:
            self.recommendation_icon = Image.open(self.thumb_down_path)
        return self.recommendation_icon

    def update_data(self, station_uuid, fuel_type, current_price):
        """
        Updates the data for the selected fuel station.
        """
        df = self.retrieve_data(station_uuid, fuel_type)
        self.dates, self.prices = self.process_data(df, fuel_type)
        self.average_price = str(self.calc_avg_price(self.prices))
        self.is_recommended = self.suggest_result(self.prices, current_price)
