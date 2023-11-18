class Station:
    def __init__(self, id, name, brand, street, place, lat, lng, dist, diesel, e5, e10, is_open, house_number, post_code):
        self.id = id
        self.name = name
        self.brand = brand
        self.street = street
        self.place = place
        self.lat = lat
        self.lng = lng
        self.dist = dist
        self.diesel = diesel
        self.e5 = e5
        self.e10 = e10
        self.isOpen = is_open
        self.houseNumber = house_number
        self.postCode = post_code

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nBrand: {self.brand}\nStreet: {self.street}\nPlace: {self.place}\nLatitude: {self.lat}\nLongitude: {self.lng}\nDistance: {self.dist} km\nDiesel Price: {self.diesel} €\nE5 Price: {self.e5} €\nE10 Price: {self.e10} €\nIs Open: {self.isOpen}\nHouse Number: {self.houseNumber}\nPost Code: {self.postCode}"
