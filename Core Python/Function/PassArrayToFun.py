from array import*
def show(ar):
	print(ar)
	print(type(ar))
	for i in ar:
		print(i)
	return ar            # Return an array
a=array('i',[101,102,103,104])
y=show(a)
print(" REturning array Y : ",y)
print(type(y))
for i in y:
	print(i)
