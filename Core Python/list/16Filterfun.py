a=[10,20,30,50,60,58,60,50,60,50,80,40,20,5,4,5]


def high_marks(n):
	if n>=60:
		return True

'''
lambda n : (n>=60)             it replace function

'''

result=filter(high_marks,a)   # here resulrt veriable only for that function is the return
print(result)
print(type(result)) 

for i in result:
	print(i)
