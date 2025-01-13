class Fraction:
    def __init__(self, num, den):
        self.__n = num
        self.__d = den
    
    def getNum(self):
        return self.__n

    def getDen(self):
        return self.__d
    
    def setNum(self, num):
        self.__n = num
    
    def setDen(self, den):
        self.__d = den
        
    def unreduce(self, mul):
        self.setNum(self.getNum() * mul)
        self.setDen(self.getDen() * mul)
    
    def mult(self, g):
        numerator = g.getNum() * self.getNum()
        denominator = g.getDen() * self.getDen()
        newFrac = Fraction(numerator, denominator)
        return newFrac
        
    def __str__(self):
        return "{0}/{1}".format(self.__n, self.__d)

class Fraction2(Fraction): # inherits from Fraction (base class)
    def __init__(self, num, den):
        Fraction.__init__(self, num, den) # Call base class's constructor
    
    def check(self): # checks to see if denominator is 0
        if self.getDen() == 0:
            print("Error: 0 in the denominator")
        else:
            print("Fraction OK")

# Driver code
f1 = Fraction2(3, 4)
f2 = Fraction2(5, 9)
f3 = f1.mult(f2)
print(f1, "+", f2, "=", f3)
f1.check()
f2.check()
f1.unreduce(3)
print(f1)
