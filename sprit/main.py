import tkinter as tk
from sprit.controller.stations_list_map_view_controller import StationsListMapViewController

def main():
    root = tk.Tk()
    controller = StationsListMapViewController(root)
    controller.run()

if __name__ == "__main__":
    main()
