def show(s):
	print(s)
	print(type(s))
	print(id(s))
	for i in s:
		print(i)
	return s

st = {10,20,30,40,50,"Shivani"}
new_set = show(st)
print(new_set)
print(type(new_set))