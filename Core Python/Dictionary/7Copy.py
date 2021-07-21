'''
USe to copy all element from the exiting dictionary into a new dictionary.
Synatx :- 

    dict.copy()
Ex :- 
      new_stu = stu.copy()
'''

stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Orignel Dictionary : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")

new_stu = stu.copy()

print(" Copied Dictionary : ")
print(new_stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")