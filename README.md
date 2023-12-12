# Sprit
15.11.2023 JT

ersten Prototyp erstellt als "TK_Sprint1.jpynb" und "TK_Sprint1.py".
Vor der Nutzung sind Bibliotheken zu installieren:
pip install pysimplegui
pip install pytankerkoenig
pip install geopy

Die angezeigten Daten sind noch als Rohdaten im Json Format. Der nächste Schritt wäre die Daten zu in eine anzeigbare Form zu bringen.

Links zu Dokumentationen:

PySimpleGUI
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms

Homepage & Docs
https://www.pysimplegui.org/en/latest/

Tankerkoenig
pytankerkoenig auf github
https://github.com/ultrara1n/pytankerkoenig

Beschreibung pytankerkoenig
https://pypi.org/project/pytankerkoenig/

API Beschreibung von Tankerkoenig direkt
https://creativecommons.tankerkoenig.de/?page=info

GeoPy
https://geopy.readthedocs.io/en/stable/



-------------------------------------------------------------------------------------------------

12.12.2023 JT

Fertigstellung:

- Prototype zur Abfrage der Stationen eines Umkreises

- Anlegen einer Datenbank mit historischen Daten und Funktionen zur Abfrage der Preis- und Stationsdaten implementiert


PROTOTYP:

- Ausführen des Prototyps durch Aufruf von "main.py" im Projektverzeichnis "sprit".

Die Oberfläche ist intuitiv bedienbar. Einfach ein wenig ausprobieren.

Das Ergebnis der Suche wird im Fensterausschnitt Ergebnis angezeigt. 


- Beschreibung des Prototyps:

Die Oberfläche des Prototyps ist mit PySimpleGUI im Modul "search_for_stations_view.py" im Verzeichnis "View" realisiert. 
Neben der Funktion als Prototyp dient die Oberfläche zum Testen der zugrunde liegenden Funktionen.

Der Zugriff auf die Tankerkönig (kurz: TK)  API (ist im Modul "search_for_stations_model.py" implementiert. 

Der Zugriff auf die TK Daten erfolgt in der Klasse "SearchForStationsModel" über die Funktion "get_nearby_stations(...)".

Der Aufruf hat folgende Auswahlparameter:

	- Adresse
	- Entfernung
	- Benzinsorte
	- Marke
	- geöffnet
	- Sortierung


Das Ergebnis ist eine Liste von Dictionarie. Bsp:

[
{
'id': '813ed58c-b58d-4d17-895b-2078cb302649',
'name': 'Aral Tankstelle',
'brand': 'ARAL',
'street': 'Prinzenstraße',
'place': 'Berlin',
 lat': 52.501896,
 lng': 13.409839,
'dist': 2.2,
'price': 1.779,
'isOpen': True,
 'houseNumber': '29',
'postCode': 10969
},
{
'id': '278130b1-e062-4a0f-80cc-19e486b4c024',
'name': 'Aral Tankstelle',
'brand': 'ARAL',
'street': 'Holzmarktstraße',
'place': 'Berlin',
'lat': 52.514153,
'lng': 13.421487,
'dist': 2.2,
'price': 1.719,
'isOpen': True,
'houseNumber': '12/14',
'postCode': 10179
},
{
….
}
]

oder im Fehlerfall eine Fehlermeldung!!!

-------

HISTORISCHE DATENBANK


- Die täglich csv-Dateien mit den täglichen Preisänderungen und aktuellen Daten zu allen Tankstellen können mit dem Programm "imp_hist_tk_data.py" welches ich im Projekthauptverzeichnis befindet in die Datenbank geladen werden.

- Die csv-Dateien und die Datenbank befinden sich im Unterverzeichnis "data".

- Ich habe vorerst nur die Daten vom 01. bis 10. Dezember geladen. Da alle Tankstellen die Preise mehrfach täglich ändern, sind dies bereits 3,5 Mio. Datensätze. Bei Bedarf kann ich gern weiter Daten importieren. Ich habe alle verfügbaren historischen Daten von TK vorliegen.

-  Die Methoden zum Auslesen der Daten aus der Datenbank sind im Modulhist_db_funtions.py und gehören zur Klasse hist_data.

- Die Methode "get_date_prices" liefert alle Preisänderungen aller Tankstellen mit Uhrzeit. Die Tankstellen sind über die eindeutige uuid referenziert. Werden die Informationen zu der Tankstelle benötigt, sind diese mit der uuid über die Methode "get_station" abzufragen.

- Beispiele für den Aufruf der beiden Methoden finden sich im Programm "test_hist.py"

- Hier die Rückgabe-Struktur der Methode "get_date_prices":

    date: 2023-12-10
    time: 23:59:53
    uuid: 24b5a970-c494-4393-974c-384d4a93813b
    diesel: 1.759
    e5: 1.809
    e10: 1.749

- Hier die Rückgabe-Struktur der Methode "get_station":

    uuid: b0ad7578-8e3f-cad2-29bc-82380cf58f88
    name: Lenz Energie AG
    brand: 
    street: Darmst�dter Landstr.
    house_number: 63
    post_code: 64311
    city: Weiterstadt 

- Bei Fehlern, Änderungen, Anpassungen sowie bei Bedarf für weitere Funktionen meldet euch!!!


Next Steps für mich:

- Fehlerbearbeitung einbauen

- Code-Style verbessern 

----------------------------------------------------------------------------------------------




 






 
