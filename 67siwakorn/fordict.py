phonebook = {'Anirach': '777-1111' , 'mickey': '777-2222', 'Donald': '777-3333'}

phonebook['bart']=[1, 3, 5]

elements = len(phonebook)
print('there are', elements, 'names in phonebook')

for key in phonebook:
    print(key, 'phone number is: ', phonebook[key])

phonebook['bart'][1]=9
print(phonebook)

