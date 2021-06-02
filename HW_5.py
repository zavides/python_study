#1
# f = open('text.txt', 'w')
# while True:
#     line = input()
#     if line == "":
#         break
#     f.write(line + '\n')
# f.close()

#2
# f = open('text.txt', 'r')
# lines = f.readlines()
# f.close()
# print(f"Количество строк: {len(lines)}")
# for number, line in enumerate(lines):
#     print(f"Количество символов в строке {number + 1}: {len(line)}")

#3
# f = open('employ.txt', 'r', encoding="utf-8")
# lines = f.readlines()
# f.close()
# count_employ = len(lines)
# sum_salary = 0
# for line in lines:
#     employ = line.split(" ")
#     salary = int(employ[1])
#     if salary < 20000:
#         print(f"Сотрудник {employ[0]}: {salary}")
#     sum_salary += salary
# print(f"Средняя зарплата сотрудников: {sum_salary/count_employ}")

#4
# f = open('numbers_en.txt', 'r', encoding='utf-8')
# lines = f.readlines()
# f.close()
# dict_numbers = {"One": "Один", 'Two': "Два", "Three": "Три", "Four": "Четыре"}
# f = open("numbers_ru.txt", 'w', encoding='utf-8')
# for line in lines:
#     pair = line.split(" — ")
#     f.write(f"{dict_numbers[pair[0]]} - {pair[1]}")
# f.close()

#5
# import random
# random_list = []
# for i in range(0, 10):
#     n = random.randint(1, 1000)
#     random_list.append(n)
# f = open("numbers.txt", 'w', encoding='utf-8')
# for number in random_list:
#     f.write(f"{number} ")
# f.close()
# f = open("numbers.txt", 'r', encoding='utf-8')
# line = f.readlines()
# numbers = line[0].rstrip().split(" ")
# sum = 0
# for number in numbers:
#     sum += int(number)
# print(f"Результат: {sum}")
# f.close()

#6
# f = open('lect.txt', 'r', encoding="utf-8")
# lines = f.readlines()
# f.close()
# dict = {}
# for line in lines:
#     parse = line.rstrip().split(" ")
#     name = parse[0].rstrip(":")
#     count_hours = 0
#     for hour in parse[1:]:
#         res = int('0' + "".join([i for i in hour if i.isdigit()]))
#         count_hours += res
#     dict[name] = count_hours
# print(dict)

#7
# import json
# lines = []
# dict_firm = {}
# average_profit = 0
# count_positive_firm = 0
# with open('firms.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
# for line in lines:
#     firm = line.rstrip().split(" ")
#     profit = int(firm[2]) - int(firm[3])
#     if profit > 0:
#         average_profit += profit
#         count_positive_firm += 1
#     dict_firm[firm[0]] = profit
#
# res = [dict_firm, {"average_profit": average_profit/count_positive_firm}]
# with open('data.json', 'w') as outfile:
#     json.dump(res, outfile)
