import os

#Programm um den absoluten Pfad einer Datei in einem Verzeichnis zu ermitteln

# Relative Pfadangabe zur CSV-Datei
rel_csv_path = '2023-12-01-prices.csv'

# Verwende os.path, um den absoluten Pfad zur CSV-Datei zu erhalten
abs_csv_path = os.path.abspath(rel_csv_path)

print(abs_csv_path)

