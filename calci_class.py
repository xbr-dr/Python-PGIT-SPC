class Calci:
    """This is a basic example of calculator made using class"""
    def __init__(self, p, q):
        self.a = p
        self.b = q

    def add(self):
        print("the sum of two numbers is:", self.a + self.b)

    def sub(self):
        print("the diff. of two numbers is:", self.a - self.b)

    def multi(self):
        print("the prod. of two numbers is:", self.a * self.b)

    def div(self):
        print("the quot. of two numbers is:", self.a / self.b)

    def rem(self):
        print("the remainder of two nos. is:", self.a % self.b)


# for an object to be made we need following command
c1 = Calci(200, 20)
c1.div()
c1.multi()
c1.sub()
c1.add()
c1.rem()
