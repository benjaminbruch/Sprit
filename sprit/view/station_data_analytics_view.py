import customtkinter
from sprit.model.station_data_analytics_model import StationDataAnalyticsModel

class StationDataAnalyticsView(customtkinter.CTkFrame):
    def __init__(self, master, model: StationDataAnalyticsModel, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.price_label = customtkinter.CTkLabel(self,
                                                  text="Detail",
                                                  font=('Arial', 48),
                                                  text_color='#fabe02',
                                                  fg_color='black',
                                                  padx=10)

        self.price_label.grid(row=0, column=0, padx=10, pady=(15, 10), sticky='ns')

