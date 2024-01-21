import customtkinter
from sprit.model.station_info_card_model import StationInfoCardModel

class StationInfoCardView(customtkinter.CTkFrame):
    """
    A custom Tkinter Frame class for displaying information about a gas station.

    This class extends customtkinter.CTkFrame to create a UI component that shows detailed information
    about a gas station, such as price, company name, address, and distance. It is designed to be used
    as part of a larger interface where each station is represented by a card in a list.
    """

    # Class variables for styling the card
    card_bg_color = '#4e5d77'
    card_price_font_size = ('Digital-7', 48)
    card_price_font_color = '#fabe02'
    card_price_bg_color = 'black'

    def __init__(self, master, model: StationInfoCardModel, **kwargs):
        """
        Initialize the StationInfoCardView.

        Args:
            master: The parent widget.
            model: An instance of StationInfoCardModel containing the data to be displayed.
            **kwargs: Arbitrary keyword arguments for the CTkFrame.
        """
        super().__init__(master, **kwargs)
        self.model = model  # The data model for the station
        self.selected = False  # Tracks if this card is selected

        # Configure grid layout for the card
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Initialize and position the price label
        self.price_label = customtkinter.CTkLabel(self,
                                                  text=self.model.price,
                                                  font=self.card_price_font_size,
                                                  text_color=self.card_price_font_color,
                                                  fg_color=self.card_price_bg_color,
                                                  padx=10)
        self.price_label.grid(row=0, column=0, padx=10, pady=(15, 10), sticky='ns')

        # Initialize and position the additional information label
        self.extra_info_label = customtkinter.CTkLabel(self, text=self.model.extra_info, font=('Arial', 10))
        self.extra_info_label.grid(row=1, column=0, sticky='w', padx=10, pady=(0, 10))

        # Initialize and position the frame for company and address information
        self.company_address_frame = customtkinter.CTkFrame(self, fg_color=self.card_bg_color)
        self.company_address_frame.grid(row=0, column=1, sticky='nsew', padx=(0, 10), pady=(5, 0))

        # Initialize and position the company label
        self.company_label = customtkinter.CTkLabel(self.company_address_frame,
                                                    text=self.model.company_name,
                                                    font=('Arial', 22),
                                                    wraplength=161,
                                                    justify="left")
        self.company_label.grid(row=0, column=0, sticky='nw', padx=(5, 5), pady=(5, 0))

        # Initialize and position the address label
        self.address_label = customtkinter.CTkLabel(self.company_address_frame,
                                                    text=self.model.address,
                                                    font=('Arial', 12), justify="left")
        self.address_label.grid(row=1, column=0, sticky='nw', padx=(5, 5), pady=(5, 0))

        # Initialize and position the distance label
        self.distance_label = customtkinter.CTkLabel(self,
                                                     text=str(self.model.distance) + " km",
                                                     font=('Arial', 12))
        self.distance_label.grid(row=1, column=1, sticky='e', padx=(0, 10), pady=(0, 10))
