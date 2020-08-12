class Car:
    wheels = 4   #class variables
    def __init__(self):
        self.com = 'BMW'  #instance variable
        self.price = 50000

c1 = Car()
c2 = Car()
Car.wheels = 6
c2.com = 'Mercedes'
c2.price = 70000

print(c1.com,c1.price,c1.wheels)
print(c2.com,c2.price,c2.wheels)