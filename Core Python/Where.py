from numpy import *
a=array([10,20,30,100,50])
b=array([12,50,80,40,90])
result=where(a>b,a,b)
print(result)  