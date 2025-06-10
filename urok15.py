# # Задача 1
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def vivod(self):
        print(f'Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}')

Autobus = Transport("Renaul Logan", 180, 12)
Autobus.vivod()

# Задача 2

class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"

class Autobus(Transport):
    def __init__(self, name, max_speed, mileage):
       Transport.__init__(self, name, max_speed, mileage)

    def seating_capacity(self, capacity=50):
        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"


autobus = Autobus("Renaul Logan", 120, 12)
print(autobus.seating_capacity())