#1
# import time
# class TrafficLight:
#     __color = ["Красный", "Желтый", "Зеленый"]
#
#     def running(self):
#         while True:
#             print(TrafficLight.__color[0])
#             time.sleep(7)
#             print(TrafficLight.__color[1])
#             time.sleep(2)
#             print(TrafficLight.__color[2])
#             time.sleep(7)
#
# traffic = TrafficLight()
# traffic.running()

#2
# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def calculate_weight(self, weight, depth):
#         return self._length * self._width * weight * depth / 100 / 1000
#
# road = Road(100, 50)
# print(f"{road.calculate_weight(50, 25)}т")


#3
# class Worker:
#    def  __init__(self, name, surname, position, income):
#        self.name = name
#        self.surname = surname
#        self.position = position
#        self._income = income
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return self.name
#
#     def get_total_income(self):
#         return self._income["wage"] + self._income["bonus"]
#
# position = Position("Антон", "Иванов", "Инженер", {"wage":15000, "bonus": 5000})
# print(position.get_full_name())
# print(position.get_total_income())

#4
# class Car:
#     def __init__(self, speed, color, name, is_police):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#
#     def go(self):
#         print("Машина поехала")
#
#     def stop(self):
#         print("Машина остановилась")
#
#     def turn(self, direction):
#         if direction == "left":
#             print("Машина повернула на лево")
#         elif direction == "right":
#             print("Машина повернула направо")
#         else:
#             pass
#
#     def show_speed(self):
#         print(self.speed)
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed > 60 and not self.is_police:
#             print("Вы превысили скорость")
#         Car.show_speed(self)
#
# class SportCar(Car):
#     def print(self):
#         pass
#
#
# class WorkCar(Car):
#
#     def show_speed(self):
#         if self.speed > 40 and not self.is_police:
#             print("Вы превысили скорость")
#         Car.show_speed(self)
#
#
# class PoliceCar(Car):
#     def print(self):
#         pass
#
# car = WorkCar(30, "RED", "Mustang", False)
# car.show_speed()

#5
# class Stationery:
#     title = "Stationery"
#     def draw(self):
#         print("Запуск отрисовки")
#
# class Pen(Stationery):
#
#     def draw(self):
#         print("Запуск отрисовки ручки")
#
#
# class Pencil(Stationery):
#
#     def draw(self):
#         print("Запуск отрисовки карандаша")
#
# class Handle(Stationery):
#
#     def draw(self):
#         print("Запуск отрисовки маркера")
#
# hadle = Handle()
# hadle.draw()
#
# pen = Pen()
# pen.draw()
#
# pencil = Pencil()
# pencil.draw()