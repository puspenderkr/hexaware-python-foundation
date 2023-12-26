class Location:
    def __init__(self, locationID, locationName, address):
        self.locationID = locationID
        self.locationName = locationName
        self.address = address

    def __str__(self):
        return f"Location ID: {self.locationID}, Name: {self.locationName}, Address: {self.address}"
