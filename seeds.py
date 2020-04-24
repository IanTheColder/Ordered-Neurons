from random import randint

with open('seeds','w') as f:
	l = []
	for i in range(4):
		l.append(randint(1,2000))
	f.write(str(l))
