from math import fsum
def decor_2(func):
    def outp (*args):
        print(func.__name__)
        print(args)
        print(func(*args))
    return outp
@decor_2
def func(*args):
    print(fsum(args))
func(1, 2, 10, 145, 567)