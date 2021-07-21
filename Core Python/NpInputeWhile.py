from numpy import *
n=int(input("Please enter Number of Elements :"))
a=zeros(n, dtype=int)
i=0
while i<len(a):
	x=int(input(" ENter Element :"))
	a[i]=x
	i +=1	
print(a)