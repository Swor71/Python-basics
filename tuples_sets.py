# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create a tuple

fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma!!

fruits3 = ('Apples',)

print(fruits[1])

# Delete tuple

print(len(fruits2))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set

fruits_set = {'Apples', 'Orange', 'Mango'}

# Check if something is in the set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')
print(fruits_set)

# Remove

fruits_set.remove('Grape')
print(fruits_set)

# Clear set

fruits_set.clear()

# Deleting

del fruits_set
