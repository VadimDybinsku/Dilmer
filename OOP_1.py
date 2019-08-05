class A(object):
    x = 1
class B(A):
    x = 2
    def __init__(self):
        self.x = 3

b = B()
print(b.x)