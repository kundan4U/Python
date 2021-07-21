
'''
 get() Methode :-  This methode return the value of the specified key .py
 If key is not found then it will return none or Default values.
 
 Syntax :-   dict.get(key , dafaultvalue)

 Ex :-
  stu.get(104)
  stu.get(104,"Shivani")

'''
stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Orignel Dictionary : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")

g = stu.get(101)
print(g)
print(stu.get(101))   # second methode to wriiten code direct