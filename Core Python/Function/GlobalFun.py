a=5000
def show():
	a=10000
	print("Local Variable A : ",a)
	x=globals()['a']
	print( " X is :",x)
show()
print(" global Varialle A : ",a)