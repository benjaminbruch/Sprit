import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
#from sprit.resources.credentials import Credentials


class FuelPriceAnalyzer:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def connect_to_hist_database(self):   
        """
        Diese Funktion Stellen Sie eine Verbindung zur historischen Datenbank her.
        Wenn eine Verbindung zur Datenbank möglich ist, dann wird ein " True"-Wert zurückgegeben, andernfalls ein "False"-Wert und eine Fehlermeldung angezeigt.
        """     
              
        try:
            self.conn = sqlite3.connect(self.db_path)
            
        except sqlite3.OperationalError as e:
            print("Verbindung zur Datenbank nicht möglich:", e)
            return False
        return True



    def close_connection(self):       
        """
        Diese Funktion wird verwendet, um die Verbindung zur Datenbank zu beenden.
        """
        
        if self.conn:
            self.conn.close()



    def retrieve_data(self, station_uuid):
        """
        Diese Funktion wird verwendet, um die Daten der ausgewählten Tankstelle abzurufen.
        Dabei werden die Daten über die Pandas-Funktion "read_sql_query()" eingelesen und in einem Padas-DataFrame gespeichert und zurückgegeben.
           
        Parameters: 
            - station_uuid (str): Eindeutige Tankstellen ID
                
        Returns:
            - df (Pandas.DataFrame): Pandas-DataFrame der ausgewählten Tankstelle
        """
        
        self.station_uuid = station_uuid 

        #Wenn die Verbindung zur Datenbank nicht möglich, dann gibt eine Fehlermeldung aus.
        if not self.conn:
            print("Datenbankverbindung fehlt.")
            return None
        
        #Wenn eine Verbindung möglich ist, rufen Sie die Daten aus der Datenbank ab..
        self.query = f"SELECT * FROM prices WHERE station_uuid = '{self.station_uuid}'" #SQL Query für die ausgewählte Tankstelle.
        
        df = pd.read_sql_query(self.query, self.conn) #Pandas-Dataframe
        #print(f'Mein Dataframe: \n  {df}')
                
        return df
    

    def process_data(self, df, fuel_type):
        
        """
        Diese Funktion dient der Analyse der Daten aus der Datenbank/Pandas.DataFrame.
        Sie erstellt einen neuen zweidimensionalen Datenwürfel, der die tägliche Durchschnittspreisentwicklung enthält.   
       
        Parameters:  
            - df (Pandas.Dataframe): DataFrame der ausgewählten Tankstelle
            
                 Examples:
            
                    Dates       |       Prices
                    
                    2023-12-01  |       1.6847
                    
                    2023-12-02  |       1.7102
                    
                    2023-12-XX  |       1.XXXX
                    
                    2023-12-10  |       1.7054
                    
            - fuel_type (str): Kraftstoffsart
                
        Returns:
            - dates, prices (Tupel): Datum und Preise für die Datenvisualisierung

        """
         
        self.fuel_type = fuel_type
        self.df = df
                
        self.df['date'] = pd.to_datetime(self.df['date']) #Das Feld "date" enthält mehrere Zeitstämpel. Diese werden zum einfachen Datum konvertiert. 
        dates = self.df.groupby(self.df['date'].dt.date)[self.fuel_type].mean().index # Eindeutiges Datum 
        prices = self.df.groupby(self.df['date'].dt.date)[self.fuel_type].mean() #Preis
        
        return dates, prices
        
    
    def calc_avg_price(self, prices):
        """
        Diese Funktion wird verwendet, um die Durchschnittspreis (MEDIAN) der letzten 7 Tage mit Numpy zu ermitteln. 
                   
        Parameters: 
            - prices (Pandas.DataFrame): DataFrame mit den Preisen von der ausgewählten Tankstelle
                
        Returns:
            - avg_price (float): Durchschnittspreis (MEDIAN) der letzten 7 Tage
        """
        
        self.price_list = []
        self.avg_price_list = []                      
        self.prices = prices
        avg_price = None  
        
        
       #Preise in einer Preis-Liste speichern 
        for price in self.prices:
            #print(type(price))
            self.price_list.append(format(price, '.2f'))
        #print('Aktuelle Preisliste = ', price_list)
        
        #Eine neue Liste "avg_price_list" mit den Durchschnittspreisen der letzten 7 Tage erstellen.        
        if len(self.price_list) >= 8:
            self.avg_price_list = self.price_list[-8:]     # Die letzten 8 Elemente durch Slicing ermitteln
           
            for i in range(len(self.avg_price_list)):
               self.avg_price_list[i] = float(self.avg_price_list[i]) #Einzelne List-Objekt in Float konvertieren
            
            self.avg_price_list.pop() #Letze List-Objekt entfernen, damit nur die Durchschnittspreise der letzten 7 Tage, aktuelles Datum ausgenommen, berücksichtigt werden.
                
        #  7Tagedurchschnittspreis mit Numpy berechnen
        avg_price = float(np.median(self.avg_price_list)) 
      
        return avg_price
    
    
    def calc_todays_price(self, prices):
        """
        Diese Funktion wird verwendet, um letzter/aktueller Preis zu ermitteln. 
                   
        Parameters: 
            - prices (Pandas.DataFrame): DataFrame mit den Preisen von der ausgewählten Tankstelle
                
        Returns:
            - todays_price (float): #Letzter bzw. aktueller Preis
        """
        
        self.price_list = []        
        self.prices = prices
        
        todays_price = None

        #Preise in einer neuen Preisliste "price_list" speichern 
        for price in self.prices:
            #print(type(price))
            self.price_list.append(format(price, '.2f'))
        #print('Aktuelle Preisliste = ', price_list)
        
        #Letzter bzw. aktueller Preis als Tagespreis speichern 
        todays_price = float(self.price_list[-1]) 
            
        return todays_price    
       
          
    def suggest_result(self, avg_price, todays_price):
        """
        Diese Funktion wird verwendet, um ein Vergleich zwischen Durchschnittspreis und aktueller Preis zu vergleichen und anschließend eine Empfehlung zu geben. 
                   
        Parameters: 
            - avg_price (float): Durchschnittspreis (MEDIAN) der letzten 7 Tage
            - todays_price (float): #Letzter bzw. aktueller Preis
                
        Returns:
            - suggestion (str): Empfehlung '👍' #'Guter Zeitpunkt zum Tanken!' bzw. '👎' #'Schlechter Zeitpunkt zum Tanken!'
        """
        
        suggestion = None
        self.avg_price = avg_price
        self.todays_price = todays_price
        
        self.good_news = '👍' #'Guter Zeitpunkt zum Tanken!'
        self.bad_news =  '👎' #'Schlechter Zeitpunkt zum Tanken!'
          
        if self.todays_price <= self.avg_price:
            suggestion  = self.good_news
        else:
            suggestion = self.bad_news
            
        return suggestion       
    
    def visualize_data(self, dates, prices, fuel_type, frame):
       
        """
        Erzeugt und zeigt ein Balkendiagramm der Kraftstoffpreise an.
        
        Parameters:
            - dates (Tupel): Datum (eindeutig)
            - prices (Tupel): Kraffstoffpreise (Median)       

        Returns:
            - ax (matplotlib.axes.Axes): Das erstellte Axes-Objekt
        """
        
        self.dates = dates
        self.prices = prices
        self.fuel_type = fuel_type
        self.frame = frame
               
        fig, ax = plt.subplots()#figsize =(width, heigh)

        #Balkendiagramm erstellen
        ax.bar(self.dates, self.prices, width=0.5, align='center', edgecolor='black')
        
        #AVG Kraftstoffspreis im Diagramm abbilden
        for i, price in zip(self.dates, self.prices):
            ax.text(i, price + 0.00, f'{price:.2f}', ha='center', va='top', rotation=90, color = 'white')

        ax.set_ylabel(f'Preis in EUR')
        ax.set_title(f'Preisentwicklung - Kraftstoff: {self.fuel_type.upper()}')
        #ax.set_xticklabels(dates, rotation=90) #fontsize = 5
        ax.set_xticks = True
        
        # FigureCanvasTkAgg erstellen und in das Frame einbinden
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            
############################################################################################

