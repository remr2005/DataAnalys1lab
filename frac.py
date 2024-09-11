from math import gcd

class Frac:
    numerator = 0
    denominator = 0
    def __init__(self, a: int, b: int):
        self.numerator = a
        if b == 0:
            return ZeroDivisionError
        self.denominator = b
        self.remove_minus()
        self.reduction()
        pass
    def print_me(self):
        print(f"{self.numerator}/{self.denominator}")
    def sum(self, a):
        self.numerator = self.numerator*a.denominator + a.numerator*self.denominator
        self.denominator *= a.denominator
        self.remove_minus()
        self.reduction()
    def multiply(self, a):
        self.numerator*=a.numerator
        self.denominator*=a.denominator
        self.remove_minus()
        self.reduction()
    def remove_minus(self):
        if (self.numerator < 0 and self.denominator < 0) or self.denominator<0:
            self.numerator*=-1
            self.denominator*=-1
    def obrash(self):
        return self.numerator/self.denominator
    def reduction(self):
        a = gcd(self.numerator,self.denominator)
        while a != 1:
            self.numerator//=a
            self.denominator//=a
            a = gcd(self.numerator,self.denominator)

