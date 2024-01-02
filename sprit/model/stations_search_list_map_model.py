from sprit.model.station_model import Station

class StationsSearchListMapModel:

    def __init__(self):
        self.stations: [Station] = [Station(
    id="1",
    name="Station 1",
    brand="Brand 1",
    street="Street 1",
    place="Place 1",
    lat=50.1,
    lng=8.6,
    dist=10,
    diesel=1.23,
    e5=1.45,
    e10=1.37,
    isOpen=True,
    houseNumber="1A",
    postCode="12345"
)]

