# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:05:33 2018

@author: Neetu

Implement class Fraction that supports common fraction methods
"""

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
        


class Fraction:
    
    def __init__(self,num,den):
        if not isinstance(num,int):
            valError = ValueError("{} is not integer".format(num))
            raise valError
        if not isinstance(den,int):
            valError = ValueError("{} is not integer".format(den))
            raise valError
        common = gcd(num,den)
        self.num = num //common
        self.den = den //common
      
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self,otherF):
        numer = self.num * otherF.den + otherF.num * self.den
        denom = self.den * otherF.den
        if (numer == denom):
            return 1
        return Fraction(numer, denom)
    
    def __sub__(self, otherF):
        numer = self.num * otherF.den - otherF.num * self.den
        denom = self.den * otherF.den
        if (numer == denom):
            return 1
        if(numer == 0):
            return 0
        return Fraction(numer, denom)
    
    def __mul__(self,otherF):
        numer = self.num * otherF.num 
        denom = self.den * otherF.den
        return Fraction(numer, denom)
    
    def __truediv__(self,otherF):
        numer = self.num * otherF.den 
        denom = self.den * otherF.num
        if (numer == denom):
            return 1
        return Fraction(numer, denom)
    
    def getNum():
        return self.num
    
    def getDen():
        return self.den
    
#    def __gt__(self,otherF):
        
myFr1 = Fraction(2,3)
myFr2 = Fraction(2,3)

addFr = myFr1 + myFr2
subFr = myFr1 - myFr2
mulFr = myFr1 * myFr2
divFr = myFr1 / myFr2

print("add: {0} sub: {1} mul: {2} div: {3}".format(addFr,subFr,mulFr,divFr))
#print(myFr1)