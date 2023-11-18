import PySimpleGUI as sg
import pytankerkoenig as tk
from geopy.geocoders import Nominatim


def adresse_zu_gps(adresse):
    geolocator = Nominatim(user_agent="FH_SWF")
    location = geolocator.geocode(adresse)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None
    
layout = [
    [sg.Text('Entfernung'), 
     sg.Spin(['2km','5km','10km'], key = '-Distance-')
    ],
    [sg.Text()],
    [sg.Text('Adresse:'),
     sg.Input(key = '-Input-')
    ],
    [sg.Text('')],
    [sg.Text('Ergebnis')],
    [sg.Multiline("", size = (150,40),disabled=True, key = "-ML-")],
    [sg.Button('Suchen', key = '-Button1-')]
]

window = sg.Window('Tankstellen suchen', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break;
    
    if event == '-Button1-':
        adr = values['-Input-']
        dist = values['-Distance-']

        match values['-Distance-']:
            case '2km':
                dist = float(2)
            case '5km':
                dist = 5
            case '10km':
                dist = 10

        lat, long = adresse_zu_gps(adr)

        data = tk.getNearbyStations('532bec4c-380c-6f32-d8c7-6a11d0d8b2d5',float(lat),float(long),dist,'all','dist')

        window['-ML-'].update(data)

window.close