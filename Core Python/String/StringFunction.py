name=" kundan chauhan"
print(name)
print(name.upper()) # Upper function

name=" KUNDAN CHAUHAN"
print(name)
print(name.lower())

print(name.swapcase()) # swapcase change small to Capital and Capital to small

name=" Hi kundan chauhan how are you"
print(name.title())

# Second methode
name=" Hi kundan chauhan how are you"
a=name.title()
print(a)

# isupper()
name=" kundan chauhan"
print(name.isupper())
name=" KUNDAN CHAUHAN"
print(name.isupper())

# istitle()

name="Kundan Chauhan"
print(name.istitle())

# isdigit()
name="35413545"
print(name.isdigit())

name="354jh13545"
print(name.isdigit())

# isalpha
n="jbjd354d58"
print(n.isalpha())

# isalnum()
str="dd24565"
print(str.isalpha())

# isspace()
name=" "
print(name.isspace())

# lstrip()
name=" Kundan Chauhan"
print(name)
print(name.lstrip()) # remove left side space

# rstrip()
name =" Kundan chauhan   "
print(name)
print(name.rstrip()) # remove Right side space

# strip()
name="  Kundan Chauhan   "
print(name)
print(name.strip())