# Usage Example:
db_path =  '/Users/Janjira Boonkhamsaen/Desktop/tk_hist.db'#TODO #Credentials.sqlite_db
station_uuid = '005056ba-7cb6-1ed2-bceb-aab58f050d43' #TODO #Dynamisch anpassen!!! get from selection 
fuel_type = 'diesel' #TODO #Dynamisch anpassen!!! get from selection 

fuel_analyzer = FuelPriceAnalyzer(db_path)

if fuel_analyzer.connect_to_hist_database():
    data_frame = fuel_analyzer.retrieve_data(station_uuid)
    #print(data_frame)

    if data_frame is not None: 
        dates, prices = fuel_analyzer.process_data(data_frame, fuel_type)
        #print(dates, prices)
        
        avg_price = fuel_analyzer.calc_avg_price(prices)
        todays_price = fuel_analyzer.calc_todays_price(prices)
        suggestion = fuel_analyzer.suggest_result(avg_price, todays_price)        
     
    fuel_analyzer.close_connection()
   
############################################################################################

#GUI mit TKINTER 
root = tk.Tk()

# Styling
s = ttk.Style()
s.configure('mainFrame.TFrame', background = '#3A3845')
s.configure('mainFrame.TLabel',
            background = '#3A3845',
            font = ('Helvetica',30),
            foreground = 'white',
            padding = (15,6,15,6)
            )
            
