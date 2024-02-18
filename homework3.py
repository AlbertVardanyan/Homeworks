# a = 15
# b = 12
# for i in range(a, a * b + 1, a):
#     if i % b == 0:
#      print(i)
#      break
#=============================================
# odd = 0
# even = 0

# for i in range(1, 101):
#    if i % 2 == 0:
#       even += 1
#    else:
#       odd += 1

# print(f'even numbers: {even}')
# print(f'odd numbers: {odd}')
#=============================================
# string = input('Write any word and number: ')
# str = 0
# num = 0
# for i in string:
#     if i.isdigit():
#         num += 1
#     elif i.isalpha():
#         str += 1

# print(f'number count: {num}')
# print(f'string count: {str}')
#=============================================
# age = int(input('your age: '))
# gender = input('your gender male/famale: ').lower()

# if 18 <= age <= 20 and gender == 'male':
#     print('duq hamapatasxanum eq')
# else:
#     print('duq cheq hamapatasxanum')
#=============================================
# num = 1
# n = int(input('Enter num: '))
# for i in range(1, n + 1):
#     num *= i
# print(num)
#=============================================
# num = 0
# count = 0
# a = int(input('Enter num1: '))    
# b = int(input('Enter num2: '))    
# if a > b:
#     for i in range(b, a + 1):
#         num += i
#         count += 1
# else:
#     for i in range(a, b + 1):
#         num += i
#         count += 1
# print(num / count)
#=============================================
# for i in range(10, 101):
#     if i % 3 == 0:
#         print(i)
#=============================================
# count = 0
# for i in range(100, 1, -4):
#     count += 1
#     print(f'Месяц {count} осталось--->{i}kg')
#=============================================
# price = 0
# m = int(input('кол-во должников: '))
# for i in range(0, m, 5):
#     a = int(input('сколько должны ? '))
#     price += a
# print(price)
#=============================================
# for i in range(1, 11):
#     word = input('напишите слово для капитана: ').lower()
#     if word == 'карамба':
#         break
# print('вы приняты')
#=============================================
# count = 0
# num = (input('Enter num: '))
# for i in num:
#     if i.isdigit():
#          count += int(i)
# print(count)
#=============================================
# count = 0
# for i in range(1, 13):
#     money = int(input('ваша зарплата за каждый месяц: '))
#     count += money
# print(count)
#=============================================
# three = int(input('сколько человек получили тройку: '))
# four = int(input('сколько человек получили черверку: '))
# five = int(input('сколько человек получили пятерку: '))
# if five < three > four:
#     print('больше всего троечников')
# elif three < four > five:
#     print('больше всего хорошистов')
# elif three < five > four:
#     print('больше всего отличников')
# else:
#     print('все по равну')
#=============================================
# num = 0
# count = 0
# a = int(input('Enter num1: '))    
# b = int(input('Enter num2: '))    
# if a > b:
#     for i in range(b, a + 1):
#         if i % 3 == 0:
#             num += i
#             count += 1
# else:
#     for i in range(a, b + 1):
#         if i % 3 == 0:
#             num += i
#             count += 1
# print(num / count)
#=============================================
