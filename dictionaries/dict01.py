a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
'''
Sample dictionary code
'''
for key in a_dict:
    print(key,'->', a_dict[key])

#Iterating Through .items()
for item in a_dict.items():
    print(item)

print('Iterating Through .values()')
for value in a_dict.values():
    print(value)

print('Iterating through keys')
for k in a_dict.keys():
    print(k)
