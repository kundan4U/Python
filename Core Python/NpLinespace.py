from numpy import*
a=linspace(1,8,5000)
n=len(a)
for i in range(n): # with index
	print("Index NO  ",i," = ","Element is " ,"(",a[i],")")
for element in a: # Without index
	print(element)
