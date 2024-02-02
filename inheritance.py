# Single inheritance
class vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost

    def vehicle_details(self):
        print("The Vehicle mileage is",self.mileage)
        print("The vehicle cost is",self.cost)

# v1=vehicle(650,200000)
# v1.vehicle_details()

class Bike(vehicle):
    def show_bike(self):
        print("Bike Model GT650")

b1=Bike(22,200000)
b1.vehicle_details()
b1.show_bike()