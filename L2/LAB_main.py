#!/bin/python3

#Class to describe car
class Car:
	def __init__(self, model):
		self._model = model
		self._door = 4
		self._window = 8
		self._wheels = 4
		self._seats = 4
		self.passengerNumber = None

	#Return model name
	def getModel(self):
		return self._model

	#Return door count
	def getDoors(self):
		return self._door

	#Return window count
	def getWindows(self):
		return self._window

	#Return wheel count
	def getWheels(self):
		return self._wheels

	#return seat number
	def getSeats(self):
		return self._seats

CarObj = Car("Xterra 1999")

CarObj.passengerNumber = 3

print('~Car info~')
print('----------')
print('Model		%s' % (CarObj.getModel()))
print('Doors		%d' % (CarObj.getDoors()))
print('Windows		%d' % (CarObj.getWindows()))
print('Wheels		%d' % (CarObj.getWheels()))
print('Seats		%d' % (CarObj.getSeats()))
print('Passengers	%d' % (CarObj.passengerNumber))
