class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        st = Student(m1, m2)
        return st

    def __gt__(self, other):
        s = self.m1 + self.m2
        o = other.m1 + other.m2
        if s > o:
            return True
        else:
            return False

    def __str__(self):
        return f'{self.m1} {self.m2}'


s1 = Student(76, 86)
s2 = Student(60, 89)

s3 = s1 + s2
print(s3.m1)
print(s3)

if s1 > s2:
    print("S1 has more Marks")
else:
    print("S2 has more marks")

