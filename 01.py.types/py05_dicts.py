my_dict = {'name': 'jon', 'age': 32, 'magic_power': False}
print(my_dict['name'])
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))
print(list(my_dict.items()))

my_dict['favourite_snack'] = 'grapes'
print(my_dict.get('age'))
print(my_dict.get('ages', 0))

del my_dict['name']
my_dict.pop('name', None)

my_dict.update({'cool': True})

{**my_dict, **{'cool': True}}

new_dict = dict([['name', 'jon'], ['age', 32], ['magic_power', False]])
new_dict = dict(zip(['name', 'age', 'magic_power'], ['jon', 32, False]))
new_dict = my_dict.pop('favourite_snack')

print({key: value for key, value in new_dict.items() if key ==
       'age' or key == 'name'})
