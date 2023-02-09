from functools import reduce

print(list(map(lambda x: x + 1, range(10))))

print(list(filter(lambda x: x > 5, range(10))))

print(reduce(lambda acc, x: acc + x, range(10)))
