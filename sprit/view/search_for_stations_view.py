import PySimpleGUI as sg
from model.search_for_stations_model import SearchForStationsModel, Distance, SpritType, BrandType, OpenType, SortBy


class SearchForStationsView:

    def __init__(self, view_model: SearchForStationsModel):

        self.view_model = view_model

        # Define the window's contents (layout)
        layout = [
            [sg.Text('Entfernung: '),
             sg.Spin(['2km', '5km', '10km'], key='-Distance-')
            ],
            [sg.Text()],
              [sg.Text('Marken: '),
               sg.Radio('Alle', "Radio1", key='-Brand_Alle-', default=True),
               sg.Radio('Aral', "Radio1", key='-Brand_Aral-'),
               sg.Radio('Shell', "Radio1", key='-Brand_Shell-'),
               sg.Radio('Total', "Radio1", key='-Brand_Total-')
            ],
            [sg.Text()],
              [sg.Text('Kraftstoff: '),
               sg.Radio('all', "Radio2", key='-Sprit_Alle-', default=True),
               sg.Radio('e5', "Radio2", key='-Sprit_e5-'),
               sg.Radio('e10', "Radio2", key='-Sprit_e10-'),
               sg.Radio('Diesel', "Radio2", key='-Sprit_Diesel-'),
            ],
            [sg.Text()],
              [sg.Text('Sortierung nach: '),
               sg.Radio('Entfernung', "Radio3", key='-Sort_dist-', default=True),
               sg.Radio('Preis', "Radio3", key='-Sort_price-'),
            ],
            [sg.Text()],
            [sg.Checkbox('Nur geöffnete Tankstellen', key='-Open-', default=False)], 
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

                #Marke aus Eingabe ermitteln
                if values['-Brand_Alle-'] == True: brand = BrandType.all
                elif values['-Brand_Aral-'] == True: brand = BrandType.aral
                elif values['-Brand_Shell-'] == True: brand = BrandType.shell
                elif values['-Brand_Total-'] == True: brand = BrandType.total

                #Kraftstoff aus Eingabe ermitteln
                if values['-Sprit_Alle-'] == True: sprit = SpritType.all
                elif values['-Sprit_e5-'] == True: sprit = SpritType.e5
                elif values['-Sprit_e10-'] == True: sprit = SpritType.e10
                elif values['-Sprit_Diesel-'] == True: sprit = SpritType.diesel

                #Sortierung aus Eingabe ermitteln
                if values['-Sort_dist-'] == True: sort = SortBy.distance
                elif values['-Sort_price-'] == True: sort = SortBy.price

                #Aus Eingabe ermitteln, ob nur geöffnete Tankstellen angezeigt werden sollen
                if values['-Open-'] == True: open = OpenType.is_open
                else: open = OpenType.all
                
                data = self.view_model.get_nearby_stations(adress, distance, sprit, brand, open, sort)
                self.window['-ML-'].update(data)

        self.window.close()
