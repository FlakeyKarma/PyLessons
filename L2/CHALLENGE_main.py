#!/bin/python3

#Class to describe car
class Car:
	def __init__(self):
		self._model = None
		self._door = None
		self._window = None
		self._wheels = None
		self._seats = None
		self.passengerNumber = None

	#Return model name
	def getModel(self):
		return self._model

	#Set model name
	def setModel(self, model):
		self._model = model

	#Return door count
	def getDoors(self):
		return self._door

	#Set door count
	def setDoors(self, door):
		self._door = door

	#Return window count
	def getWindows(self):
		return self._window

	#Set window count
	def setWindows(self, window):
		self._window = window

	#Return wheel count
	def getWheels(self):
		return self._wheels

	#Set wheel count
	def setWheels(self, wheel):
		self._wheels = wheel

	#return seat number
	def getSeats(self):
		return self._seats

	#Set seat number
	def setSeats(self, seats):
		self._seats = seats

CarObj = Car()

CarObj.setModel("Xterra 1999")
CarObj.setDoors(4)
CarObj.setWindows(8)
CarObj.setWheels(4)
CarObj.setSeats(4)

CarObj.passengerNumber = 3

print('~Car info~')
print('----------')
print('Model		%s' % (CarObj.getModel()))
print('Doors		%d' % (CarObj.getDoors()))
print('Windows		%d' % (CarObj.getWindows()))
print('Wheels		%d' % (CarObj.getWheels()))
print('Seats		%d' % (CarObj.getSeats()))
print('Passengers	%d' % (CarObj.passengerNumber))
