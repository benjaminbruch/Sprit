import customtkinter
from sprit.model.station_info_card_model import StationInfoCardModel


class StationInfoCardView(customtkinter.CTkFrame):

    card_bg_color = '#4e5d77'
    card_price_font_size = ('Digital-7', 48)
    card_price_font_color = '#fabe02'
    card_price_bg_color = 'black'

    def __init__(self, master, model: StationInfoCardModel, **kwargs):
        super().__init__(master, **kwargs)
        self.model = model
        self.selected = False

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.price_label = customtkinter.CTkLabel(self,
                                                  text=self.model.price,
                                                  font=self.card_price_font_size,
                                                  text_color=self.card_price_font_color,
                                                  fg_color=self.card_price_bg_color,
                                                  padx=10)
        self.price_label.grid(row=0, column=0, padx=10, pady=(15,10), sticky='ns')

        self.extra_info_label = customtkinter.CTkLabel(self, text=self.model.extra_info, font=('Arial', 10))
        self.extra_info_label.grid(row=1, column=0, sticky='w', padx=10, pady=(0, 10))

        self.company_address_frame = customtkinter.CTkFrame(self, fg_color=self.card_bg_color)
        self.company_address_frame.grid(row=0, column=1, sticky='nsew', padx=(0, 10), pady=(5, 0))

        self.company_label = customtkinter.CTkLabel(self.company_address_frame,
                                                    text=self.model.company_name,
                                                    font=('Arial', 22),
                                                    wraplength=161,
                                                    justify="left")
        self.company_label.grid(row=0, column=0, sticky='nw', padx=(5, 5), pady=(5, 0))

        self.address_label = customtkinter.CTkLabel(self.company_address_frame,
                                                    text=self.model.address,
                                                    font=('Arial', 12), justify="left")
        self.address_label.grid(row=1, column=0, sticky='nw', padx=(5, 5), pady=(5, 0))

        self.distance_label = customtkinter.CTkLabel(self,
                                                     text=str(self.model.distance) + " km",
                                                     font=('Arial', 12))
        self.distance_label.grid(row=1, column=2, sticky='e', padx=(0, 10), pady=(0, 10))