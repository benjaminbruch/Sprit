import csv
import os
import sqlite3

# Path to the CSV file and SQLite database
prices_path = "csv/"
sqlite_db = "tk_hist.db"


# Function to create an SQLite database and table
def create_tables():
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute('DROP TABLE IF EXISTS prices')

    cursor.execute('''CREATE TABLE prices (
                        date TEXT NOT NULL,
                        time TEXT NOT NULL,
                        station_uuid TEXT NOT NULL,
                        diesel REAL,
                        e5 REAL,
                        e10 REAL,
                        dieselchange INTEGER,
                        e5change INTEGER,
                        e10change INTEGER
                    )''')

    conn.commit()
    conn.close()


# Function to insert data from the CSV file into the SQLite database
def insert_data_from_csv():
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    for prices_file in os.listdir(prices_path):
        # Check if the file is a CSV file
        _, file_extension = os.path.splitext(prices_file)
        if file_extension == '.csv':
            # Join the directory path with the file name
            full_file_path = os.path.join(prices_path, prices_file)
            with open(full_file_path, 'r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Skip the header
                for row in csv_reader:
                    inp = row
                    # Separate date and time from csv input
                    dat = row[0][:10]
                    tim = row[0][11:19]
                    # Write date and time into separate fields in the database
                    del row[0]
                    row.insert(0, tim)
                    row.insert(0, dat)

                    cursor.execute(
                        'INSERT INTO prices (date, time, station_uuid, diesel, e5, e10, dieselchange, e5change, e10change) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                        row)

    conn.commit()
    conn.close()


# Main function to run the program
def main():
    create_tables()
    insert_data_from_csv()
    print("Data from CSV files successfully inserted into the SQLite3 database!")


if __name__ == "__main__":
    main()
