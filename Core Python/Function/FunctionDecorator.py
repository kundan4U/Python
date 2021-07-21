def decorate(fun):
	def inner():
		print("IF : Before enchancing Function")
		fun()
		print("IF : After Enchancing Function")
	return inner
    
def num():
	print(" WE will use this function")
	print("and will enchance thid is decorator")

result_fun=decorate(num)
result_fun()

print("*****************************   Second Method  *********************************")

# second method
def decor(num):
	def inner():
		print("IF : Before enchancing Function")
		num()
		print("IF : After Enchancing Function")
	return inner
    
def num():
	print(" WE will use this function")
	print("and will enchance thid is decorator")
num = decor(num)
num()

print("*****************************   Third Method  using @decor *********************************")
# Third Method using @decor

def decor(num):
	def inner():
		print("IF : Before enchancing Function")
		num()
		print("IF : After Enchancing Function")
	return inner

@decor    
def num():
	print(" WE will use this function")
	print("and will enchance thid is decorator")
num()


print("*****************************   Real Example of decorate function  *********************************")


def decor(fun):
	def inner():
		a=fun()
		add = a+5
		return add
	return inner

def num():
	return 10

result_fun = decor(num)
print (result_fun())

print("*****************************   SEcond Method  of  Real Example   *********************************")
# Second Methode
def decor(num):
	def inner():
		a=num()
		add = a+5
		return add
	return inner

def num():
	return 10

num = decor(num)
print (num())

print("*****************************   Third Method of  Real Example using @decor *********************************")
# Third Methode
def decor(num):
	def inner():
		a=num()
		add = a+5
		return add
	return inner
@decor
def num():
	return 10

print(num())