class Computer:
    def config(self):
        print("I5 , 16GB , 1TB ")

com1 = Computer()
com2 = Computer()
print(type(com1))

Computer.config(com1)
com2.config()

a = 5
a.conjugate()