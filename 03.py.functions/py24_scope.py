def get_counter():
    i = 0

    def out():
        nonlocal i
        i += 1
        return i
    return out


counter = get_counter()

print(counter(), counter(), counter())
