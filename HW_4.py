#1
# import sys
# print(f"Результат: {sys.argv[1] * sys.argv[2] + sys.argv[3]}")

#2
# import random
# a = []
# for i in range(1,15):
#     a.append(random.randint(1, 1000))
# print(a)
# tmp = a[0]
# b = []
# for i in a:
#     if i > tmp:
#         b.append(i)
#     tmp = i
# print(f'Результат: {b}')

#3
# print(f"Результат: {[c for c in range(20, 240) if c % 20 == 0 or c % 21 ==0]}")

#4
# import random
# a = []
# for i in range(1,15):
#     a.append(random.randint(1, 1000))
# print(a)
# b = []
# for i in a:
#     if i in b:
#         b.remove(i)
#         continue
#     b.append(i)
# print(f"результат: {b}")

#5
# from functools import reduce
# print(f"Результат: {reduce(lambda a, b: a * b, [c for c in range(100, 1001) if c % 2 == 0 ])}")

#6.1
# import sys
# class SimpleIterator:
#     def __init__(self, start_number, limit):
#         self.limit = limit
#         self.counter = start_number
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
#
#
# start_number = sys.argv[1]
# count_numbers = 10
# s_iter = SimpleIterator(start_number, count_numbers)
# while True:
#     print(next(s_iter))

#6.2
# from itertools import cycle
# class CycleIterator:
#     def __init__(self, start_list, limit):
#         self.limit = limit
#         self.example = start_list
#         self.count_numbers = len(self.example)
#         self.current_index = -1
#         self.repit = 0
#
#     def __next__(self):
#         self.current_index += 1
#         if self.repit >= self.limit:
#             raise StopIteration
#         if self.current_index < self.count_numbers:
#             return self.example[self.current_index]
#         else:
#             self.current_index = 0
#             self.repit += 1
#             return self.example[self.current_index]
#
#
# start_list = [1,2,5,6,12,43]
# count_numbers = 10
# c_iter = CycleIterator(start_list, count_numbers)
# while True:
#     print(next(c_iter))

