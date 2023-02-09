class Classe:
    age = 80

    def __init__(self, a):
        self.a = a

    @classmethod
    def get_class_name(cls):
        return cls.__name__


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, staff_num):
        super().__init__(name, age)
        self.staff_num = staff_num


class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(C.mro())
