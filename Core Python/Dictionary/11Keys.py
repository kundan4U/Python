
'''
THis methode returns all the keys
'''
stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Orignel Dictionary : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")




all_keys = stu.keys()      # Keys Syntax

print(all_keys)
print(type(all_keys),"\n")

key_lst = list(all_keys)   # key dictionary convert into the List

print(key_lst[0])
print(key_lst[1])
print(key_lst[2] ,"\n")


for element in key_lst:  # print all key using the for loop
	print(element)