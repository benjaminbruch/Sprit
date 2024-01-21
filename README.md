# Sprit - Tankstellenpreise in Echtzeit

![sprit_banner.png](files%2Fsprit_banner.png)

## Ein Semesterprojekt der Projektgruppe A3-3 im Modul "Programmierung für KI" an der Fachhochschule Südwestfalen

<!-- TABLE OF CONTENTS -->
## Inhaltsverzeichnis
* [Funktionen](#Funktionen)
* [Installation](#Installation)
* [Benutzung](#Benutzung)
* [Vorgehensweise im Projekt](#Vorgehensweise-im-Projekt)
* [Datenimport](#Datenimport)
* [Ausblick](#Ausblick)
* [Hinweise](#Hinweise)
* [Anerkennung](#Anerkennung)


<!-- Features -->
## Funktionen
* Tankstellen in der Umgebung suchen inkl. Echtzeitpreise
* Sortierung nach Preis und Entfernung
* Filtern nach Kraftstoffart
* Darstellung der Tankstellen auf einer Karte
* Anzeige von historischen Preisen
* Empfehlung der günstigsten Tankstelle und der günstigsten Tankzeit

<!-- INSTALLATION -->
## Installation
Es gibt 2 Möglichkeiten die App zu installieren:

a) Die App kann auf Github unter "Release" für die jeweilige Plattform heruntergeladen werden.

b) Die App kann auch über den Quellcode installiert werden. Dazu muss das Repository geklont werden. Danach sollte in einer Virtuellen Umgebung die Datei `requirements.txt` installiert werden. 
Abschließend kann die Datei `main.py` ausgeführt werden.

Optional: Kann die unter [Datenimport](#Datenimport) beschriebene Datenbank aktualisiert werden.

<!-- USAGE EXAMPLES -->
## Benutzung
 ![list_map_search_view_screenshot.png](files%2Flist_map_search_view_screenshot.png)

1. Eingabe der Adresse in der Suchleiste und anschließendes Drücken der Enter-Taste oder des Suchbuttons
2. Auswahl der gewünschten Kraftstoffart
3. Auswahl der gewünschten Sortierung
4. Tankstellen werden auf der Karte angezeigt
5. Bei Auswahl einer Tankstelle in der Liste zoomt die Karte auf die entsprechende Tankstelle
 
<!-- PLANNING -->
## Vorgehensweise im Projekt
![trello_screenshot.png](files%2Ftrello_screenshot.png)
*Bildschirmfoto von unserem Trelloboard*

In unserem ersten Treffen haben wir die Grundlage für unser App-Projekt gelegt. Unser Fokus lag darauf, die Funktionen der App zu definieren und einen Plan für deren Umsetzung zu entwickeln. Dabei haben wir uns für die Programmierung mit Python und Tkinter entschieden, da diese Tools eine effiziente und flexible Entwicklung ermöglichen.

Für die Datenintegration haben wir uns für die API von Tankerkönig entschieden. Dies war eine strategische Entscheidung, da Tankerkönig eine kostenlose API anbietet, die Echtzeitdaten liefert. Dies passt perfekt zu unseren Anforderungen und gewährleistet eine hohe Aktualität und Zuverlässigkeit der Daten in unserer App.

Um die Entwicklung dynamisch und anpassungsfähig zu gestalten, haben wir uns für einen agilen Ansatz entschieden. Wir arbeiteten in zweiwöchigen Sprints, was uns ermöglichte, regelmäßig Features zu implementieren und zu bewerten. Nach jedem Sprint reflektierten wir unsere Fortschritte und planten, welche neuen Features im nächsten Sprint integriert werden sollten. Diese Methode förderte nicht nur eine kontinuierliche Verbesserung, sondern auch eine flexible Anpassung an sich ändernde Anforderungen.

Für die Übersicht und Projektplanung setzten wir auf Trello. Dieses Tool half uns, Aufgaben zu organisieren, den Fortschritt zu verfolgen und effektiv als Team zusammenzuarbeiten. Zur Versionsverwaltung unserer Codebasis wählten wir GitHub. Dies ermöglichte uns eine sichere Speicherung unseres Codes, eine reibungslose Zusammenarbeit im Team und eine effiziente Verfolgung von Änderungen.

Insgesamt bildeten diese Entscheidungen und Tools die Grundlage für eine strukturierte und effiziente Entwicklung unserer App. Wir waren in der Lage, ein robustes Produkt zu schaffen, das auf den Prinzipien guter Softwareentwicklungspraktiken basiert.

<!-- Datenimport -->
## Datenimport
Aktuell wird für den Abruf der historischen Spritpreise und der Berechnung von Durchschnittspreis und Preisempfehlung eine lokale SQLite-Datenbank verwendet. Die Datenbank wird in der Datei `tk_hist.db` im Ordner `data` gespeichert. 
Um die Daten zu aktualisieren, müssen die aktuellen CSV-Dateien von der Tankerkönig-Seite: https://dev.azure.com/tankerkoenig/_git/tankerkoenig-data?path=/prices geladen werden und in den Ordner `data/csv` kopiert werden. Anschließend kann das Skript `import_hist_tk_data.py` ausgeführt werden. Die Datenbank wird dann aktualisiert.

Aufgrund der Limitierung von Github von Dateigrößen auf 50 MB konnten wir die Datenbank nicht in das Repository hochladen. Deswegen muss die Datenbank lokal erstellt werden.
<!-- Ausblick -->
## Ausblick
In zukünftigen Updates planen wir, die aktuelle SQLite-Datenbank durch eine remote gehostete Datenbank zu ersetzen. Dies wird es uns ermöglichen, die Daten zentral zu speichern und von verschiedenen Geräten aus darauf zuzugreifen. Die Kommunikation mit der Datenbank wird über eine REST-Schnittstelle erfolgen, die eine standardisierte und effiziente Interaktion mit den Daten ermöglicht. Dieser Schritt wird die Skalierbarkeit und Flexibilität unserer Anwendung erheblich verbessern.

Desweiteren planen wir, Caching-Techniken einzuführen, um die Leistung und Benutzererfahrung zu verbessern. Caching ermöglicht es uns, häufig abgerufene Daten temporär zu speichern, um zukünftige Anfragen schneller zu bedienen.
<!-- Hinweise -->
## Hinweise 
Für die Erstellung dieser Readme und der Dokumentation inklusive der Inline-Kommentare sowie der Unit-Tests wurde die Hilfe von Github Copilot & OpenAI ChatGPT in Anspruch genommen. Desweiteren wurden diese Tools auch zum Auflösen und Beheben von Fehlermeldungen verwendet.
<!-- ACKNOWLEDGEMENTS -->
## Anerkennung 
* [Tankerkönig](https://tankerkoenig.de)
* [Customtkinter](https://customtkinter.tomschimansky.com)
* [Trello](https://trello.com/de)
* [PyCharm](https://www.jetbrains.com/de-de/pycharm/)
* [Visual Studio Code](https://code.visualstudio.com)
* [Github](https://github.com)
* [GithubCopilot](https://copilot.github.com)
* [ChatGPT](https://chat.openai.com/)






 
