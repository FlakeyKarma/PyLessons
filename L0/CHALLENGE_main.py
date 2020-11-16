#!/bin/python3

#Current year
year = 2020

#Get first name
first_name = input("first name: ")

#Get last name
last_name = input("last name: ")

#Get age
age = int(input("age: "))

#Make full name
name = first_name + " " + last_name

#Birth year
birth_year = year-age

#Print name
print("Hello there, " + name)
print("And I see you were born in " + str(birth_year) + " too!")
