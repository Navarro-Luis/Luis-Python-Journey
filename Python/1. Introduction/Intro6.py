dictionary = {
    'Gender' : 'male',
    'Height' : 'Tall',
    'Eyes' : 'blue'
}

print(dictionary['Gender'])
print(dictionary.get('Height', "does not exist"))
print('Gender' in dictionary)