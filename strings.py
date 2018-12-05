# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Marcin'
age = 31

# Concatenate
print('Hi my name is ' + name + ' I am ' + str(age))

# String Formatting

# Arguments by position

print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)

print(f'Hi, my name is {name} and I am {age}')

# String Methods

s = 'hello world'

# Capitalize sting

print(s.capitalize()),
print(s.upper()),
print(s.swapcase()),
len(s),
print(s.replace('world', 'everyone'))
sub = 'hi'
print(s.count(sub))
print(s.startswith('hello'))
print(s.endswith('world'))
print(s.split())
print(s.find('r'))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())
