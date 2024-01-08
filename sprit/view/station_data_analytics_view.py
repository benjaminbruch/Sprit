import customtkinter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sprit.model.station_data_analytics_model import StationDataAnalyticsModel

class StationDataAnalyticsView(customtkinter.CTkFrame):
    def __init__(self, master, model: StationDataAnalyticsModel, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #Mock data
        self.prices = np.random.uniform(1.65, 1.70, 14)
        self.dates =pd.date_range(start="2024-01-01", end="2024-01-14")
        self.dates = self.dates.strftime("%d.%m")

        self.chart_frame = customtkinter.CTkFrame(self)
        self.chart_frame.grid(row=0, column=0, sticky='nsew')
        self.create_chart(self.dates, self.prices, self.chart_frame)


        self.average_recommendation_frame = customtkinter.CTkFrame(self)
        self.average_recommendation_frame.grid(row=0, column=1, sticky='nsew')

        self.average_price_label = customtkinter.CTkLabel(self.average_recommendation_frame, text="Durchschnittspreis: ", font=("Arial", 12))
        self.average_price_label.grid(row=0, column=1, sticky='nsew')

        self.recommendation_label = customtkinter.CTkLabel(self.average_recommendation_frame, text="Empfehlung: ", font=("Arial", 12))
        self.recommendation_label.grid(row=1, column=1, sticky='nsew')


    def create_chart(self, dates, prices, frame):
        min_price = min(prices) - 0.01
        max_price = max(prices) + 0.01

        fig, ax = plt.subplots()
        # Adjust the subplot parameters
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

        fig.set_facecolor('#323333')
        ax.set_facecolor('#323333')

        ax.bar(dates, prices, width=0.8, align='center', color="#4e5d78")

        ax.set_yticks([])
        # Set the y-axis limits
        ax.set_ylim([min_price, max_price])

        # Display the price on top of each bar
        for i, price in zip(dates, prices):
            ax.text(i, price + 0.00, f'{price:.2f}', ha='center', va='bottom', color='white')

        # Set the labels and title
        ax.tick_params(axis='x', colors='white')

        every_second_date = dates[::2]  # Slice the list to get every second date

        plt.xticks(every_second_date)

        # Remove the frame
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)

        # FigureCanvasTkAgg erstellen und in das Frame einbinden
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, sticky='nsew')
        canvas_widget.grid_columnconfigure(index=0, weight=1)
        canvas_widget.grid_propagate(False)  # Prevent the widget from changing its size due to its children
        canvas_widget.configure(height=150)