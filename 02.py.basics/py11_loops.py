my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list2 = [(1, 2), (3, 4), (5, 6)]
my_dict = {'a': 1, 'b': 2, 'c': 3}

for num in my_list:
    print(num)

for num in my_tuple:
    print(num)

for num in my_list2:
    print(num)

for num in '123':
    print(num)

for idx, value in enumerate(my_list):
    print(idx)
    print(value)


for k, v in my_dict.items():
    print(k)
    print(v)

while False:
    ...
    if True:
        break
    if True:
        continue

msg = ''
while msg != 'quit':
    msg = input('What should I do? ')
    print(msg)
