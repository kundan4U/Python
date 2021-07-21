'''
 # Dictionary pop() Methode
use to remove the item with specified key.
It return the removed items Value.
If key is not found then the a default value is returned
If key is not found and default value is not given then shows KeyError.

Syntax :-  dict_name.pop(key,defaultvalue)

Ex :- 
stu.pop(101)
stu.pop(101,"www")                here www is the default vlue
'''

stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Orignel Dictionary : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")

removed_value = stu.pop(102)

print(" After pop the remain dictionary is : " ,stu)
print(id(stu),'\n')

print(" rEmoved Valued Is : ",removed_value)


