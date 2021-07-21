# Insert Function = Insert in particuler Position
a=[2,5,8,6,7,2,3,2]
print("Befor Insert :",a)
a.insert(3,'Kundan')
print("After Insertion :",a)

# Pop( )   Remove list last element
a.pop()
print("After Pop :",a)

# Remove()      FIrtst Accurence of the List
a.remove(5)
print("After Remove :",a)

# index()   Return fisrt occurence of given element in the list
n=a.index('Kundan')
print("After Index get :",n)

# REverse() This function reverse the List
a.reverse()
print(" After Reverse : ",a)

# Exted()          THis method append nother List

s=[2,5,3,8,3]
t=['Shivani',"jnp",]
print("List s :",s)
print("List t :",t)
s.extend(t)
print("After Extend List ",s) 

# Count() This Methode Return the occurence if the specified element in the list
num=a.count(2)
print("Totl 2 in the list is :",num)

#Sort() This methode is use to short in Accending Order

m=[2,85,6,45,32,85,12,65,86,14]
print("LIst  Befor Sort :",m)
m.sort()
print("After  Befor Sort :",m)


# Clear()  This methide is clear the list
p=[85,52,1,54,1,2,5,4,1,2,5,78,4,2,5]
print("  List Before cler :",p)
p.clear()
print(" After Before cler :",p)
