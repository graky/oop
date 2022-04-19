class Counter:
    def __init__(self):
        self._current = 0

    def increment(self):
        self._current += 1

    def value(self):
        return self._current

    def reset(self):
        self._current = 0


counter = Counter()

# Вызов counter._current вызовет ошибку атрибута, т.к. атрибут приватный и не доступен из экземпляра класса напрямую


class ClassPrivate:

    def __init__(self):
        self.__num = 0

    def __value(self):
        return self.__num

    def display(self):
        return self.__value()

# Вызов __value вызовет ошибку метода, т.к. метод личный и не доступен напрямую

var_private = ClassPrivate()
print(var_private.display())