# replace()
name="kundan chauhan"
old="chauhan"
new=" Singh"
str1=name.replace(old,new)
print(name)
print(str1)

# 2nd methode

name="Kundan Chauhan"
print(name.replace("Chauhan","Singh"))

# split()

name= " Hi Shivani How are you"
print(name)
print(name.split(" "))
name= " Hi-Shivani-How-are-you"
print(name)
print(name.split("-"))

# join()
name=("kundan","chauhan","shivani")
print(name)
print("_".join(name)) # This function is join with the underscore which is your choice what u are to join with which charecter also include Space

#startswith()
n= "Hi how are you"
print(n.startswith("Hi"))

# endswith
s=" Hi you are so good"
print(s.endswith('good'))