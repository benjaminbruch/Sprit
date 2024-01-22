import customtkinter
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sprit.model.station_data_analytics_model import StationDataAnalyticsModel


class StationDataAnalyticsView(customtkinter.CTkFrame):
    def __init__(self, master, model: StationDataAnalyticsModel, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model

        self.thumb_icon = Image.open("sprit/resources/recommendation_icons/thumb_up_green.png") if (
            self.model.is_recommended) else Image.open(
            "sprit/resources/recommendation_icons/thumb_down_red.png")

        self.frame_background_color = '#323333'
        self.box_background_color = 'black'

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.chart_label_frame = customtkinter.CTkFrame(self, fg_color=self.frame_background_color)
        self.chart_label_frame.grid(row=0, column=0, sticky='nsew', padx=(0, 10))
        self.chart_label_frame.grid_rowconfigure(0, weight=0)
        self.chart_label_frame.grid_rowconfigure(1, weight=1)
        self.chart_label_frame.grid_columnconfigure(0, weight=1)

        self.chart_label = customtkinter.CTkLabel(self.chart_label_frame, text=f"Preisentwicklung in €",
                                                  font=("Arial", 24, "bold"), pady=10, fg_color="transparent")
        self.chart_label.grid(row=0, column=0, sticky='nsew', pady=(0, 10))

        self.chart_frame = customtkinter.CTkFrame(self.chart_label_frame, fg_color=self.frame_background_color)
        self.chart_frame.grid(row=1, column=0, sticky='nsew', pady=(0, 10))
        self.chart_frame.grid_rowconfigure(0, weight=1)
        self.chart_frame.grid_columnconfigure(0, weight=1)
        self.create_chart(self.model.dates, self.model.prices, self.chart_frame)

        self.average_recommendation_frame = customtkinter.CTkFrame(self, fg_color=self.frame_background_color)
        self.average_recommendation_frame.grid(row=0, column=1, sticky='nsew', padx=(0, 10))
        self.average_recommendation_frame.grid_rowconfigure(0, weight=1)
        self.average_recommendation_frame.grid_rowconfigure(1, weight=1)
        self.average_recommendation_frame.grid_columnconfigure(0, weight=1)

        self.average_price_label = customtkinter.CTkLabel(self.average_recommendation_frame, text="Durchschnittspreis",
                                                          font=("Arial", 20, "bold"), pady=10, fg_color="transparent")
        self.average_price_label.grid(row=0, column=0, sticky='nsew', pady=(0, 10))
        self.average_price_box = customtkinter.CTkLabel(self.average_recommendation_frame,
                                                        text=self.model.average_price + ' €',
                                                        font=('Digital-7', 48),
                                                        text_color='#fabe02',
                                                        fg_color=self.box_background_color,
                                                        padx=10,
                                                        pady=10)
        self.average_price_box.grid(row=1, column=0, sticky='nsew', pady=(0, 20))

        self.recommendation_label = customtkinter.CTkLabel(self.average_recommendation_frame, text="Tankempfehlung",
                                                           font=("Arial", 20, "bold"), pady=10)
        self.recommendation_label.grid(row=2, column=0, sticky='nsew', pady=(0, 20))

        self.recommendation_icon = customtkinter.CTkImage(self.thumb_icon, size=(64, 64))
        self.recommendation_box = customtkinter.CTkLabel(self.average_recommendation_frame,
                                                         image=self.recommendation_icon,
                                                         text="",
                                                         fg_color=self.frame_background_color,
                                                         pady=20)
        self.recommendation_box.grid(row=3, column=0, sticky='nsew', pady=(0, 20))

    def create_chart(self, dates, prices, frame):

        dates = dates.to_numpy(dtype='datetime64[D]')

        # Assuming 'dates' is your numpy array of dates
        formatted_dates = np.datetime_as_string(dates, unit='D')

        # Extract day and month from the formatted dates
        dates = [date[8:10] + '.' + date[5:7] for date in formatted_dates]

        min_price = min(prices) - 0.01
        max_price = max(prices) + 0.01

        fig, ax = plt.subplots()
        # Adjust the subplot parameters
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

        fig.set_facecolor(self.frame_background_color)
        ax.set_facecolor(self.frame_background_color)

        ax.bar(dates, prices, width=0.8, align='center', color="#4e5d78")

        ax.set_yticks([])
        # Set the y-axis limits
        ax.set_ylim([min_price, max_price])

        # Display the price on top of each bar
        for i, price in zip(dates, prices):
            ax.text(i, price + 0.00, f'{price:.2f}', ha='center', va='bottom', color='white')

        for index, (price, date) in enumerate(zip(prices, dates)):
            ax.text(index, min_price + 0.001, date, ha='center', va='bottom', color='white', fontsize=8)

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

        plt.close(fig)

    def update_view(self, station_id, fuel_type):
        self.model.update_data(station_id, fuel_type)
        self.create_chart(self.model.dates, self.model.prices, self.chart_frame)

        self.average_price_box.configure(text=self.model.average_price + ' €')

        self.thumb_icon = Image.open("sprit/resources/recommendation_icons/thumb_up_green.png") if (
            self.model.is_recommended) else Image.open(
            "sprit/resources/recommendation_icons/thumb_down_red.png")
        self.recommendation_icon = customtkinter.CTkImage(self.thumb_icon, size=(64, 64))
        self.recommendation_box.configure(image=self.recommendation_icon)


