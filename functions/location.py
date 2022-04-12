class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


bham_academy = Location(52.488647, -1.887249)
print(bham_academy)
print(f"The Sparta Global Birmingham Academy is located at co-ordinates {bham_academy}")