from enum import Enum


class SpritType(Enum):
    e5 = "e5"
    e10 = "e10"
    diesel = "diesel"
    all = "all"


class SortBy(Enum):
    distance = "dist"
    price = "price"


class Station:
    def __init__(self, id, name, brand, street, place, lat, lng, dist, price=None, diesel=None, e5=None, e10=None, isOpen=True, houseNumber=None, postCode=None):
        self.id = id
        self.name = name
        self.brand = brand
        self.street = street
        self.place = place
        self.lat = lat
        self.lng = lng
        self.dist = dist
        self.price: float = price
        self.diesel = diesel
        self.e5 = e5
        self.e10 = e10
        self.is_open = isOpen
        self.house_number = houseNumber
        self.post_code = postCode

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nBrand: {self.brand}\nStreet: {self.street}\nPlace: {self.place}\nLatitude: {self.lat}\nLongitude: {self.lng}\nDistance: {self.dist} km\nDiesel Price: {self.diesel} €\nE5 Price: {self.e5} €\nE10 Price: {self.e10} €\nIs Open: {self.is_open}\nHouse Number: {self.house_number}\nPost Code: {self.post_code}"
