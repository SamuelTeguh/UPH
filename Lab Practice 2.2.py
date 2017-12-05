import random

x = []
for i in range(100):
	x.append(randint(1,100))
	print(str(x[i]), end=' ', flush=True)

y= sorted(x)
z= sorted(x,reverse=True)

print ('\n'+"ascending")

for i in range(len(y)) :
	print(str(y[i]), end=' ',flush=True)

print('\n'+"descending")
for i in range(len(y)) :
	print (str(z[i]), end=' ', flush=True)
print('\n')
