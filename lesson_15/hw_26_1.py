
class NegativePower(UserWarning):
    def __init__(self, a, b):
        super().__init__("Відемна ступінь")


class SqrtNegative(UserWarning):
    def __init__(self):
        super().__init__("Відемний аргумент")


class Calculator:
    def add(self,a,b):
        try:
            result = a + b
            return result
        except Exception:
            return "Помилка"

    def subtract(self, a, b):
        try:
            result = a - b
            return result
        except Exception:
            return "Помилка"
        
    def multiplication(self, a, b):
        try:
            result = a * b
            return result
        except Exception:
            return "Помилка"
        
    def divide(self, a, b):
        try:
            if b == 0:
                raise ZeroDivisionError
            result = a / b
            return result
        except ZeroDivisionError:
            print("Ділити на 0 неможна")
            return "Error"

    def sqroot(self, a):
        try:
            if a < 0:
                raise SqrtNegative
            result = a ** 0.5
            return result
        except SqrtNegative:
            print(SqrtNegative)
            return "Error"
        
    def power(self, a, b):
        try:
            if b < 0:
                raise NegativePower
            result = a ** b
            return result
        except NegativePower:
            print(NegativePower)
            return "Error"
        
calc = Calculator()
print(calc.add(1,2))
print(calc.subtract(4,3))
print(calc.divide(3,4))
print(calc.multiplication(3,4))
print(calc.power(3,4))
print(calc.sqroot(3))

print(calc.add(1,"True"))
print(calc.multiplication("rrr",3))
