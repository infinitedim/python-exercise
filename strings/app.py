# String on python

# double and single quotes
'''
wrong_string_1 = 'Python's for Beginners'
correct_string_1 = "Python's for Beginners"
'''

'''
wrong_string_2 = "Python for "Beginners"."
correct_string_2 = 'Python for "Beginners"'
'''
# triple quote
# triple quote can be a comment like a hastag symbols

hii = '''
Hii, My name is Dimas
this is my first python program
and this text created using triple quote
nice to meet you, see u again
'''


# square brackets
'''
square brackets can be use to search indexes value of string
in python, indexes start from 0
you can input indexes value by negative like -1
and python will be print last one character of the string

colon symbols ( : )
colon symbols use for print string all selected index
exclude last character

'''

# square brackets example
'''
course = "Python's for Beginners"
print(course[0])

# colon example
print(course[0:-1]) # will be print ython's for Beginner

name = "John doe"
print(name[2:-2]) # will be print hn d
'''

'''
# concat string

first = 'John'
last = 'Doe'

messege = first + ' ['+ last +'] is a coder'

print(messege)


# formatted string
msg = f'{ first } [{ last }] is a coder'

print(msg)
'''

#### Build in function for string ####
# len() - for calculate indexes on string 
# example
course = "Python's for Beginners"

print(len(course)) # will be print 22

# more example for build in function string

print(course.upper()) # uppercase character
print(course.lower()) # lowercade character
print(course.find('B')) # for print indexes of character
print(course.replace('Beginners', 'Absolutely Beginners')) # for replace old string to new string
