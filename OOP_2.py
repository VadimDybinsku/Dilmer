class A(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
# Перезапись функции дискриптором
    @property
    def z(self):
        return self.x + self.y

a = A(1,2)
print(a.z)
