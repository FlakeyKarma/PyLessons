#!/bin/python3

#Class creation
class wool_cloth:
	#Initialization of class object
	def __init__(self, cloth):
		#Self values
		self._cloth_type = cloth
		self.shouldDry = False

	def clean(self):
		#How to go about cleaning cloth
