# # Data types
# # Computers are stupid
# # they don't understand context so we need to be specific with data types
#
# # We can use type() to check datatypes
#
# # Strings
# # lists of characters bundled together in a specific order
# # using index
# print('hello')
# print(type('hello'))
#
# # Concatentation of strings
# string_a = 'hello there'
# name_person = 'Juan Pier'
# print(string_a + ' ' + name_person)
#
# # Useful methods
# # Length
# # Returns the length of a string
# print(len(string_a))
# print(len(name_person))
#
# # Strip
# # Removes trailing or prevailing white spaces
# string_num = ' 90383 '
# print(string_num)
# print(string_num.strip())
#
# # .Split this is a method for strings
# # it splits in a specific location and outputs a list (data type)
# string_text = 'Hello I need to test this'
# split_string = string_text.split(' ')
# print(split_string)
#
# # Capturing user input
# # get user input of first name
# # save user input to variable
# # get user last name and save it to variable
# # join the 2
# # print
#
# user_fname = input('What is your first name? ')
# user_lname = input('What is your last name? ')
# # Concatenation
# user_name = user_fname + ' ' + user_lname
# print('Hello ' + user_name)
# # Interpolation - use f in front of string to add python into the string
# welcome_message = f"Hi {user_name}, you are very welcome!"
# print(welcome_message)

# ctrl + / for mass comment out

# Count/Lower/Upper/Capitalize
text_example = "here is sOMe text wItH  a whole bunch of lots of text, so much text wow"
# Count
print(text_example.count('e'))
print(text_example.upper())
print(text_example.capitalize())
print(text_example.lower())
# Casting


