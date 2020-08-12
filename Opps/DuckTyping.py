class PyCharm:
    def execute(self):
        print('Compiling')
        print('Debugging')
        print('Running')


class Eclipse:
    def execute(self):
        print('Compiling')
        print('Editing')


class Laptop:
    def show_ide(self, ide):
        ide.execute()


lap1 = Laptop()
pyc = PyCharm()
ecl = Eclipse()
lap1.show_ide(pyc)
lap1.show_ide(ecl)
