import customtkinter
from sprit.model.station_data_analytics_model import StationDataAnalyticsModel

class StationDataAnalyticsView(customtkinter.CTkFrame):
    def __init__(self, master, model: StationDataAnalyticsModel, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.prices = [1.24, 1.25, 1.26, 1.27, 1.28, 1.29, 1.30]
        self.dates = ['1/1/2020', '1/2/2020', '1/3/2020', '1/4/2020', '1/5/2020', '1/6/2020', '1/7/2020']

        self.chart_frame = customtkinter.CTkFrame(self)
        self.chart_frame.grid(row=0, column=0, sticky='nsew')
        self.model.visualize_data(self.dates, self.prices, "diesel", self.chart_frame)