'''
This methode rerurns an object tht contain key-value pair of dictionary
The pairs are stored as tuples in the object.

Syntax :- dict_name.items()

Ex:- 

stu.items()
'''

stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Orignel Dictionary : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")


it = stu.items()

print(" it :",it)
print(type(it),"\n")

lst = list(it)
print(lst)
print(type(lst),"\n")

print(lst[0])
print(lst[0][0])
print(lst[0][1],"\n")

for r in lst:
	for c in r:
		print(c)






