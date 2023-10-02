
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

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='', weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        super().move()
        print("attention")

    def load(self):
        import time
        time.sleep(1)
        print("load")
        time.sleep(1)

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='', weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")

truck1 = Truck(brand='Porsche', age=5, mark='Cayenne', max_load=10000, color='blue', weight=7500)
truck2 = Truck(brand='Mercedes', age=3, mark='Actros', max_load=35000, color='red', weight=8800)

truck1.move()
truck1.load()
truck2.move()
truck2.load()

car1 = Car(brand='Toyota', age=2, mark='Camry', max_speed=180, color='silver', weight=1700)
car2 = Car(brand='Ford', age=1, mark='Mustang', max_speed=220, color='black', weight=1300)

car1.move()
car2.move()
