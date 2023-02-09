def get_multiplier(a):
    def out(b):
        return a * b
    return out


multiply_by_3 = get_multiplier(3)
print(multiply_by_3(10))
