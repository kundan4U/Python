from time import *
str="Kundan"
l=len(str)  # len()  for Obtined String Length
print(l)
print(str[4])

for i in str: # Using for Loop
	print(i)
	sleep(2) # sleep function for dealy 
i=0
while i<len(str): #  Using While Loop 
	print(str[i])
	i+=1