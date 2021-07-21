'''
SYNTAX

tuple_name = ()
Ex:- a = ()

'''
# ingle elemenrt is define as a Integer if we add comma then its define as a Tuple
 
b=(10)   # Integer
c=(10,)  # Tuple
print(b)
print(type(b))

print(c)
print(type(c))

d = (10,20,30)
e = (10,20,30,40,'KUNDAN')
f = 10,20,30,40,50,'SHIVANI'  # without parenthisis it also is a Tuple its by default

print(" Without parenthis",type(f))

print(e[0])
print(e[1])
print(e[2])
print(e[3])
print(e[4],"\n\n")

print("****************        Using For loop  **************************************************\n\n")

x=( 10,20,50,60,80,'Shivani')

print(" ***************** Withiut index  ******************\n")
for i in x:
	print(i)

print("********** With index  index ************************  \n")

y=len(x)
for i in range(y):
	print("X","[",i,"] = ",x[i])


print("****************        Using While loop  **************************************************\n\n")

i=0
while i<y:
	print("X","[",i,"] = ",x[i])
	i+=1
