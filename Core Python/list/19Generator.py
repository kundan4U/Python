def disp(a,b):
	yield a
	yield b

result= disp(10,20)
print(result)
print(type(result))
lst = list(result)
print(lst)
print(type(lst))


print(next(result))