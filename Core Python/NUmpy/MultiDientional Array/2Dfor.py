import numpy 
a=numpy.array([[10,20,30,40,50],[60,70,80,90,100]])
n=len(a)
# without Index
print("********    Without INdex      *******")
for r in a:                                      # Outer loop work for Row
	for c in r:                                  # Inner loop work for column
		print(c)
	print()
# with index
print("************  With Index ***********")
for i in range(n):                                 # Outer loop work for Row
	for j in range(len(a[i])):                     # Inner loop work for column
		print("a","[",i,"]","[",j,"]","=",a[i][j])
	print()
