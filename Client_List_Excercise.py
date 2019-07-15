# Create a list with 10 clients for sparta
# Access at least 4 clients and print them out with a nice sentences
sparta_clients = [['RBS', 'nice'], ['Direct Line', 'cool'], ['Spotify', 'very cool'], ['Google', 'exciting'],
                  ['Amazon', 'big'], ['KFC', 'fantastic'], ['Aviva', 'wealthy'], ['Budweiser', 'fun'],
                  ['Netflix', 'famous'], ['Ebay', 'loyal']]

for x in range(0, 5):
    print(f'{sparta_clients[x][0]} is a {sparta_clients[x][1]} client of Sparta')
for x in range(5, 10):
    print(sparta_clients[x][0] + ' is a ' + sparta_clients[x][1] + ' client of Sparta')

# Exercise 3

Story = {
    'title': 'The Story of Sparta',
    'author': 'Matthew Mackreth',
    'hero': 'Matt',
    'beginning': 'Once upon a time there was a large Dev Ops class that took 2 trainers to teach.',
    'middle': 'They were expertly taught business skills, SQL skills and python skills by Fillipe and Markson.',
    'end': 'Then they all got placed and had a great time. The end.'
}

print(Story['title'])
print('by' + Story['author'])
print('The hero of the story is ' + Story['hero'])
print(Story['beginning']),
print(Story['middle']),
print(Story['end'])
