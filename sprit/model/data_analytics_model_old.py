import sqlite3
import pandas as pd
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


# This class is first iteration and was base for station_data_analytics_model.py and station_analytics_view.py
class FuelPriceAnalyzer:
    def __init__(self, db_path):
        """
        Initialize the FuelPriceAnalyzer with a database path.

        Args:
            db_path (str): The path to the SQLite database.
        """
        self.db_path = db_path
        self.conn = None

    def connect_to_hist_database(self):
        """
        Establish a connection to the historical database.
        If a connection to the database is possible, a "True" value is returned, otherwise a "False" value and an error message is displayed.
        """
        try:
            self.conn = sqlite3.connect(self.db_path)
        except sqlite3.OperationalError as e:
            print("Unable to connect to the database:", e)
            return False
        return True

    def close_connection(self):
        """
        This function is used to close the connection to the database.
        """
        if self.conn:
            self.conn.close()

    def retrieve_data(self, station_uuid):
        """
        This function is used to retrieve the data of the selected gas station.
        The data is read in via the Pandas function "read_sql_query()" and stored in a Pandas DataFrame and returned.

        Args:
            station_uuid (str): Unique gas station ID

        Returns:
            df (Pandas.DataFrame): Pandas DataFrame of the selected gas station
        """
        self.station_uuid = station_uuid

        # If the connection to the database is not possible, then an error message is output.
        if not self.conn:
            print("Database connection is missing.")
            return None

        # If a connection is possible, retrieve the data from the database.
        self.query = f"SELECT * FROM prices WHERE station_uuid = '{self.station_uuid}'"  # SQL Query for the selected gas station.

        df = pd.read_sql_query(self.query, self.conn)  # Pandas DataFrame
        return df

    def process_data(self, df, fuel_type):
        """
        This function is used to analyze the data from the database/Pandas DataFrame.
        It creates a new two-dimensional data cube that contains the daily average price development.

        Args:
            df (Pandas.Dataframe): DataFrame of the selected gas station
            fuel_type (str): Type of fuel

        Returns:
            dates, prices (tuple): Date and prices for data visualization
        """
        self.fuel_type = fuel_type
        self.df = df

        self.df['date'] = pd.to_datetime(
            self.df['date'])  # The "date" field contains several timestamps. These are converted to a simple date.
        dates = self.df.groupby(self.df['date'].dt.date)[self.fuel_type].mean().index  # Unique date
        prices = self.df.groupby(self.df['date'].dt.date)[self.fuel_type].mean()  # Price

        return dates, prices

    def calc_avg_price(self, prices):
        """
        This function is used to calculate the average price (MEDIAN) of the last 7 days with Numpy.

        Args:
            prices (Pandas.DataFrame): DataFrame with the prices from the selected gas station

        Returns:
            avg_price (float): Average price (MEDIAN) of the last 7 days
        """
        self.price_list = []
        self.avg_price_list = []
        self.prices = prices
        avg_price = None

        # Store prices in a price list
        for price in self.prices:
            self.price_list.append(format(price, '.2f'))

        # Create a new list "avg_price_list" with the average prices of the last 7 days.
        if len(self.price_list) >= 8:
            self.avg_price_list = self.price_list[-8:]  # Determine the last 8 elements by slicing

            for i in range(len(self.avg_price_list)):
                self.avg_price_list[i] = float(self.avg_price_list[i])  # Convert individual list object to float

            self.avg_price_list.pop()  # Remove last list object, so that only the average prices of the last 7 days, excluding the current date, are considered.

        # Calculate 7-day average price with Numpy
        avg_price = float(np.median(self.avg_price_list))

        return avg_price

    def calc_todays_price(self, prices):
        """
        This function is used to determine the last/current price.

        Args:
            prices (Pandas.DataFrame): DataFrame with the prices from the selected gas station

        Returns:
            todays_price (float): Last or current price
        """
        self.price_list = []
        self.prices = prices

        todays_price = None

        # Store prices in a new price list "price_list"
        for price in self.prices:
            self.price_list.append(format(price, '.2f'))

        # Save the last or current price as the daily price
        todays_price = float(self.price_list[-1])

        return todays_price

    def suggest_result(self, avg_price, todays_price):
        """
        This function is used to compare the average price and the current price and then give a recommendation.

        Args:
            avg_price (float): Average price (MEDIAN) of the last 7 days
            todays_price (float): Last or current price

        Returns:
            suggestion (str): Recommendation '👍' #'Good time to refuel!' or '👎' #'Bad time to refuel!'
        """
        suggestion = None
        self.avg_price = avg_price
        self.todays_price = todays_price

        self.good_news = '👍'  # 'Good time to refuel!'
        self.bad_news = '👎'  # 'Bad time to refuel!'

        if self.todays_price <= self.avg_price:
            suggestion = self.good_news
        else:
            suggestion = self.bad_news

        return suggestion

    def visualize_data(self, dates, prices, fuel_type, frame):
        """
        Creates and displays a bar chart of fuel prices.

        Args:
            dates (tuple): Date (unique)
            prices (tuple): Fuel prices (Median)
            fuel_type (str): Type of fuel
            frame (tkinter.Frame): The frame to display the chart in

        Returns:
            ax (matplotlib.axes.Axes): The created Axes object
        """
        self.dates = dates
        self.prices = prices
        self.fuel_type = fuel_type
        self.frame = frame

        fig, ax = plt.subplots()

        # Create bar chart
        ax.bar(self.dates, self.prices, width=0.5, align='center', edgecolor='black')

        # Display AVG fuel price in the chart
        for i, price in zip(self.dates, self.prices):
            ax.text(i, price + 0.00, f'{price:.2f}', ha='center', va='top', rotation=90, color='white')

        ax.set_ylabel(f'Price in EUR')
        ax.set_title(f'Price development - Fuel: {self.fuel_type.upper()}')
        ax.set_xticks = True

        # Create FigureCanvasTkAgg and integrate it into the frame
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)