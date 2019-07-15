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

