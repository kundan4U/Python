
# Nested Dictionary
# Empty NEsted dictionary
z={
	1:{},
	2:{},
	3:{}
}


# Access Element

a = {'course':'python','fees':15000,1:{'course':'javaScript','fees':100000}}

print(a['course'])
print(a[1])
print(a[1]['fees'],"\n")

# Modifi Element
print("Before Modifieng",a)
a['course']= 'Machine Learning'

print(" After modife ",a)