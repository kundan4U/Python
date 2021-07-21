# Input using while Loop
from array import *
stu_roll=array('i',[])
n=int(input("PLease Enter how many Element you want"))
i,j=0,0
while i<n:
	stu_roll.append(int(input("Enter Element")))
	i+=1
while j<n:
	print(stu_roll[j])
	j+=1
print(stu_roll)