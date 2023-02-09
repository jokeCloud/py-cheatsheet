print(type('olow'))


# print('I\'m thirsty)
print("I\'m thirsty")
print("olow\nolow")  # <br>
print("\tolow")  # tab

print('hey you'[4])
name = 'johansen masterson'
print(name[4])
print(name[:])
print(name[1:])
print(name[:1])
print(name[::1])
print(name[::-1])
print(name[0:10:2])

print('Hi there ' + 'jon')
print('*' * 3)
print('🥇' * 3)

print(len('turtle'))

striped = '   I am alone'.strip()
print(striped)
striped = 'on an island'.strip('d')
print(striped)

splited = 'but life is good!'.split()
print(splited)

replaced = 'help me'.replace('me', 'you')
print(replaced)

starts_with = 'need to make fire'.startswith('need')
print(starts_with)

ends_with = 'and cook rice'.endswith('rice')
print(starts_with)

print('still there?'.upper())

print('HELLO?'.lower())

print('ok, I am done'.capitalize())

print('oh hi there'.count('e'))

print('bye bye'.index('e'))

print('oh hi there'.find('i'))

print('oh hi there'.find('a'))

# print('oh hi there'.index('a'))


name_1 = 'jon'
name_2 = 'mark'

print(f'hello there {name_1} and {name_2}')
print('hello there {} and {}'.format(name_1, name_2))
print('hello there %s and %s' % (name_1, name_2))

word = 'reviver'
p = bool(word.find(word[::-1]) + 1)
print(p)
