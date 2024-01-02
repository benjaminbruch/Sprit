import customtkinter
from sprit.controller.stations_list_map_controller import StationsListMapController

def main():
    controller = StationsListMapController()
    controller.start()

if __name__ == "__main__":
    main()
