import tkinter as tk
import tkinter.messagebox
import re

class StationsSearchView:
    def __init__(self, root, search_callback):
        self.root = root
        self.search_callback = search_callback

        self.search_var = tk.StringVar()

        self.create_search_view()

    def create_search_view(self):
        self.search_frame = tk.Frame(self.root)
        self.search_frame.grid(row=0, padx=16, pady=16, sticky='ew')

        self.search_entry = tk.Entry(self.search_frame, textvariable=self.search_var)
        self.search_entry.grid(row=0, column=0, sticky='ew')

        self.search_button = tk.Button(self.search_frame, text='Suchen', command=self.search)
        self.search_button.grid(row=0, column=1, padx=8)

        # Create a new frame for the pickers
        self.pickers_frame = tk.Frame(self.root)
        self.pickers_frame.grid(row=1, padx=16, pady=16, sticky='ew')

        # Create label and picker for "Suchradius" in the pickers frame
        self.radius_var = tk.StringVar()
        self.radius_var.set("1")  # default value
        self.radius_label = tk.Label(self.pickers_frame, text="Suchradius")
        self.radius_label.grid(row=0, column=0, padx=8)
        self.radius_picker = tk.OptionMenu(self.pickers_frame, self.radius_var, *range(1, 11))
        self.radius_picker.grid(row=0, column=1, padx=8)

        # Create label and picker for "Sprit-Typ" in the pickers frame
        self.fuel_type_var = tk.StringVar()
        self.fuel_type_var.set("Diesel")  # default value
        self.fuel_type_label = tk.Label(self.pickers_frame, text="Sprit-Typ")
        self.fuel_type_label.grid(row=0, column=2, padx=8)
        self.fuel_type_picker = tk.OptionMenu(self.pickers_frame, self.fuel_type_var, "Diesel", "E10", "E5")
        self.fuel_type_picker.grid(row=0, column=3, padx=8)

        # Create label and picker for "Sortieren nach" in the pickers frame
        self.sort_by_var = tk.StringVar()
        self.sort_by_var.set("Preis")  # default value
        self.sort_by_label = tk.Label(self.pickers_frame, text="Sortieren nach")
        self.sort_by_label.grid(row=0, column=4, padx=8)
        self.sort_by_picker = tk.OptionMenu(self.pickers_frame, self.sort_by_var, "Preis", "Entfernung")
        self.sort_by_picker.grid(row=0, column=5, padx=8)

    def search(self):
        #self.search_callback(self.search_var.get())
        self.search_callback("Dresden, Hansastraße")