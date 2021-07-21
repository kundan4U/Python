from numpy import *
a=array([[12,25,23],
	     [24,54,68], 
	     [21,85,58]])
print(" Orignel Array")
print(a)

print( " o row all column")
n= a[1, :]
print(n)

print( " All row all 0 column")
n=a[:,0]
print(n)
for i in n:
	print(i)

print(" 0 to 2 row and 0 to 2 column")
n=a[0:2 , 0:2]
print(n)

