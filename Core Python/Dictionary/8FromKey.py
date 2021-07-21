'''

Is use to create a new Dictionary with the specifing key and values.
Syntax :-
  
  dict.fromkeys(key,value)
Ex :-

    key = (101,102,103)
    value = "shivani"
    new_stu = dict.fromkeys(key,value)
'''

key = (101,102,103)
value = "shivani"     # If we not provide value the its take default value  =  None

new_stu = dict.fromkeys(key,value)

print(new_stu)