s.configure('currentPriceFrame.TFrame', background = '#3A3845')
s.configure('avgPriceFrame.TFrame', background = '#3A3845')
s.configure('suggestionFrame.TFrame', background = '#3A3845')

s.configure('kpiLabel.TLabel',
            background='#3A3845',
            font=('Helvetica', 12),
            foreground='white',
            padding=(0, 0, 0, 0)
            )

s.configure('valueLabel.TLabel',
            background='#3A3845',
            font=('Helvetica', 24),
            foreground='white',
            padding=(0, 0, 0, 0)
            )



s.configure('chartFrame.TFrame', background = '#3A3845')


mf_width = 1200
mf_height = 80

pf_width = 380
pf_height = 150

cf_width = 1200
cf_height = 400


# Widget
# Darstellung Tankstelle
selected_station = 'JET, Provinzialstr. 99, 44388 Dortmund' #TODO #Dynamisch anpassen!!! get from selection 
mainFrame = ttk.Frame(root, width= mf_width, height= mf_height, style= 'mainFrame.TFrame')
mainFrame.grid(padx= 10, pady= 5, columnspan=3)
mainLabel = ttk.Label(root, text= selected_station, style='mainFrame.TLabel')
mainLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Darstellung Aktueller Preis
current_price = todays_price
currentPriceFrame = ttk.Frame(root, width=pf_width, height=pf_height, style='currentPriceFrame.TFrame')
currentPriceFrame.grid(padx=10, pady=5, row=1, column=0, sticky='NSEW')
currentPriceLabel = ttk.Label(currentPriceFrame, text='Aktueller Preis', style='kpiLabel.TLabel')
currentPriceLabel.grid(row=0, column=0, columnspan=2, pady=5, sticky='n')
currentPriceValue = ttk.Label(currentPriceFrame, text=f'{current_price:.2f} EUR', style='valueLabel.TLabel')
currentPriceValue.grid(row=1, column=0, columnspan=2, pady=5, sticky='n')


# Darstellung Durchschnittspreis 
avg_price_cur = avg_price
avgPriceFrame = ttk.Frame(root, width=pf_width, height=pf_height, style='avgPriceFrame.TFrame')
avgPriceFrame.grid(padx=10, pady=5, row=1, column=1, sticky='NSEW')
avgPriceLabel = ttk.Label(avgPriceFrame, text='AVG Preis', style='kpiLabel.TLabel')
avgPriceLabel.grid(row=0, column=0, columnspan=2, pady=5, sticky='n')
avgPriceValue = ttk.Label(avgPriceFrame, text=f'{avg_price_cur:.2f} EUR', style='valueLabel.TLabel')
avgPriceValue.grid(row=1, column=0, columnspan=2, pady=5, sticky='n')


# Darstellung Empfehlung 
suggest_cur = suggestion
suggestionFrame = ttk.Frame(root, width=pf_width, height=pf_height, style='suggestionFrame.TFrame')
suggestionFrame.grid(padx=10, pady=5, row=1, column=2, sticky='NSEW')
suggestionLabel = ttk.Label(suggestionFrame, text='Empfehlung', style='kpiLabel.TLabel')
suggestionLabel.grid(row=0, column=0, columnspan=2, pady=5)
suggestionValue = ttk.Label(suggestionFrame, text=f'{suggest_cur}', style='valueLabel.TLabel')
suggestionValue.grid(row=1, column=0, columnspan=2, pady=5)

#Balkendiagramm in ChartFrame einbinden
chartFrame = ttk.Frame(root, width= cf_width, height= cf_height, style= 'chartFrame.TFrame')
chartFrame.grid(padx= 10, pady= 5, columnspan=3, sticky='NSEW')
fuel_analyzer.visualize_data(dates, prices, fuel_type, chartFrame)



# Grid Config
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
mainFrame.columnconfigure(0, weight=1)

currentPriceFrame.columnconfigure(0, weight=1)
currentPriceFrame.columnconfigure(1, weight=1)

avgPriceFrame.columnconfigure(0, weight=1)
avgPriceFrame.columnconfigure(1, weight=1)

suggestionFrame.columnconfigure(0, weight=1)
suggestionFrame.columnconfigure(1, weight=1)

chartFrame.columnconfigure(0, weight=1)


root.resizable(width= False, height= False)
root.mainloop()