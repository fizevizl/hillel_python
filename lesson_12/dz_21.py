
class Auto:
    def __init__(self, brand, age, mark, color='', weight=0):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print(f"{self.brand} is moving.")

    def stop(self):
        print(f"{self.brand} has stopped.")

    def birthday(self):
        self.age += 1

# Приклад використання класу Auto:
car1 = Auto(brand='Toyota', age=3, mark='Camry', color='red', weight=1500)
print(f"Car 1: Brand - {car1.brand}, Age - {car1.age}, Mark - {car1.mark}, Color - {car1.color}, Weight - {car1.weight}")
car1.move()
car1.stop()
car1.birthday()
print(f"Car 1's age after birthday: {car1.age}")
