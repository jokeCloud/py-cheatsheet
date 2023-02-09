print([i+1 for i in range(10)])
print(set(i for i in range(10) if i > 5))
print(tuple(i+5 for i in range(10)))
print({i: i*2 for i in range(10)})

output = [i+j for i in range(3) for j in range(3)]
print(output)

output = []
for i in range(3):
    for j in range(3):
        output.append(i+j)
