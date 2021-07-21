'''
THis methode returns all the Values

'''

stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Orignel Dictionary : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")

all_values = stu.values()

print(all_values)
print(type(all_values),"\n")

 
value_list = list(all_values)   # Convert ditionary imnto the List for accessing the element
print(value_list)
print(type(value_list),"\n")

for element in value_list:        # print all the values using the for loop ,,We can also accsess using the Index value 
	print(element)