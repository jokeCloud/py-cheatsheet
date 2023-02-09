from collections import Counter
colors = ['red', 'green', 'blue', 'yellow', 'blue', 'red']
counter = Counter(colors)
print(counter)
print(counter.most_common())
print(counter.most_common()[0])
