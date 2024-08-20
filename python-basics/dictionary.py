# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members allowed. 
# This is basically the opposite of tuples


# There is a huge difference between dictionary and lists
# 
# Create dictionary

person = {
    'first_name': 'Andrew',
    'last_name': 'Okwe',
    'age': 40
}

# print(person, type(person))

# Create dictionary using constructor

person2 = dict(first_name='Steph', lastName='Okwe')

# print(person2, type(person2))

# print(person['last_name'])
# print(person.get("first_name"))

# Add key/value to dictionary
person['phone'] = '806-888-000-99'

# print(person.get('phone'))

# print(person.keys())

print(person.items())

# COpy dictionaries

person2 = person.copy()

person2['city'] = 'Lagos'

# print(person2)

# Remove item

del(person['age'])
person.pop('phone')

# print(person)

#Clear dictionary

person.clear()

# get length
print(len(person))

person3 = [
    {'name':'Andrew', 'age':80},
    {'name':'Kelvin', 'age': 89}
]

print(person3[0])