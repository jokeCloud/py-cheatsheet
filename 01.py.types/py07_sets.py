my_set = set()
print(my_set)

my_set.add(1)
my_set.add(100)
my_set.add(100)
print(my_set)


new_list = [1, 2, 3, 3, 3, 4, 4, 5, 6, 1]
print(new_list)

print(set(new_list))

print(my_set)
my_set.remove(100)
print(my_set)
my_set.discard(100)
print(my_set)
my_set.clear()
print(my_set)

new_set = {1, 2, 3}.copy()
print(new_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
set5 = set1.difference(set2)
print(set5)
set6 = set1.symmetric_difference(set2)
print(set6)
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))
