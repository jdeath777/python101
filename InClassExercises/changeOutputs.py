class calculs:
    a = 100
    b = 200

    def change(self,a,b):
        print("The global value before change, a: ",self.a)
        print("The global value before change, b: ", self.b)
        self.a = a
        self.b = b
        return self.a + self.b

c1 = calculs()

print("The global value after change, a: ", c1.change(1, 2))
