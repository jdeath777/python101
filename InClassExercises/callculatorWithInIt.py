class Calculs:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.sum = 0

    def add_num(self):
        self.sum = self.a + self.b
        return self.sum


c1 = Calculs(40, 50)
print("The result are: ", c1.add_num())

