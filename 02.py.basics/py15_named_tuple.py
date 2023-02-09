from collections import namedtuple


Point = namedtuple('Point', 'x y')
p = Point(1, y=2)
print(p[0])
print(p.x)
print(getattr(p, 'y'))
print(p._fields)

Person = namedtuple('Person', 'name height')
person = Person('jon-luc', 187)
print(f'{person.height}')
print('{p.height}'.format(p=person))
