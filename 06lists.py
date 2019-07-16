# Lists and dictionaries
# List aka: array

# Sometimes we just need to list our pokemons
# This is how you make a list
# [items go in here, seperated using commas]
pokemons = ['Pikachu', 'Snorlax', 'Mewtwo']
# declaring a list of type string
print(pokemons)
print(len(pokemons))
print(pokemons[0])
print(pokemons[1])

# If you want to print the last in a list you have 2 options
# either array[len(array) - 1]
print(pokemons[len(pokemons) - 1])
# or array[-1]
print(pokemons[-1])

# We need to evolve Mewtwo to Mewthree
# Re-assigning the value in a list using the index

print(pokemons)
pokemons[2] = 'Mewthree'
print(pokemons)

# Appending a new pokemon
# We caught a Piedgeotto
pokemons.append('Pidgeotto')
print(pokemons)
pokemons.insert(0, 'Rattata')
print(pokemons)
print(pokemons.pop())
print(pokemons)
print(pokemons.pop(0))
print(pokemons)

# Removing using a filter
pokemons.remove('Snorlax')
# Remove a specific index
print(pokemons)

# Lists can have any datatypes
mixed_list = ['Jones', 10, 42, 'John']
print(type(mixed_list[0]), type(mixed_list[1]))

# Inception list
leo_d = ['first', 2, ['leo', 'd']]
print(leo_d[1])
print(leo_d[2])
print(leo_d[2][1])

sub_array = leo_d[2]
print(sub_array[1])
# All of this is the same as
print(leo_d[2][1])

# Tuples
# Tuples are immutable lists, meaning they do not change
# Syntax >> tuple_list{'hello', 10, 13, 4}
my_tuple = ('eggs', 'bread', 'oats', '10')
print(my_tuple)
print(type(my_tuple))
# Can read from them but not add to them or change them


# breakpoint() can be used for debugging and pauses code while running at a given point
breakpoint()

