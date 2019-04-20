class Redefined_Oprators():
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other

    def __radd__(self, other):
        return other + self.num

    def __iadd__(self, other):
        raise TypeError

    def __sub__(self, other):
        return self.num - other

    def __rsub__(self, other):
        return other - self.num

    def __isub__(self, other):
        raise TypeError

    def __truediv__(self, other):
        return self.num / other

    def __rtruediv__(self, other):
        return other / self.num

    def __itruediv__(self, other):
        return TypeError

    def __mod__(self, other):
        return self.num % other

    def __rmod__(self, other):
        return other % self.num

    def __imod__(self, other):
        raise TypeError

    def __rshift__(self, other):
        return self.num >> other

    def __rrshift__(self, other):
        return other >> self.num

    def __irshift__(self, other):
        raise TypeError
