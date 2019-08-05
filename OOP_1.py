class Descriptor(object):
    def __get__(self, instante, owner):
        pass
class A(object):
    x = Descriptor
    def f(self):
        print('hello')
# instance - сам объект
# owner - сам класс
a = A()
'''print(A.f)
print(a.f)
print(A.x)
print(a.x)
A.f(a)
a.f()'''
a.x
A.x.__get__(a, type(a))