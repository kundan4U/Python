#10AccsessNestedListUsingForLoop.py


a=[10,20,30,[40,50]]
print(type(a))
n=len(a)

for i in range(n):
	if type(a[i]) is list:
		if len(a[i])>1:
			m=len(a[i])
			for j in range(m):
				print(i,j,a[i][j])
	else:
		print(i,a[i])


# Nested list for loop print wothout index

b=[[10,20,30],[40,50,60]]
print(b)
print(type(b))

for r in b: 
	for c in r:
		print(c)
	print()

# with index for loop

n=len(b)
for i in range(n):
	for j in range(len(b[i])):
		print(i,j,b[i][j])
	print()