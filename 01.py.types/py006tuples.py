my_tuple = ('apple', 'grapes', 'mango', 'grapes')

apple, grapes, mango, grapes = my_tuple

print(len(my_tuple))
print(my_tuple[2])
print(my_tuple[-1])

# error
# my_tuple[1] = 'donuts'
# my_tuple.append('candy')

print(my_tuple.index('grapes'))
print(my_tuple.count('grapes'))

a = list(zip([1, 2, 3], [4, 5, 6]))
print(a)

z = [(1, 2), (3, 4), (5, 6), (7, 8)]
def unzip(z): return list(zip(*z))


unzip(z)
print(z)
