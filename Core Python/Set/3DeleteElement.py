

# Remove : Remove elemet if target element not found then Got An Error
# Discard : Remeove element if tzrget element not found then not raise any error and code run successfully

a={10,20,30,40,"shivani"}
print("Orignel Set ",a)
print(id(a))
print()

a.remove("shivani")
print(" After removing :",a)
print(id(a))

'''a.remove("Kundan")                  # remove got an error because element not found
print(" After removing :",a)
print(id(a))
'''

a.discard("Kundan")                  # Discard methode not any error if any element not folud so
print(" After removing :",a)
print(id(a))