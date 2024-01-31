import PySimpleGUI as sg
from model.search_for_stations_model import SearchForStationsModel, Distance, SpritType, BrandType, OpenType, SortBy

# This is first iteration of the main view and base for the stations_search_list_map_view.py
class SearchForStationsView:
    """
    View class for searching for gas stations based on certain criteria.
    """

    def __init__(self, view_model: SearchForStationsModel):
        """
        Initialize the view with the given model.

        Args:
            view_model (SearchForStationsModel): The model to use for this view.
        """
        self.view_model = view_model

        # Define the window's contents (layout)
        layout = [
            [sg.Text('Distance: '),
             sg.Spin(['2km', '5km', '10km'], key='-Distance-')
            ],
            [...]
        ]

        # Create the window
        self.window = sg.Window("Search for Stations", layout)

    def run(self):
        """
        Run the event loop for the window.
        """
        # Event loop
        while True:
            event, values = self.window.read()

            if event == sg.WIN_CLOSED:
                break

            if event == '-Button1-':
                address = values['-Input-']
                distance = values['-Distance-']

                # Determine the distance from the input
                match values['-Distance-']:
                    [...]

                # Determine the brand from the input
                if values['-Brand_Alle-'] == True: brand = BrandType.all
                elif values['-Brand_Aral-'] == True: brand = BrandType.aral
                elif values['-Brand_Shell-'] == True: brand = BrandType.shell
                elif values['-Brand_Total-'] == True: brand = BrandType.total

                # Determine the fuel type from the input
                if values['-Sprit_Alle-'] == True: sprit = SpritType.all
                elif values['-Sprit_e5-'] == True: sprit = SpritType.e5
                elif values['-Sprit_e10-'] == True: sprit = SpritType.e10
                elif values['-Sprit_Diesel-'] == True: sprit = SpritType.diesel

                # Determine the sorting from the input
                if values['-Sort_dist-'] == True: sort = SortBy.distance
                elif values['-Sort_price-'] == True: sort = SortBy.price

                # Determine from the input whether only open gas stations should be displayed
                if values['-Open-'] == True: open = OpenType.is_open
                else: open = OpenType.all

                data = self.view_model.get_nearby_stations(address, distance, sprit, brand, open, sort)
                self.window['-ML-'].update(data)

        self.window.close()