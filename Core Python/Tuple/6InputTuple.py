# GEtting Input from User - Tuple

a=[]

n=int(input(" Enter Number of Element"))

for i in range(n):
	a.append(int(input(" Enter the Element :")))

print(type(a))
print(a)      # Now it print in form of List
a=tuple(a)
print(type(a))

print(a) #      # Now it print in form of Tuple
