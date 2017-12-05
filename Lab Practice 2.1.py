def evenOdd(x):
	return x%2

y = int(input("Input integer: "))

if evenOdd(y) == 1:
	print(y,"is odd number")
else:
	print(y,"is even number")
