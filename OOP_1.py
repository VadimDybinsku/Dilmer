class C(object):
    def __get__(self, instante, owner):
        return 4
class A(object):
    x = 1
class B(A):
    x = C()
    def __init__(self):
        x = 3
b = B()
print(b.x)