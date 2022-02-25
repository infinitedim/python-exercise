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

course = "Python's for Beginners"
print(course[0])

# colon example
print(course[0:-1]) # will be print ython's for Beginner

name = "John doe"
print(name[2:-2]) # will be print hn d