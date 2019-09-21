a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_item = {}
for key,value in a_dict.items():
    if value <=2:
        new_item[key] = value
print(new_item)

#Dict comprehension
dict_comprehension = {k: v for k, v in a_dict.items() if v <= 2}
print(dict_comprehension)