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
        self.search_frame.pack(side='top', fill='x', padx=16, pady=16)

        self.search_entry = tk.Entry(self.search_frame, textvariable=self.search_var)
        self.search_entry.pack(side='left', fill='x', expand=True)

        self.search_button = tk.Button(self.search_frame, text='Suchen', command=self.search)
        self.search_button.pack(side='right', padx=8)

    def search(self):
        #self.search_callback(self.search_var.get())
        self.search_callback("Dresden, Hansastraße")