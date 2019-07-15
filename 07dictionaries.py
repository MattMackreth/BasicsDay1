# Dictionaries AKA Hashes
# Work with key: value pairs. As opposed to using indexes

# Declaring a hash/ dictionary
pika = {}
# Dictionaries work with keys: values
pika = {
    'name': 'Derek Danger',
    'pokemon': 'Pikachu',
    'age': 17,
    'personality': 'Grumpy'
}
print(pika)

# Access information using the keys
print(pika['age'])
print(pika['pokemon'])

# Re-assign values using the keys
pika['age'] += 1
print(pika['age'])

# Adding a key: value pair
pika['colour'] = 'Yellow'
print(pika)

# Creating key value for first and last name
full_name = pika['name'].split()
print(full_name)
first_name = full_name[0]
pika['first_name'] = first_name
pika['last_name'] = full_name[1]
print(pika)

# Embedded data
pika = {
    'name': 'Derek Danger',
    'pokemon': 'Pikachu',
    'age': 17,
    'personality': ['Grumpy', 'Jumpy', 'Angry', 'Shocked', 'Static']
}
print(pika['personality'][2])

# Important Methods
print(pika.keys())
# Outputs an array of keys

values = pika.values()
print(values)

