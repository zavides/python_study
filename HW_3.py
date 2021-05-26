#1
# def devide(a, b):
#     if b == 0:
#         print("На ноль делить нельзя")
#         exit(0)
#     return a / b
#
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print(f"Результат: {devide(a,b)}")

#2
# def print_info(name, last_name, burn_year, city, email, phone_number):
#     print(f"Информация о пользователе: Имя: {name}, Фамилия: {last_name}, год рождения: {burn_year}, город: {city}, "
#           f"почта: {email}, номер телефона: {phone_number}")
#
#
# name = input("Введите имя пользователя: ")
# last_name = input("Введите фамилию: ")
# burn_year = input("Введите год рождения: ")
# city = input("Введите город проживания: ")
# email = input("Введите email: ")
# phone_number = input("Введите номер телефона: ")
#
# print_info(name=name, last_name=last_name, burn_year=burn_year, city=city, email=email, phone_number=phone_number)

#3
# def find_max_sum(a,b,c):
#     array = sorted({int(a),int(b),int(c)}, reverse=True)
#     print(array)
#     return array[0] + array[1]
#
#
# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# c = input("Введите третье число: ")
# print(f"Результат: {find_max_sum(a,b,c)}")

#4
# def manual_polinom(a: float, b: int):
#     if b == 0:
#         return 1
#     if b == -1:
#         return 1/a
#     delit = a ** abs(b)
#     return 1/delit
#
#
# a = int(input("Введите число: "))
# b = int(input("Введите отрицательную степень: "))
# print(f"Результат: {manual_polinom(a,b)}")

#5
# result = 0
# exit = False
# while True:
#     array_numbers = input("Введите строку чисел разделённых пробелами. Для выхода введите букву 'q': ").split(" ")
#     for chars in array_numbers:
#         if chars == 'q':
#             exit = True
#             break
#         result += int(chars)
#     if result != 0:
#         print(f"Результат: {result}")
#     if exit:
#         print("Выход из программы.")

#6
# def int_func(s):
#     result = s[0].upper()
#     result = result + s[1:]
#     return result
#
#
# input_string = input('Введите строку: ')
# print(f"Результат: {int_func(input_string)}")