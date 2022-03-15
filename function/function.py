"""function_name()
execute function before declaration will be error
"""


# Function without parameter
def function_name(): 
  print("Hello wolrd")
  print("Welcome to first your function")
  
  
# Function with parameter
def function_params(name):
  print(f"Hello {name}"}
  
  
# Function with keyword arguments
def key_args(first_name, last_name):
  print(f"{fisrt_name} {last_name}")
  
  
# Return Statement on function
def square(number):
  return number * number


print("start")
# function_name()
function_params("Dimas") # this is value of parameter (arguments)
key_args(first_name="Dimas", last_name="Saputra") # keyword arguments
square(3)
print("finish")