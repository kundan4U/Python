
# Accessing Dictionary using for loop.


stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Orignel Dictionary : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")

print("************* Accessing Dictionary using for loop*********************,\n ")

for k in stu:
	print(k) # This print only key
print()

for k in stu:
	print(stu[k]) # This print only Value
print()

for k in stu:
	print(k," = ",stu[k])


