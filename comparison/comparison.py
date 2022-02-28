# case
'''
if temperature greater than 30
  is a hot day
otherwise if temperature less than 10
  is a cold day
otherwise 
  is netheir not cold or hot day
  
'''

# greater & less operator 

temperature = 30

if temperature > 30:
  print("is a hot day")
elif temperature < 10:
  print("is a cold day")
else:
  print("is a lovely day")
  
# greater equals & less equals operator
if temperature >= 30:
  print("is a hot day")
elif temperature <= 10:
  print("is a cold day")
else:
  print("is a lovely day")
  
# not equals and equality operator

is_a_good_day = True

if is_a_good_day != True:
  print("is a bad day")
elif is_a_good_day == True:
  print("is a good day")