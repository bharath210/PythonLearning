class Studernt:
    school = "Hyderabad Public School"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avgMarks(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,marks):
        self.m1 = marks
    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print('Its a Student class')

s1 = Studernt(45,98,76)
s2 = Studernt(75,87,87)

print(s1.avgMarks())
print(s2.avgMarks())
print(Studernt.school)

print(s2.get_m1())
s2.set_m1(55)
print(s2.avgMarks())
print(Studernt.getSchool())
Studernt.info()