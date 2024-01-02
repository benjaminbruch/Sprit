import tkinter as tk
import sprit.model.station_info_card_model as StationInfoCardModel

class StationInfoCard(tk.Frame):
    def __init__(self, parent, model: StationInfoCardModel, click_callback=None):
        super().__init__(parent)
        self.model = model
        self.click_callback = click_callback
        self.selected = False
        self.card_bg_color = 'gray'

        self.config(bg=self.card_bg_color, bd=2)  # Dark grey background for the card

        # Left side for the price
        left_frame = tk.Frame(self, bg='black')
        left_frame.grid(row=0, column=0, sticky='ns')

        self.price_label = tk.Label(left_frame, text=self.model.price, font=('Digital-7', 48), fg='yellow', bg='black')
        self.price_label.grid(row=0, column=0, padx=10, pady=10)

        # Right side for the text information
        right_frame = tk.Frame(self, bg=self.card_bg_color)
        right_frame.grid(row=0, column=1, sticky='nsew')

        self.company_label = tk.Label(right_frame, text=self.model.company_name, font=('Arial', 16), fg='white', bg=self.card_bg_color)
        self.company_label.grid(row=0, column=0, sticky='w')

        self.address_label = tk.Label(right_frame, text=self.model.address, font=('Arial', 12), fg='white', bg=self.card_bg_color)
        self.address_label.grid(row=1, column=0, sticky='w')

        self.extra_info_label = tk.Label(right_frame, text=self.model.extra_info, font=('Arial', 10), fg='white', bg=self.card_bg_color)
        self.extra_info_label.grid(row=2, column=0, sticky='w')

        # Right side for the distance and arrow icon
        distance_frame = tk.Frame(right_frame, bg=self.card_bg_color)
        distance_frame.grid(row=3, column=0, sticky='e')

        self.distance_label = tk.Label(distance_frame, text=self.model.distance, font=('Arial', 12), fg='white', bg=self.card_bg_color)
        self.distance_label.grid(row=0, column=0)

        # Bind click event to all widgets
        self.bind_click_event(self)

    def bind_click_event(self, widget):
        widget.bind("<Button-1>", self.on_click)
        for child in widget.winfo_children():
            self.bind_click_event(child)

    def on_click(self, event):
        if self.click_callback:
            self.click_callback(self)

    def toggle_select(self):
        self.selected = not self.selected

        if self.selected == True:
            self.card_bg_color = 'green'
        else:
            self.card_bg_color = 'gray'

        self.config(bg=self.card_bg_color, bd=2)
        self.update_widget_colors(self)

    def update_widget_colors(self, widget):
        if widget != self.price_label:
            widget.config(bg=self.card_bg_color)
        for child in widget.winfo_children():
            self.update_widget_colors(child)

    def get_station(self):
        return self.model.station