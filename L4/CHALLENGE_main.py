#!/bin/python3
from CHALLENGE_resources import F_MK,F_IN,F_OT

#Create file
make = F_MK()
make.filepath = "./"
make.makeFil()

#Write to file
while(True):
	write = F_IN()
	write.filepath = "./"
	txt = input("One of your favorite cars> ")
	if txt == "END":
		break
	else:
		write.writeTo(txt + '\n')

#Read from file
read = F_OT()
read.filepath = "./"
read.readFil()
