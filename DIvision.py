from abc import ABCMeta, abstractmethod
from numbers import Number
from Redefined_Opreators import Redefined_Oprators
from Abstract_Class import Abstract_Class
from Argument_Checker import Argument_Checker


class Division(Abstract_Class, Argument_Checker, Redefined_Oprators):
    def __init__(self, *denominators, numerator=1):

        if not self.is_number(numerator) or self.is_zero(numerator):
            raise TypeError('Numerator must be a number and not zero')

        self.numerator = numerator
        self.denominators = self.check_numbers(*denominators)
        self.denoms_sum = sum(denominators)

        Redefined_Oprators.__init__(self, self.denoms_sum)

        self.ratios = [i / self.denoms_sum for i in self.denominators]

    def __len__(self):
        return len(self.denominators)

    def __bool__(self):
        return not self.numerator == 1

    def __str__(self):
        return f"""
            numerator: {self.numerator}
            denominators: {tuple(self.denominators)}
            ratios: {self.calc_divisions(self.numerator)}
        """

    def __call__(self, arg=None):
        if not arg:
            return self.calc_divisions(self.numerator)
        # from parent Argument_Checker class
        if not self.apply_all_checks_to_arg(arg):
            raise TypeError
        return self.calc_divisions(arg)

    def calc_divisions(self, arg):
        return tuple(arg * i for i in self.ratios)


test = Division(1, 3, 4, numerator=3)

print(test)
print(bool(test))
print(len(test))
print(test(4))

# почему здесь del, описано в Abstract_Class.py
del test
