class String(str):
    def __init__(self, value):
        self.value = str(value)

    def __add__(self, other):
        if not isinstance(other, String):
            other = String(other)
        return String(super().__add__(other))

    def __sub__(self, other):
        if not isinstance(other, String):
            other = String(other)
        return String(self.value.replace(other, "", 1))


a = String("New")
b = String(890)
print(a + b, type(a + b))
print(String("New") + String(890))
print(String(1234) + 5678)
print(String("New") + "castle")
print(String("New") + 77)
print(String("New") + True)
print(String("New") + ["s", " ", 23])
print(String("New") + None)

print(String("New bala7nce") - 7)
print(String("New balance") - "bal")
print(String("New balance") - "Bal")
print(String("pineapple apple pine") - "apple")
print(String("New balance") - "apple")
print(String("NoneType") - None)
print(String(55678345672) - 7)
