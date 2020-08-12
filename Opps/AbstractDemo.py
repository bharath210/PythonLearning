from abc import ABC,abstractmethod

class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

    def show_config(self):
        print("Intel i5")

class Laptop(Computer):

    def process(self):
        print("It's Processing")

lap = Laptop()
lap.process()
lap.show_config()