class Bike:
    def __init__(self,brand,type):
        self.brand = brand
        self.type = type
    def showBike(self):
        print("Bike company is {} and Bike type is {}".format(self.brand,self.type))

b1 = Bike('Triump','ADV')
b2 = Bike('BMW','Super Sports')
b1.showBike()
b2.showBike()