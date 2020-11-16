#!/bin/python3

class Car:
	def __init__(self, name=None):
		self.name = name
		self.color = None
		self.company = None

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color

	def setCompany(self, company):
		self.company = company

	def getCompany(self):
		return self.companty

	def setName(self, name):
		self.name = name

	def getName(self):
		return self.name


