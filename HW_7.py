# 1
# class Matrix:
#     def __init__(self, data):
#         self.data = data
#         self.count_str = len(data)
#
#     def __str__(self):
#         result = ""
#         for item in self.data:
#             for number in item:
#                 result += str(number)
#                 result += " "
#             result += '\n'
#         return result
#
#     def __add__(self, other):
#         if self.count_str == other.count_str and len(self.data[0]) == len(other.data[0]):
#             data = []
#             for i in range(len(self.data)):
#                 data.append([self.data[i][j] + other.data[i][j] for j in range(len(self.data[i]))])
#             return Matrix(data)
#         else:
#             print("Мы не можем складывать матрицы разных размерностей")
#             pass
#
# matrix1 = Matrix([[10, 12], [10,12]])
# matrix2 = Matrix([[20, 21], [20,21]])
# matrix3 = matrix1 + matrix2
# print(matrix1)
# print(matrix2)
# print(matrix3)

# 2
# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     def __add__(self, other):
#         return self.calculation_tissue_consumption() + other.calculation_tissue_consumption()
#
#     @abstractmethod
#     def calculation_tissue_consumption(self):
#         pass
#
#
# class Suit(Clothes):
#
#     def __init__(self, h):
#         self._h = h
#
#     @property
#     def h(self):
#         return self._h
#
#     @h.setter
#     def h(self, value):
#         self._h = value
#
#     def calculation_tissue_consumption(self):
#         return 2 * self.h + 0.3
#
#
# class Coat(Clothes):
#
#     def __init__(self, v):
#         self._v = v
#
#     @property
#     def v(self):
#         return self._v
#
#     @v.setter
#     def v(self, value):
#         self._v = value
#
#     def calculation_tissue_consumption(self):
#         return self.v / 6.5 + 0.5
#
#
# coat = Coat(170)
# suit = Suit(45)
# print(coat + suit)

# 3


# class Cell:
#     def __init__(self, count_cell):
#         self.count_cell = count_cell
#
#     def __add__(self, other):
#         return Cell(self.count_cell + other.count_cell)
#
#     def __sub__(self, other):
#         result = self.count_cell - other.count_cell
#         if result > 0:
#             return Cell(self.count_cell - other.count_cell)
#         else:
#             print("Разность двух ячеек меньше нуля")
#
#     def __mul__(self, other):
#         return Cell(self.count_cell * other.count_cell)
#
#     def __truediv__(self, other):
#         return Cell(self.count_cell // other.count_cell)
#
#     def make_order(self, count):
#         count_str = self.count_cell / count
#         count_end_str = self.count_cell % count
#         for i in range(int(count_str)):
#             for j in range(count):
#                 print("*", end="")
#             print()
#         if count_end_str != 0:
#             for i in range(count_end_str):
#                 print("*", end="")
#
#
# cell = Cell(11)
# cell.make_order(4)
