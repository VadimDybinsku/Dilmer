def f(self):
    print(self)

class Descriptor(object):
    def __get__(self, instance, owner):
        def wrapper():
            return f(instance)
        return wrapper
class A(object):
    f = Descriptor

a = A()
print(a)
a.f()