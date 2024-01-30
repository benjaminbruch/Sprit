import sqlite3
from sprit.resources.credentials import Credentials
# This file is first iteration and was base for import_hist_data.py

# Database file name
sqlite_db = 'tk_hist.db'


class HistData:
    """
    Class for handling historical data from a SQLite database.
    """

    def print_dict(self, d, indent=0):
        """
        Recursive function to print a dictionary.

        Args:
            d (dict): The dictionary to print.
            indent (int, optional): The current indentation level. Defaults to 0.
        """
        for key, value in d.items():
            if isinstance(value, dict):
                print(' ' * indent + str(key) + ': ')
                self.print_dict(value, indent + 4)
            else:
                print(' ' * indent + str(key) + ': ' + str(value))

    def get_station(self, uuid: str):
        """
        Fetches station data from the database using the provided UUID.

        Args:
            uuid (str): The UUID of the station.

        Returns:
            dict: A dictionary containing the station data.
        """

        # Establish connection to the SQLite database
        conn = sqlite3.connect(Credentials.sqlite_db)
        cursor = conn.cursor()

        # SQL query to fetch station data
        query = """SELECT uuid, name, brand, street, house_number, post_code, city from stations where uuid = ?"""
        cursor.execute(query, (uuid,))

        # Fetch the results of the query
        results = cursor.fetchall()

        # Create a dictionary from the results
        data_dict = {}
        for row in results:
            data_dict[row[0]] = {'uuid': row[0], 'name': row[1], 'brand': row[2], 'street': row[3],
                                 'house_number': row[4], 'post_code': row[5], 'city': row[6]}

        # Print the dictionary
        self.print_dict(data_dict)

        # Close the connection to the database
        conn.close()
        return data_dict

    def get_date_prices(self, datum: str):
        """
        Fetches price data from the database for the provided date.

        Args:
            datum (str): The date to fetch data for.

        Returns:
            dict: A dictionary containing the price data.
        """

        # Establish connection to the SQLite database
        conn = sqlite3.connect(Credentials.sqlite_db)
        cursor = conn.cursor()

        # SQL query to fetch price data
        query = """SELECT date, time, station_uuid, diesel, e5, e10 from prices where date = ?"""
        cursor.execute(query, (datum,))

        # Fetch the results of the query
        results = cursor.fetchall()

        # Create a dictionary from the results
        data_dict = {}
        for row in results:
            data_dict[row] = {'date': row[0], 'time': row[1], 'uuid': row[2], 'diesel': row[3], 'e5': row[4],
                              'e10': row[5]}

        # Close the connection to the database
        conn.close()
        return data_dict