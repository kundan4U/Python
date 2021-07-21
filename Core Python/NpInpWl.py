from numpy import *
n=int(input("Please enter Number of Elements :"))
a=zeros(n, dtype=int)
u=len(a)
i=0
j=0
while i<u:
	x=int(input(" ENter Element :"))
	a[i]=x
	i +=1	
while j<u:
	print(a[j])
	j +=1