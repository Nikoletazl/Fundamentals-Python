class Vehicle:
    def __init__(self, vehicle_type, model, price):
        self.owner = None
        self.vehicle_type = vehicle_type
        self.model = model
        self.price = price

    def buy(self, money, buyer):
        if self.price > money:
            return "Sorry, not enough money"
        elif self.owner is not None:
            return "Car already sold"
        else:
            self.owner = buyer
            change = money - self.price

            return f"Successfully bought a {self.vehicle_type}. Change: {change:.2f}"

    def sell(self):
        if self.owner is None:
            return "Vehicle has no owner"

        self.owner = None

    def __repr__(self):
        if self.owner is not None:
            return f"{self.model} {self.vehicle_type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.vehicle_type} is on sale: {self.price}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)

