
# Update the dictionary eith the specified key and value pair

stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Orignel Dictionary : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")

stu.update({104:"Shivni"})  # Update the Dictionary for single element

vals = {"name":"KUndan","address":"Azamgarh","Mobile_number":6386616915}
stu.update(vals)


print("After Update Dictionary  is : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")