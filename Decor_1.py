def decor_1(func):
    def reverse(*args):
        return func(*args[::-1])
    return reverse
@decor_1
def func(*args):
    print(*args)
func(1, 2, 10, 145, 567)
