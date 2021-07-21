def add():
	x=10
	y=20
	c=x+y
	return c
sum=add()     #  return is the  calling function and we take print this 
print(sum) 


# not returnable
def add():
	x=10
	y=40
	c=x+y
	print(c)
add()        # it call on the function call 