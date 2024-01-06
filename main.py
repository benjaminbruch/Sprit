import customtkinter
from sprit.view.stations_search_list_map_view import StationsSearchListMapView

def main():
    app = customtkinter.CTk()
    app.title("Sprit - Tankstellensuche")
    app.geometry("1200x600")
    app.minsize(1200, 600)

    # Configure the grid to expand
    app.grid_columnconfigure(0, weight=0)
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)

    view = StationsSearchListMapView(app)
    view.start()


if __name__ == "__main__":
    main()
