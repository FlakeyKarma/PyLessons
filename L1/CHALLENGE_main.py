#!/usr/bin/python3

list_0 = []
list_1 = []
list_com = [list_0, list_1]
dict = {}

math_func = ["%s - %s", "%s + %s", "%s / %s", "%s * %s"]

for i in range(2):
	print("Enter `end` when you\'re done entering values for the current list.")
	while(True):
		val = input("KEY=List_%d:VAL=" % (i))
		if val.lower() == "end":
			break
		if int(val) in list_com[i]:
			print("%s is already in the list, please try again." % (val))
		else:
			list_com[i].append(int(val))
for j in range(len(list_com[0])):
	for k in range(len(list_com[1])):
			add = list_com[0][j] + list_com[1][k]
			sub = list_com[0][j] - list_com[1][k]
			mult = list_com[0][j] * list_com[1][k]
			div = list_com[0][j] / list_com[1][k]
			dict['%d and %d' % (list_com[0][j], list_com[1][k])] = [add, sub, mult, div]



print("OUTPUT IN ORDER OF: addition, subtraction, multiplication, division")
for key in dict:
	print(key, dict[key])
