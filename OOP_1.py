def f(self):
    print(self)

class Descriptor(object):
    def __get__(self, instance, owner):
        def wrapper(*args):
            return f(instance, *args)
        return wrapper

class A(object):
    def f(self):
        pass

a = A()
print(a.f)
print('f' in a.__dict__)
value = None
for base in A.__mro__:
    print(f"{base.__name__}: {'f'in base.__dict__}")
    if 'f' in base.__dict__:
        value = base.__dict__['f']
        break
getter = getattr(value,'__get__', None)
print(getter)

print(getter(a, A))
print(a.f)