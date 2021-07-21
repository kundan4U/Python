from numpy import *
n=int(input("Please enter Number of Elements :"))
a=zeros(n, dtype=int)
for i in range(len(a)):
	x=int(input("Enter element"))
	a[i]=x
print(a)