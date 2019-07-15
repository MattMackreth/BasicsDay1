# This is where I will do my exercise
# Filipe told me to pseudo code first

# Get user first name
# save to variable
user_first_name = input('What is your first name? ').capitalize()
print('Nice to meet you ' + user_first_name)

# Get user funny fact
# save to variable
user_funny_fact = input('Tell me a funny fact: ')
print('Hahaha, that is very funny!')

# Get most important date
# Save to another variable
print('What is your most important date? ')
user_day = input('First give me the day in numerical form (eg. 1 for the first): ')
user_month = input('Then the month: ')
user_year = input('Finally the year: ')
user_date = user_day + '-' + user_month + '-' + user_year

# Get reason for most important date
# Save to another variable
user_date_reason = input('Why is this your most important date? ')

# Get favourite pokemon
# Save to another variable
user_pokemon = input('What is your favourite pokemon? ').capitalize()
# Print out information nicely
print(f'Your name is {user_first_name} '
      f'\nYour fun fact is {user_funny_fact} '
      f'\nYour most important date is {user_date} because {user_date_reason}'
      f'\nYour favourite pokemon is {user_pokemon}')


user_num = int(input('Give me a number: '))
print('Your number multiplied by the answer to life the universe and everything is ', user_num * 42)
