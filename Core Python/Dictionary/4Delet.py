# delete item or dictionary using Dell Statement

stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Before Delete: ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")

del stu[102]      # Delete the element of the dictionary

print(" After   Delete  one element: ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")



del stu  # Delete whole Dictionary

print(stu)	# Now the Dictionary Delete and its time they not show
