a=[10,20,-50,65,'Kundan'] # This is the list
l=len(a)

print("*************** Using For  Nprmal For Loop Without Index************")
for element in a:
	print(element)

print("*************** Using For Loop************")
for i in range(l): # for loop
	print(a[i])
a[2]=" Shivani "
print("*************** Using While Loop  After MOdification on list**********")
i=0
while i<l:
	print(a[i])
	i+=1
print("*************** Accseccing List with negative index**********")
print(a[-5])
print(a[-4])
print(a[-3])
print(a[-2])
print(a[-1])

