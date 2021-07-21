
a = {'course':'python','fees':15000,1:{'course':'javaScript','fees':100000}}


for i in a:
	if type(a[i]) is dict:
		for k in a[i]:
			print(k,"=",a[i][k])
		else:
			print(i,"=",a[i])