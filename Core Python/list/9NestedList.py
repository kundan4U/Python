''' 
NEsted List
A list within another list is called as Nested List or Nesting of a List
Ex :-
 a=[5,65,68,15,[25,12,4,25,7]]
 b=[[2,5,4,2,],[8,6,4,5,8]] 
 c=b[ 
     [2,5,4,2,],
     [8,6,4,5,8]] 
'''

a=[5,65,68,[25,12]]
print(a)

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[3][0])
print(a[3][1])


print("Before Modification : ",a)
a[1]='shivani'
a[3][0]='Jnp'
print("After Modification : ",a,"\n\n\n")


print("***********************************************************************************************************\n")

c=[50,60]
d=[6,21,65,658,c]
print(" C is : ",c)
print(" D is : ",d,"\n")

print("***********************************************************************************************************\n")

p=[[2,3,4],[5,6,7]]
print(" P is : ",p)
print("First Row of P is :" ,p[0])
print("Second Row of P is :" ,p[1],"\n")

print(p[0][0])
print(p[0][1])
print(p[0][2])
print(p[1][0])
print(p[1][1])
print(p[1][2])







































