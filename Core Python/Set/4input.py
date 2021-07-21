a=set()
print(type(a))
print(id(a),"\n\n\n")

n=int(input("Enter the Element :"))

for i in range(n):
	e=input(" Enter the Element ")
	a.add(e)

for i in a:
	print(i)