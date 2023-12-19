import tkinter as tk
from sprit.controller.stations_list_map_controller import StationsListMapController

def main():
    root = tk.Tk()
    controller = StationsListMapController(root)
    controller.run()

if __name__ == "__main__":
    main()
