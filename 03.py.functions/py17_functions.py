args = (1, 2)
kwargs = {'x': 3, 'y': 4, 'z': 5}


def some_func(*args, **kwargs):
    for arg in args:
        print(arg)

    for kwarg in kwargs:
        print(kwarg)


some_func(args, kwargs)


print(args)
print(kwargs)


def add(*a):
    return sum(a)


print(add(1, 2, 3))


# def f(*args):                  # f(1, 2, 3)
# def f(x, *args):               # f(1, 2, 3)
# def f(*args, z):               # f(1, 2, z=3)
# def f(x, *args, z):            # f(1, 2, z=3)

# def f(**kwargs):               # f(x=1, y=2, z=3)
# def f(x, **kwargs):            # f(x=1, y=2, z=3) | f(1, y=2, z=3)

# def f(*args, **kwargs):        # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
# def f(x, *args, **kwargs):     # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3) | f(1, 2, 3)
# def f(*args, y, **kwargs):     # f(x=1, y=2, z=3) | f(1, y=2, z=3)
# def f(x, *args, z, **kwargs):  # f(x=1, y=2, z=3) | f(1, y=2, z=3) | f(1, 2, z=3)


print([*[1, 2, 3], *[4]])
print({*[1, 2, 3], *[4]})
print((*[1, 2, 3], *[4]))
print({**{'a': 1, 'b': 2}, **{'c': 3}})

head, *body, tail = [1, 2, 3, 4, 5]
