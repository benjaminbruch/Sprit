# Kommentar
# zweiter Kommentar
from model.search_for_stations_model import SearchForStationsModel
from view.search_for_stations_view import SearchForStationsView

def main():
    model = SearchForStationsModel()
    view = SearchForStationsView(model)
    view.run()

if __name__ == "__main__":
    main()
