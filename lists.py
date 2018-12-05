# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list

numbers = [1, 2, 3, 4, 5]

numbers2 = list((1, 2, 3, 4, 5, 6))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# print(numbers, numbers2)

print(fruits[1])

# Get lenght

len(fruits)

# Change value

fruits[0] = 'Blueberries'

# Append to list

fruits.append('Mangos')

fruits.remove('Grapes')

fruits.insert(2, 'Strawberries')
print(fruits)

fruits.pop(2)

fruits.reverse()

fruits.sort()

fruits.sort(reverse=True)

print(fruits)
