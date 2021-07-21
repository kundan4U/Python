# Map Function 

a=[10,20,30,40,50,60]
 
def inc(n):
	return n+25 

result = map(inc,a)   #  inc is the function name and a is the itterable
print(result)
print(type(result))


# now using for loop

for i in  result:
	print(i)


# convert map to list
result = list(map(inc,a))
print(type(result	))  

