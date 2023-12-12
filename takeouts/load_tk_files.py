# Funktioniert so nicht, da html Format! Evtl. Beautiful Soup?

import requests

#url = 'https://www.beispielwebsite.com/pfad/zur/datei/dateiname.txt'
#url = 'https://dev.azure.com/tankerkoenig/_git/tankerkoenig-data?path=/stations/2023/12/2023-12-02-stations.csv'
url = 'https://dev.azure.com/tankerkoenig/_git/tankerkoenig-data?path=/prices/2023/12/2023-12-02-prices.csv'

#ziel_dateipfad = 'lokaler/speicherort/dateiname.txt'
#ziel_dateipfad = '/Users/joerg/Programming/AKI/KI Programmierung/Sprit/sprit/data/2023-12-02-stations.csv'
ziel_dateipfad = '/Users/joerg/Programming/AKI/KI Programmierung/Sprit/sprit/data/2023-12-02-prices.csv'

# Die Datei herunterladen
antwort = requests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war (Statuscode 200 bedeutet Erfolg)
if antwort.status_code == 200:
    # Die heruntergeladene Datei speichern
    with open(ziel_dateipfad, 'wb') as datei:
        datei.write(antwort.content)
    print("Die Datei wurde erfolgreich heruntergeladen und gespeichert.")
else:
    print("Fehler beim Herunterladen der Datei. Statuscode:", antwort.status_code)
