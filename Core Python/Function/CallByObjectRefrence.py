def val(x):
	print(x,id(x))
	x=15
	print(x,id(x))
x=10
val(x)
print(x,id(x))



# in the List 


def val(lst):
	lst.append(4)
	print(lst,id(lst))
lst=[1,2,3]
print(" Befor calling function by object",lst,id(lst))
val(lst)
print(" After calling function by object", lst,id(lst))