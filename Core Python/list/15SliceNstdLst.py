# Slicing the Nested List
x=[[10,20,30],
	[40,50,60],
	[70,80,90],
	[50,60,40],
	[51,51,84],
	[65,48,24],
	[32,64,35],
	[32,62,95],]
print("Orignel List ")
print(x,"\n")

print(" From 1st to 4th position")
a=x[1:5]
print(a,"\n")

print(" From 0th to last position")
b=x[0:]
print(b,"\n")

print(" From 0th to 4th position")
c=x[:5]
print(c,"\n")

print(" From nested list 0th to 4 of 1st position")
d=x[0:5]
print(d)
d=x[0:5][2]
print(d,'\n')

print(" From nested list 0th to 6th of 2nd to 4th position")
d=x[0:6]
print(d)
d=x[0:6][2:5]
print(d,'\n')