from enum import Enum


class SortBy(Enum):
    """
    An enumeration to define sorting criteria for gas stations.

    Attributes:
        distance (str): Enum member for sorting by distance.
        price (str): Enum member for sorting by price.
    """
    distance = "dist"
    price = "price"


class Station:
    """
    A class to represent a gas station.

    This class encapsulates various attributes of a gas station, such as ID, name, brand,
    geographic coordinates, fuel prices, and other relevant information.

    Attributes:
        id (str): The unique identifier for the station.
        name (str): The name of the station.
        brand (str): The brand associated with the station.
        street (str): The street address of the station.
        place (str): The locality or area where the station is located.
        lat (float): The latitude coordinate of the station.
        lng (float): The longitude coordinate of the station.
        dist (float): The distance of the station from a reference point.
        price (float): The price of the primary fuel type at the station.
        diesel (float): The price of diesel at the station.
        e5 (float): The price of E5 fuel at the station.
        e10 (float): The price of E10 fuel at the station.
        is_open (bool): Indicates whether the station is currently open.
        house_number (str): The house number part of the address.
        post_code (str): The postal code of the station's location.
    """

    def __init__(self, id, name, brand, street, place, lat, lng, dist, price=None, diesel=None, e5=None, e10=None, isOpen=True, houseNumber=None, postCode=None):
        """
        Initializes a Station object with given attributes.
        """
        self.id = id
        self.name = name
        self.brand = brand
        self.street = street
        self.place = place
        self.lat = lat
        self.lng = lng
        self.dist = dist
        self.price = price
        self.diesel = diesel
        self.e5 = e5
        self.e10 = e10
        self.is_open = isOpen
        self.house_number = houseNumber
        self.post_code = postCode

    def __str__(self):
        """
        Returns a string representation of the Station object.

        Returns:
            str: A formatted string with all attributes of the Station object.
        """
        return f"ID: {self.id}\nName: {self.name}\nBrand: {self.brand}\nStreet: {self.street}\nPlace: {self.place}\nLatitude: {self.lat}\nLongitude: {self.lng}\nDistance: {self.dist} km\nDiesel Price: {self.diesel} €\nE5 Price: {self.e5} €\nE10 Price: {self.e10} €\nIs Open: {self.is_open}\nHouse Number: {self.house_number}\nPost Code: {self.post_code}"
