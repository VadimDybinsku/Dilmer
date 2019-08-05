class C(object):
    def __get__(self, instante, owner):
        return 4
class A(object):
    x = 1
class B(A):
    x = C()

b = B()
print(b.x)