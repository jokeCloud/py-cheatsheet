my_list = [1, 2, '3', True]

print(len(my_list))
print(my_list.index('3'))
print(my_list.count(2))

print(my_list[3])
print(my_list[1:])
print(my_list[:1])
print(my_list[-1])
print(my_list[::1])
print(my_list[::-1])
print(my_list[0:3:2])

print(my_list * 2)
print(my_list + [100])
my_list.append(200)
print(my_list)
my_list.extend([100, 200])
print(my_list)
my_list.insert(2, '!!!')
print(my_list)

print(' '.join(['Hello', 'There']))

basket = ['apples', 'pears', 'oranges']
new_basket = basket.copy()
new_basket2 = basket[:]

print(basket, new_basket, new_basket2)

print([1, 2, 3].pop())
print([1, 2, 3].pop(1))
a = [1, 2, 3]
a.remove(2)
print(a)
b = [1, 2, 3]
b.clear()
print(b)
c = [1, 2, 3]
del c[0]
print(c)

print(sorted([5, 2, 3, 1, 4]))
a = [5, 2, 3, 1, 4]
a.sort()
print(a)

a = [1, 2, 5, 3]
a.sort(reverse=True)
print(a)

a = [1, 2, 5, 3]
a.reverse
print(a)

a = [1, 2, 5, 3]
a = sorted(a)
print(a)

my_list = [(4, 1), (2, 4), (2, 5), (1, 6), (8, 9)]
a = sorted(my_list, key=lambda x: int(x[0]))
print(a)

a = list(reversed([1, 2, 5, 3]))
print(a)

print(1 in [1, 2, 3, 4, 5, 6])
print(min([1, 2, 3, 4, 5]))
print(max([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5]))

m_list = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
first, *x, last = m_list
print(first)
print(last)
print(*x)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[2][0])

mx = [[1, 2, 3], [4, 5, 6]]
for row in range(len(mx)):
    for col in range(len(mx[0])):
        print(mx[row][col])


print([mx[row][col] for row in range(len(mx)) for col in range(len(mx[0]))])

print([x for x in zip(*mx)])

list_of_chars = list('olow')
print(list_of_chars)

sum_of_elements = sum([1, 2, 3, 4, 5])
element_sum = [sum(pair) for pair in zip([1, 2, 3], [4, 5, 6])]
sorted_by_second = sorted(['hi', 'you', 'man'], key=lambda el: el[1])
print(sorted_by_second)
sorted_by_key = sorted([
    {'name': 'dina', 'age': 30},
    {'name': 'louie', 'age': 18},
    {'name': 'zina', 'age': 55},
], key=lambda el: (el['name']))

print(sorted_by_key)

with open('mylife.txt') as f:
    lines = [line.strip() for line in f]
