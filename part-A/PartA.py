class House:
    houseNo = 123
    street = "Long Street"
    area = "D15"
    noOfBeds = 2
    price = 250000

    def setHouseNo(self, houseNo):
        self.houseNo = int(houseNo)

    def setStreet(self, street):
        self.street = street

    def setArea(self, area):
        self.area = area

    def setNoOfBeds(self, noOfBeds):
        self.noOfBeds = int(noOfBeds)

    def setPrice(self, price):
        self.price = int(price)

    def __str__(self):
        return (str(self.houseNo) + ", " + self.street + ", " + self.area + ", " + str(self.noOfBeds) + ", " + str(
            self.price))

class Apartment(House):
    floor = 4
    hasBalcony = False

    def __str__(self):
        return super().__str__() + ", " + str(self.floor) + ", " + str(self.hasBalcony)

    def setFloor(self, floor):
        self.floor = int(floor)

    def setHasBalcony(self, hasBalcony):
        self.hasBalcony = bool(hasBalcony)


house = House()
apartment = Apartment()

print("--- House ---")
print(house)

print("--- Apartment ---")
print(apartment)

house.setHouseNo(456)
house.setStreet("Small Street")
apartment.setHouseNo(789)
apartment.setHasBalcony(True)

print("\n--- After Editing Attributes ---")
print("--- House ---")
print(house)

print("--- Apartment ---")
print(apartment)

