#!/usr/bin/python3

t0 = (1, 2, 3, 4)
t1 = (5, 6, 7, 8)

for i in range(len(t0)):
	for j in range(len(t1)):
		print(("%s + %s =" % (t0[i], t1[j])), t0[i] + t1[j])
		print(("%s - %s =" % (t0[i], t1[j])), t0[i] - t1[j])
		print(("%s * %s =" % (t0[i], t1[j])), t0[i] * t1[j])
		print(("%s / %s =" % (t0[i], t1[j])), t0[i] / t1[j])
