
class Student:
    def __init__(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop('Asus', 'VivoBook')

    def showStudent(self):
        print(self.rollNo,self.name)

    class Laptop:
        def __init__(self,brand,model):
            self.brand = brand
            self.model = model

        def showLaptop(self):
            print(self.brand,self.model)


s1 = Student('Arya Stark',1)
s2 = Student('Sansa Stark',2)
s1.showStudent()
s2.showStudent()

lap1 = Student.Laptop('Hp','NoteBook')

lap1.showLaptop()

lap2  = s2.lap
lap2.showLaptop()

print(lap1.brand)