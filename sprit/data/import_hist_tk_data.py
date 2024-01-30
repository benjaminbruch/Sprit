import csv
import os
import sqlite3
import sys

from sprit.resources import helper

# Define the path to the CSV file and the SQLite database
prices_path = "csv/"
sqlite_db = helper.find_data_file("tk_hist.db")

#sqlite_db = os.path.dirname(sys.executable)+"/tk_hist.db"
print(sqlite_db)


# Function to create an SQLite database and its tables
def create_tables():
    # Establish a connection to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # If the tables already exist, drop them
    cursor.execute('DROP TABLE IF EXISTS stations')
    cursor.execute('DROP TABLE IF EXISTS prices')

    # Create the 'stations' table
    cursor.execute('''CREATE TABLE stations (
                        id INTEGER PRIMARY KEY,
                        station_uuid TEXT NOT NULL UNIQUE
                   )''')

    # Create the 'prices' table
    cursor.execute('''
                      CREATE TABLE prices (
                        id INTEGER PRIMARY KEY,
                        date TEXT NOT NULL,
                        diesel REAL,
                        e5 REAL,
                        e10 REAL,
                        station_id INTEGER,
                        FOREIGN KEY(station_id) REFERENCES stations(id)
                   )''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


# Function to insert data from the CSV file into the SQLite database
def insert_data_from_csv():
    # Establish a connection to the SQLite database
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Iterate over each file in the specified directory
    for prices_file in os.listdir(prices_path):
        # If the file is a CSV file
        _, file_extension = os.path.splitext(prices_file)
        if file_extension == '.csv':
            # Construct the full path to the file
            full_file_path = os.path.join(prices_path, prices_file)
            # Open the file
            with open(full_file_path, 'r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the header row
                # Iterate over each row in the CSV file
                for row in csv_reader:
                    # Extract the necessary data from the row
                    date, station_uuid, diesel, e5, e10, *_ = row

                    # Check if the station_uuid already exists in the 'stations' table
                    cursor.execute("SELECT id FROM stations WHERE station_uuid = ?", (station_uuid,))
                    result = cursor.fetchone()

                    if result is None:
                        # If the station_uuid does not exist, insert a new row into the 'stations' table
                        cursor.execute("INSERT INTO stations (station_uuid) VALUES (?)", (station_uuid,))
                        station_id = cursor.lastrowid
                    else:
                        # If the station_uuid does exist, get the corresponding station_id
                        station_id = result[0]

                    # Insert a new row into the 'prices' table
                    cursor.execute("INSERT INTO prices (date, diesel, e5, e10, station_id) VALUES (?, ?, ?, ?, ?)",
                                   (date, diesel, e5, e10, station_id))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


# Main function to execute the program
def main():
    # Create the database tables
    create_tables()
    # Insert data from the CSV files into the database
    insert_data_from_csv()
    # Print a success message
    print("Data from CSV files successfully inserted into the SQLite3 database!")


# If this script is being run directly, execute the main function
if __name__ == "__main__":
    main()