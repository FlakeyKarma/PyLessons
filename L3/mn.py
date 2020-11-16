#!/bin/python3
from res import Car

#Create Car object
C = Car("Xterra")
C.setColor("Red")
C.setCompany("Nissan")


print("The car name is", C.name)
print("The car color is %s" % (C.color))
print("The manufacturer is " + C.company)
