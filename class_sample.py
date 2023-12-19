class Spc:
    """this is a simple class sample of SP college"""
    def __init__(self):
        self.name = "S.P. College"
        self.address = "M.A. road Srinagar"
        self.pin = 190001

    def display(self):
        print(self.name, self.address)
        print(self.pin)


t1 = Spc()
t1.display()
