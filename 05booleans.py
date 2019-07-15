# booleans
# booleans is a data type that is either true or false

# Syntax is a capital letter
var_true = True
var_false = False
# Proof of type boolean
print(type(var_true), type(var_false))

# When we equate/evaluate something we get a boolean as a response
# All logical operators can apply
# == / != / < / > / <= / >=
weather = 'Rainy'
print(weather == 'Sunny')
print(weather == 'Rainy')

# Logical AND & OR
# Evaluate 2 sides and BOTH have to be true for it to return True
print('> Testing logical and: ')
print(weather == 'Rainy' and weather == 'Sunny')
print(True and False)
print(weather == 'Rainy' and weather == 'Rainy')
print(True and True)

# Logical OR - One of the side of the equations has to be true to return True
print('>Testing logical or:')
print(weather == 'Rainy' or weather == 'Sunny')
print(True or True)

# Some methods/functions can return booleans
potential_number = '10'
print(potential_number.isnumeric())
print(float(potential_number).is_integer())

text = 'Hello World!'
print(text.startswith('H'))
print(text.startswith('h'))
print(text.endswith('!'))

# Booleans and numbers
print('Printing bool values of numbers')
print(bool(0))
print(bool(7))
print(bool(''))

# Value of none
print(bool(None))
