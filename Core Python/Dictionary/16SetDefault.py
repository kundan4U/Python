'''
# setdefault() Methode

 This Methode returns the value of the specified key.
 If any key is not found then it inserts key with the specified values.

 Syntax :- dict_name.setdefault(key,value)
 '''
stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Orignel Dictionary : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")

returned_value = stu.setdefault(109,"Python")

print(" After setdefault Dict ",stu)
print(id(stu),"\n")

print(" Return value is : ",returned_value)
print()