import  array as ar
roll_num=ar.array('i',[1,2,5,8,65,47])
n=len(roll_num)
i=0
while i<n:
	print(roll_num[i])
	i+=1
print("Array after Append")
roll_num.append(500)
roll_num.append(2558)
n=len(roll_num)
i=0
while i<n:
	print(roll_num[i])
	i+=1

