# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Constructor

person2 = dict(first_name='Sara', last_name='Williams', age=25)

print(person, type(person))

# Get value

print(person['first_name'])

print(person.get('last_name'))

# Add key-value

person['phone'] = '555-555'

print(person)
print(person.keys())
print(person.items())

# Copy dict

person3 = person.copy()
person3['city'] = 'Oslo'

print(person3, person)

# Remove item
del(person['age'])
person.pop('phone')

# clear
person.clear()
print(person)

# get length
len(person2)

# list of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Tom', 'age': 25}
]

print(people[0]['name'])
