from multipledispatch import dispatch


class Calculator:

    @dispatch(int, int)
    def product(self, first, second):
        result = first * second
        print(result)

    @dispatch(int, int, int)
    def product(self, first, second, third):
        result = first * second * third
        print(result)

    @dispatch(float, float, float)
    def product(self, first, second, third):
        result = first * second * third
        print(result)


calculator = Calculator()
calculator.product(2, 3, 2)
calculator.product(2.2, 3.4, 2.3)