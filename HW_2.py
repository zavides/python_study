#1
# list = ['s', 'string', ['array'], 2, 3.0]
# for item in list:
#     print(f"item: {item} type: {type(item)}")

#2
# a = []
# n = int(input("Введите количество элементов списка: "))
# for i in range(n):
#     a.append(int(input()))
#
# for i in range(len(a)):
#     if i % 2 == 0:
#         continue
#     temp = a[i]
#     a[i] = a[i-1]
#     a[i-1] = temp
#
# for i in a:
#     print(i)

#3
# list
# n = int(input("Введите номер месяца: "))
# season_count = 0
# season_list = ["Зима", "Весна", "Лето", "Осень"]
# if n <= 0 or n > 12:
#     print("некоректное значение месяца")
#     exit(-1)
#
# if n > 2 and n < 6:
#     season_count = 1
# if n >=6 and n < 9:
#     season_count = 2
# if n >= 9 and n < 12:
#     season_count = 3
# print(f"Ваш сезон: {season_list[season_count]}")

# dict
# n = int(input("Введите номер месяца: "))
#
# if n <= 0 or n > 12:
#     print("некоректное значение месяца")
#     exit(-1)
#
# season_list = {"Зима": [1,2,12], "Весна": [3,4,5], "Лето": [6,7,8], "Осень": [9,10,11]}
#
# for k, items in season_list.items():
#     if n in items:
#         print(f"Ваш сезон: {k}")

#4
# input_string = input("Введите строки разделеные пробелами: ")
# input_array = input_string.split(" ")
# for item in input_array:
#     if len(item) > 10:
#         print(item[0:10])
#     else:
#         print(item)

#5
# my_list = [7, 5, 3, 3, 2]
# while True:
#     n = int(input("Введите натуральное число: "))
#     isInsert = False
#     for i, number in reversed(list(enumerate(my_list))):
#         if number >= n:
#             my_list.insert(i, n)
#             isInsert = True
#             break
#     if not isInsert:
#         my_list.insert(0,n)
#
#     for item in my_list:
#         print(item, end=" ")


