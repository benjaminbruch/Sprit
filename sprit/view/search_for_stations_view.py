import PySimpleGUI as sg
from model.search_for_stations_model import SearchForStationsModel, Distance, SpritType, BrandType, OpenType, SortBy


class SearchForStationsView:

    def __init__(self, view_model: SearchForStationsModel):

        self.view_model = view_model

        # Define the window's contents (layout)
        layout = [
            [sg.Text('Entfernung'),
             sg.Spin(['2km', '5km', '10km'], key='-Distance-')
             ],
            [sg.Text()],
            [sg.Text('Adresse:'),
             sg.Input(key='-Input-')
             ],
            [sg.Text('')],
            [sg.Text('Ergebnis')],
            [sg.Multiline("", size=(150, 40), disabled=True, key="-ML-")],
            [sg.Button('Suchen', key='-Button1-')]
        ]

        # Create the window
        self.window = sg.Window("Suche nach Stationen", layout)

    def run(self):
        # Event loop
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == '-Button1-':
                adress = values['-Input-']
                distance = values['-Distance-']

                match values['-Distance-']:
                    case '2km':
                        distance = Distance.TWO_KM
                    case '5km':
                        distance = Distance.FIVE_KM
                    case '10km':
                        distance = Distance.TEN_KM
# Alter Aufruf 
#                data = self.view_model.get_nearby_stations(adress, distance)

                #adresse = 'Berlin'
                #dist = Distance.FIVE_KM
                sprit = SpritType.e10
                brand = BrandType.total
                open = OpenType.is_open
                sort = SortBy.distance
                print('TEST: ', adress, distance, sprit, brand, open, sort)
                #data = SearchForStationsModel()
                data = self.view_model.get_nearby_stations(adress, distance, sprit, brand, open, sort)
                self.window['-ML-'].update(data)

        self.window.close()
