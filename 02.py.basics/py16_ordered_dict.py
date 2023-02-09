from collections import OrderedDict

programmers = OrderedDict()
programmers['jon'] = ['python', 'javascript', 'ruby', 'go']
programmers['sarah'] = ['c++']
programmers['bia'] = ['javascript', 'typescript']

for name, langs in programmers.items():
    print(name + ' ➡️')
    for lang in langs:
        print('\t' + lang)


print()

print(programmers)
print(programmers['jon'])
