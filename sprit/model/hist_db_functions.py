import sqlite3
from datetime import datetime
from resources.credentials import Credentials

sqlite_db = '/Users/joerg/Programming/AKI/KI Programmierung/Sprit/sprit/data/tk_hist.db'

print(Credentials.sqlite_db)

class hist_data:


    def print_dict(self, d, indent=0):
        for key, value in d.items():
            if isinstance(value, dict):
                print(' ' * indent + str(key) + ': ')
                self.print_dict(value, indent + 4)
            else:
                print(' ' * indent + str(key) + ': ' + str(value))


    def get_station(self, uuid: str):
        
        # Verbindung zur SQLite-Datenbank herstellen
        conn = sqlite3.connect(Credentials.sqlite_db) 
        cursor = conn.cursor()

        query = """SELECT uuid, name, brand, street, house_number, post_code, city from stations where uuid = ?"""
        cursor.execute(query,(uuid,))

        # Ergebnisse der Abfrage abrufen
        results = cursor.fetchall()

        data_dict = {}
        for row in results:
            data_dict[row[0]] = {'uuid': row[0], 'name': row[1], 'brand': row[2], 'street': row[3], 'house_number': row[4], 'post_code': row[5], 'city': row[6]}
            #print(data_dict[row[0]])
       
        self.print_dict(data_dict)

        # Verbindung zur Datenbank schließen
        conn.close()
        return data_dict
    
    def get_date_prices(self, datum: str):
        
        # Verbindung zur SQLite-Datenbank herstellen
        conn = sqlite3.connect(Credentials.sqlite_db) 
        cursor = conn.cursor()

        query = """SELECT date, time, station_uuid, diesel, e5, e10 from prices where date = ?"""
        cursor.execute(query,(datum,))

        # Ergebnisse der Abfrage abrufen
        results = cursor.fetchall()

        data_dict = {}
        for row in results:
            #data_dict[row[0]] = {'date': row[0], 'time': row[1], 'uuid': row[2], 'diesel': row[3], 'e5': row[4], 'e10': row[5]}
            data_dict[row] = {'date': row[0], 'time': row[1], 'uuid': row[2], 'diesel': row[3], 'e5': row[4], 'e10': row[5]}
            #print(data_dict[row[0]])
        # Verbindung zur Datenbank schließen

        #self.print_dict(data_dict)
        conn.close()

        return data_dict
    