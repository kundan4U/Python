

a = {}
n= int(input(" Enter the number of  Element  :"))

for i in range(n):
	k = input("Enter Key     :")
	v = input("Enter Value   : ")
	a.update({k:v})

print(a)