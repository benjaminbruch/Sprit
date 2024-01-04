import csv
import sqlite3

# Pfad zur CSV-Datei und SQLite-Datenbank
prices_file = '/Users/joerg/Programming/AKI/KI Programmierung/Sprit/sprit/data/2023-12-01-prices.csv'
stations_file = '/Users/joerg/Programming/AKI/KI Programmierung/Sprit/sprit/data/2023-12-01-stations.csv'
sqlite_db = '/Users/joerg/Programming/AKI/KI Programmierung/Sprit/sprit/data/tk_hist.db'


# Funktion zum Erstellen einer SQLite-Datenbank und Tabelle
def create_tables():
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS prices (
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
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS stations (
                        uuid TEXT NOT NULL UNIQUE,
                        name TEXT,
                        brand TEXT,
                        street TEXT,
                        house_number TEXT,
                        post_code TEXT,
                        city TEXT,
                        lat REAL,
                        long REAL,
                        first_active TEXT,
                        openingtimes TEXT
                    )''')
    
    cursor.execute('''CREATE INDEX IF NOT EXISTS uuid_ind ON stations (uuid ASC)''')
                   
    conn.commit()
    
    conn.close()


# Funktion zum Einfügen von Daten aus der CSV-Datei in die SQLite-Datenbank
def insert_data_from_csv():
    conn = sqlite3.connect(sqlite_db)
    cursor = conn.cursor()

    with open(prices_file, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Überspringe den Header
        for row in csv_reader:
            inp = row
            # Datum und Zeit aus csv-input separieren 
            dat = row[0][:10]
            tim = row[0][11:19]
            # Datum und Zeit in getrennte Felder der Datenbank schreiben
            del row[0]
            row.insert(0, tim)
            row.insert(0, dat)

            cursor.execute('INSERT INTO prices (date, time, station_uuid, diesel, e5, e10, dieselchange, e5change, e10change) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

    conn.commit()

    with open(stations_file, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Überspringe den Header
        for row in csv_reader:
            try:
                cursor.execute('INSERT INTO stations (uuid, name, brand, street, house_number, post_code, city, lat, long, first_active, openingtimes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', row)
            except:
                continue

    conn.commit()

    conn.close()

# Hauptfunktion zum Ausführen des Programms
def main():
    create_tables()
    insert_data_from_csv()
    print("Daten der CSV-Dateien erfolgreich in die SQLite3-Datenbank eingefügt!")

if __name__ == "__main__":
    main()
