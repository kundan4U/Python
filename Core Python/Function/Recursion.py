i=0                               # Gloable VAriable
def myfun():
	global i                    #    Globle keyword
	print(" Hello KUndan : " ,i)
	i=i+1    
	myfun()                       # Recursion
myfun()