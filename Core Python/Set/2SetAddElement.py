# sets

a={10,20,30,40}
a.add('python')
print(a)


# Adding Multiple Element

b=set()
b.update([101,202,103])
print(b,"\n\n")


c={10,20,30,"Shivani"}
print("Befor adding  :",c)
print(id(c),"\n\n\n")

c.update(([54,97,544,65]))  # Add Multiole Element
print("After adding  :",c)
print(id(c),"\n\n\n")