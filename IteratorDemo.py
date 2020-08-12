
class TopTen:

    def __init__(self):
        self.count =1

    def __iter__(self):
        return self

    def __next__(self):

        if self.count <= 10:
            val = self.count
            self.count += 1
        else:
            raise StopIteration
        return val

value = TopTen()
print(next(value))
for i in value:
    print(i)

