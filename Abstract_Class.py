from abc import ABCMeta, abstractmethod
import atexit


class Abstract_Class(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def __repr__(self):
        instance_args = {
            key: val for key, val in self.__dict__.items() if val != None
        }
        return f"""
        module: {self.__module__}\n
        class: {self.__class__.__name__}\n
        arguments: {instance_args}
        """

    # я наткнулся на такую проблему - после завершения выполнения всего кода, python очищает память
    # и отрабатывает метод __del__. в методе del мы уже не можем достучаться до open для открытия файла,
    # т.к. __builtins__ уже не доступны. гуглил несколько подходов,
    # либо используют библиотеку atexit и ее метод register в __init__, а в данном случае класс и __init__ по условию абстрактный,
    # либо используют weekref.finalize для самого экземпляра класса,
    # либо оборачивают класс в with конструкцией типа with class() as сls и в классе тогда вместо __init__ - __enter__,
    # а вместо __del__ - __exit__
    #
    # я костыльнул слегка и написал способ через метод класса, но он работает только при удалении экземпляра используя del,
    #
    # пока оставил так, можно было еще дописать в дочерний класс в __init__  atexit.register и передать туда метод этого класса,
    # тогда __del__ вообще не нужен, а это не по заданию))
    # есть предложение на занятии разобрать как нужно в таких случаях делать, я почитал доку и stackoverflow,
    # мне кажется самое нормальное решение использовать atexit

    @classmethod
    def write_cache(self, instance):
        with open('cache.txt', 'a') as cache:
            cache.write(instance.__repr__())

    def __del__(self):
        Abstract_Class.write_cache(self)
