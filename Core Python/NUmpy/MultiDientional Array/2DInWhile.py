from numpy import *
m=int(input(" ENter of Rowa : "))
n=int(input(" ENter of Column : "))
a=zeros((m,n),dtype=int)
print(a)
u=len(a)
i=0
while i<u:
	j=0
	while j<len(a[i]):
		x=int(input(" Enter Element :"))
		a[i][j]=x
		j+=1
	i+=1
print(a)