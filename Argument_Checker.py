from abc import ABCMeta, abstractmethod
from numbers import Number


class Argument_Checker(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def is_number(self, arg):
        return isinstance(arg, Number)

    def is_zero(self, num):
        return num == 0

    def is_integer(self, num):
        return type(num) == type(int())

    def is_positive(self, num):
        return num > 0

    def apply_all_checks_to_arg(self, num):
        return (
            self.is_number(num) and
            self.is_integer(num) and
            not self.is_zero(num) and
            self.is_positive(num)
        )

    def check_numbers(self, *args):
        for el in args:
            if not '__mod__' in dir(el) or not self.apply_all_checks_to_arg(el):
                raise TypeError('Invalid argument')
        return args
