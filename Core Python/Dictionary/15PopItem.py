
# it use remove lat inserted item in the dictionsry
# LIFO

stu = {101:"Rahul" , 102:"Raj", 103:"Sonam"}
print(" Orignel Dictionary : ")
print(stu)
print(" Type :",type(stu))
print("Memory Location :",id(stu),"\n")

removed_item = stu.popitem()
print(" After PopItem Methode  dictionary is : " ,stu)
print(id(stu),'\n')

print(" Removed Valued Is : ",removed_item)
