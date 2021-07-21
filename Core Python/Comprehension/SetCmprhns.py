set1 = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
new_set1 = set()  # This is for Epty set

for i in set1:
	new_set1.add(i+1)

print(new_set1)
print(type(new_set1))



# With Set omprehension

set2 = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19}
new_set2 = {i+1 for i in set2}
print(new_set2)
print(type(new_set2))