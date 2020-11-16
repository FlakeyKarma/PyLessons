#!/bin/python3

#Make file
class F_MK:
	def __init__(self, fp=None):
		self.filepath = fp

	def makeFil(self):
		FIL = open("file.txt", 'w')
		FIL.close()

#Write to file
class F_IN:
	def __init__(self, fp=None):
		self.filepath = fp

	def writeTo(self, txt):
		with open("file.txt", "a") as FIL:
			FIL.write(txt)

#Read from file
class F_OT:
	def __inti__(self, fp=None):
		self.filepath = fp

	def readFil(self):
		print("Some of My Favorite Cars")
		print("------------------------")
		with open("file.txt", 'r') as FIL:
			print(FIL.read())
