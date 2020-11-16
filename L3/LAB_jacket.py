#!/bin/python3

#Class with jacket description
class jacket:
	def __init__(self):
		#Size of jacket {S, M, L}
		self._size = None
		#Number of pockets
		self._pocketNumber = None
		#How jacket is secured
		self._secureType = None
		#Color of jacket
		self._color = None
		#Material of jacket
		self._material = None

	#Fill values with this function
	def jacketCreation(self, size, pocketNumber, secureType, color, material):
		self._size = size
		self._pocketNumber = pocketNumber
		self._secureType = secureType
		self._color = color
		self._material = material

	#Print info for jacket
	def jacketPrint(self):
		print('JACKET DESC.')
		print('------------')
		print('size		%s' % (self._size))
		print('pockets		%d' % (self._pocketNumber))
		print('type		%s' % (self._secureType))
		print('color		%s' % (self._color))
		print('material		%s' % (self._material))
