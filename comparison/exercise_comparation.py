'''
if name is less than 3 characters 
  name must be at least 3 characters long
otherwise if name greater than 50 characters
  name can be a maximum 50 characters long
otherwise
  name looks good
'''


name = input("Input your name here: ")

if len(name) < 3:
  print("name must be at least 3 characters long")
elif len(name) > 50:
  print("name can be a maximum 50 characters long")
else:
  print(f"{name} is a good name")