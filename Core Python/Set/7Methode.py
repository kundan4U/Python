
# All methode use in [ython of the Matheme=atics Sets

a = {'RAhul','Raj','Sonam','Rani'}
b = {'Sumit','RAhul','Rani','Python','Java'}
print(" A :",a)
print(" B :",b)
print()

# INtersection Methode

ism = a.intersection(b)
print(" After Intersection  :",ism,"\n")

# Union

u = a.union(b)
print(" After Union :",u,"\n")

# Diffrence

d = a.difference(b)
print(" After Diffrence :",d,"\n")

d = b.difference(a)
print(" After Diffrence :",d,"\n")

# Issubset

s = a.issubset(b)
print("After  Subset :",s,"\n")

s = b.issubset(a)
print("After  Subset :",s,"\n")

# SUperset

s = a.issuperset(b)
print("After  Superset :",s,"\n")