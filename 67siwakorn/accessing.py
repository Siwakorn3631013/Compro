phonebook = {'anirach': '777-1111', 'mickey' : '777-2222' , 'donald' : '777-333'}

print(phonebook)

print(phonebook['mickey'])
print(phonebook.get('donald'))

key= 'pluto'
if key in phonebook:
    print(phonebook['pluto'])
else:
    print(key+ 'not in phonebook')
