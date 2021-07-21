from numpy import *
m=int(input(" ENter of Rowa : "))
n=int(input(" ENter of Column : "))
a=zeros((m,n),dtype=int)
print(a)
u=len(a)
for i in range(u):
	for j in range(len(a[i])):
		x = int(input(" Enter Element :"))
		a[i][j] = x
print(a)
