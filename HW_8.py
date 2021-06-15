# 1
# class Data:
#
#     def __init__(self, data):
#         self.int_data = self.get_data(data)
#
#     def __str__(self):
#         return f"{self.int_data}"
#
#     @classmethod
#     def get_data(cls, data):
#         data_array = data.split("-")
#         _day = int(data_array[0])
#         _month = int(data_array[1])
#         _year = int(data_array[2])
#         if Data.validate_data(_day, _month, _year):
#             return int(f"{_day}{_month}{_year}")
#         else:
#             return None
#
#     @staticmethod
#     def validate_data(day, month, year):
#         if day < 0 or day > 31:
#             print("Не корректное значение дня")
#             return False
#         if month < 0 or month > 12:
#             print("Не корректное значение месяца")
#             return False
#         return True
#
#
# data = Data("10-12-2002")
# print(data)

# 2
# class MyZeroError(Exception):
#     def __init__(self, text):
#         self.txt = text
#
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
#
# try:
#     if b == 0:
#         raise MyZeroError("На ноль делить нельзя")
# except MyZeroError as mr:
#     print(mr)
# else:
#     print(a/b)

# 3
# class MyErrorList(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# number_list = []
# while True:
#     a = input("Введите число или слово 'stop' для завершения ввода: ")
#     if a == 'stop':
#         break
#     try:
#         try:
#             a = int(a)
#         except ValueError:
#             raise MyErrorList("Нам нужны только строки")
#     except MyErrorList as mr:
#         print(mr)
#     else:
#         number_list.append(a)
# print(number_list)

# 4
# class Warehouse:
#     def __init__(self):
#         self.store = {}
#
#     def __str__(self):
#         result = ""
#         for group, equipment in self.store.items():
#             result += f"{group}: \n"
#             for item, count in equipment.items():
#                 result += f"   {item}: {count}\n"
#         return result
#
#     @staticmethod
#     def validate_count(count):
#         if not isinstance(count, int):
#             print("Не валидный тип количества оргтехники")
#             return False
#         return True
#
#     def add_equipment(self, equipment, count, group):
#         if Warehouse.validate_count(count):
#             group_store = self.store.get(group, {})
#             equipment_count = group_store.get(equipment.name, 0)
#             equipment_count += count
#             group_store[equipment.name] = equipment_count
#             self.store[group] = group_store
#
#
# class Equipment:
#     def __init__(self, name):
#         self.name = name
#
#
# class Printer(Equipment):
#     def __init__(self):
#         super().__init__("Принтер")
#
#
# class Scanner(Equipment):
#     def __init__(self):
#         super().__init__("Сканер")
#
#
# class Xerox(Equipment):
#     def __init__(self):
#         super().__init__("Ксерокс")
#
#
# scanner = Scanner()
# printer = Printer()
# printer1 = Printer()
# printer2 = Printer()
# xerox = Xerox()
#
# ware_house = Warehouse()
# ware_house.add_equipment(printer, 1, "IT")
# ware_house.add_equipment(scanner, 1, "HR")
# ware_house.add_equipment(printer1, 1, "HR")
# ware_house.add_equipment(printer2, 1, "HR")
# ware_house.add_equipment(xerox, 1, "HR")
# print(ware_house)

# 7
# class Complex(object):
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return '%s + %si' % (self.a, self.b)
#
#     def __add__(self, rhs):
#         return Complex(self.a + rhs.a, self.b + rhs.b)
#
#     def __mul__(self, rhs):
#         return Complex(self.a * rhs.a - self.b * rhs.b, self.b * rhs.a + self.a * rhs.b)
#
#
# a = Complex(0, 1)
# b = Complex(1, 2)
#
# c = a + b
# d = a * b
# print(c)
# print(b)
