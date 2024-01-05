import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


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

        #start = '2023-12-20' #datetime.now().date() - timedelta(days=7)
        #end = '2023-12-26' #datetime.now().date() - timedelta(days=1)
        

        #Wenn die Verbindung zur Datenbank nicht möglich, dann gibt eine Fehlermeldung aus.
        if not self.conn:
            print("Datenbankverbindung fehlt.")
            return None
        
        #Wenn eine Verbindung möglich ist, rufen Sie die Daten aus der Datenbank ab..
        query = f"SELECT * FROM prices WHERE station_uuid = '{station_uuid}'" #SQL Query für die ausgewählte Tankstelle.
        
        df = pd.read_sql_query(query, self.conn) #Pandas-Dataframe
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
            - dates, prices (Tupel): Datum und Preis für die Datenvisualisierung

        """
                
        df['date'] = pd.to_datetime(df['date']) #Das Feld "date" enthält mehrere Zeitstämpel. Diese werden zum einfachen Datum konvertiert. 
        dates = df.groupby(df['date'].dt.date)[fuel_type].mean().index # Eindeutiges Datum ü
        prices = df.groupby(df['date'].dt.date)[fuel_type].mean()
        
        #print(dates, prices)
        
        #dict_from_df = df.to_dict()
        #print(dict_from_df['date'])
        #print(dict_from_df['diesel'])          
        #print(f'TYPE: {type (dates)}')
        #print(f'TYPE: {type (prices)}')


        return dates, prices
        
    
    def calc_avg_price(self, prices):
        
        price_list = []
        avg_price_list = []
        avg_price = None        
        
       #Preise in einer Preis-Liste speichern 
        for price in prices:
            #print(type(price))
            price_list.append(format(price, '.2f'))
        #print('Aktuelle Preisliste = ', price_list)
                
        if len(price_list) >= 8:
            avg_price_list = price_list[-8:]     # Die letzten 8 Elemente durch Slicing ermitteln
           
            for i in range(len(avg_price_list)):
               avg_price_list[i] = float(avg_price_list[i]) #Einzelne List-Objekt in Float konvertieren
            
            avg_price_list.pop() #letze List-Objekt entfernen.

        avg_price = float(np.median(avg_price_list))
        #print('AVG = ', avg_price_list)
        #print('TYPE', type(avg_price))
        #print('Preis (avg) = ', avg_price)
        return avg_price
    
    def calc_todays_price(self, prices):
        price_list = []
        todays_price = None

        #Preise in einer Preis-Liste speichern 
        for price in prices:
            #print(type(price))
            price_list.append(format(price, '.2f'))
        #print('Aktuelle Preisliste = ', price_list)
        
        
        todays_price = float(price_list[-1]) 
        #print('TYPE', type(todays_price))
        #print(f'Preis (heute) =  {todays_price}')
            
        return todays_price    
    
    
    
          
    def suggest_result(self, prices):
        
        price_list = []
        avg_price_list = []
        avg_price = None
        todays_price = None
        suggestion = None
        good_news = '👍' #'Guter Zeitpunkt zum Tanken!'
        bad_news =  '👎'# 'Schlechter Zeitpunkt zum Tanken!'
        
       #Preise in einer Preis-Liste speichern 
        for price in prices:
            #print(type(price))
            price_list.append(format(price, '.2f'))
        #print('Aktuelle Preisliste = ', price_list)
        
        
        if len(price_list) >= 8:
            avg_price_list = price_list[-8:]     # Die letzten 8 Elemente durch Slicing ermitteln
           
            for i in range(len(avg_price_list)):
               avg_price_list[i] = float(avg_price_list[i]) #Einzelne List-Objekt in Float konvertieren
            
            avg_price_list.pop() #letze List-Objekt entfernen.

        avg_price = float(np.median(avg_price_list))
        #print('AVG = ', avg_price_list)
        #print('TYPE', type(avg_price))
        #print('Preis (avg) = ', avg_price)

        todays_price = float(price_list[-1]) 
        #print('TYPE', type(todays_price))
        #print(f'Preis (heute) =  {todays_price}')
        
        if todays_price <= avg_price:
            suggestion  = good_news
        else:
            suggestion = bad_news
            
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
        
        #Diagramm mit fixe Größe erstellen
        #width = 15
        #heigh = 5
        
        fig, ax = plt.subplots()#figsize =(width, heigh)


        #Balkendiagramm erstellen
        ax.bar(dates, prices, width=0.5, align='center', edgecolor='black')
        
        #AVG Kraftstoffspreis im Diagramm abbilden
        for i, price in zip(dates, prices):
            ax.text(i, price + 0.00, f'{price:.2f}', ha='center', va='top', rotation=90, color = 'white')

        #ax.set_xlabel('Datum')
        ax.set_ylabel(f'Preis in EUR')
        ax.set_title(f'Preisentwicklung - Kraftstoff: {fuel_type.upper()}')
        #ax.set_xticklabels(dates, rotation=90) #fontsize = 5
        ax.set_xticks = True
        
        # FigureCanvasTkAgg erstellen und in das Frame einbinden
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    

        
############################################################################################


# Usage Example:
db_path = '/Users/Janjira Boonkhamsaen/Desktop/tk_hist.db' #dynamisch anpassen
station_uuid = '005056ba-7cb6-1ed2-bceb-aab58f050d43' #Dynamisch anpassen!!! get from selection 
fuel_type = 'diesel' #Dynamisch anpassen!!! get from selection 

fuel_analyzer = FuelPriceAnalyzer(db_path)

if fuel_analyzer.connect_to_hist_database():
    data_frame = fuel_analyzer.retrieve_data(station_uuid)
    print(data_frame)

    if data_frame is not None: 
        dates, prices = fuel_analyzer.process_data(data_frame, fuel_type)
        #print(dates, prices)
        
        avg_price = fuel_analyzer.calc_avg_price(prices)
        todays_price = fuel_analyzer.calc_todays_price(prices)
        suggestion = fuel_analyzer.suggest_result(prices)


        #print('1. Preis Heute: ', todays_price)
        #print('2. Preis AVG: ', avg_price)
        #print('3. Empfehlung: ', suggestion)
        #fuel_analyzer.visualize_data(dates, prices, fuel_type)
        
     
    fuel_analyzer.close_connection()
    
 #GUI  
root = tk.Tk()


############################################################################################
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
selected_station = 'JET, Provinzialstr. 99, 44388 Dortmund' #Dynamisch anpassen!!! get from selection 
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

#Chartt TODO: Tomorrow
chartFrame = ttk.Frame(root, width= cf_width, height= cf_height, style= 'chartFrame.TFrame')
chartFrame.grid(padx= 10, pady= 5, columnspan=3, sticky='NSEW')
fuel_analyzer.visualize_data(dates, prices, fuel_type, chartFrame)

###...
#Barchart in chart frame einbetteln

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