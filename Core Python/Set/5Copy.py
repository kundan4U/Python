
# Syntax
# new_set_name = set_name.copy()

a={10,20,50,50,60,50,60,60}
print(a)
print(id(a))

new_set = a.copy()

print(" After Copy : ",new_set)
print(id(new_set))