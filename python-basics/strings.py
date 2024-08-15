# Strings

name = 'Andrew'
age = 39

# Concatenate
print('My name is ' + name)

# String formatting
print('My name is {myName} and I am {myAge} years old'.format(myName=name, myAge=age))

# f strings
print(f'My name is {name} and I am {age} years old')

# String methods
string = 'hello world'

# capitalize
print(string.capitalize())

print(string.upper())

print(string.lower())

print(string.swapcase())

print(string.startswith('3'))

print(string.endswith('e'))

print(len(string))

print(string.split())

print(string.find('e'))

print(string.isalnum())

print(string.isalpha())

print(string.islower())
