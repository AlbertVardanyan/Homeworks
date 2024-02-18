# Задача 1. Датчик погоды
#===============================================
# rain = int(input("it's raining ?: "))

# if rain == 1:
#     print('Rain is coming. Take an umbrella!')
# elif rain == 0:
#     print('There is no rain!')
# else:
#     print('Error. Enter 0 or 1')
#===============================================
#Задача 2. Поступление
#===============================================
# point1 = int(input('Enter the number of points in Russian language: '))
# point2 = int(input('Enter the number of points in mathematics: '))
# point3 = int(input('Enter the number of points in computer science: '))
# all = point1 + point2 + point3

# if 300 >= all >= 270:
#     print('Congratulations, you have entered the budget')
# elif 0 < all < 270:
#     print("Unfortunately, you didn't qualify for the budget.")
# else:
#     print('Error: points from 0 to 300')
#===============================================
#Задача 3. Следим за расписанием
#===============================================

# day = int(input('Enter num: '))
# if day % 2 == 0:
#     print('number is even')
# else:
#     print("number is not even(odd)")
#===============================================
#Задача 4. Калькулятор скидки
#===============================================

# price1 = int(input('Enter product price: '))
# price2 = int(input('Enter product price: '))
# price3 = int(input('Enter product price: '))
# price = price1 + price2 + price3

# if price >= 10000:
#     print(f'price - 10% = {price - (price / 10)}')
# elif 0 < price < 10000:
#     print(f'price = {price}')
# else:
#     print('Error. price greater then 0')
#===============================================
#Задача 5. Модуль числа
#===============================================

# x = int(input('Enter number: '))
# if x >= 0:
#     print(x)
# else:
#     print(-x)
#===============================================
#Задача 6. Игра в кубики
#===============================================
# import random
# x1 = random.randint(1, 6)
# x2 = random.randint(1, 6)

# if x1 >= x2:
#     print(f'кубик игрока: {x1}\nкубик владельца: {x2}\n{x1} >= {x2}\nигрок платит\nигра окончена')
# else:
#     print(f'кубик игрока: {x1}\nкубик владельца: {x2} \nсумма: {x1 + x2}\nвладелец платит\nигра окончена')
#===============================================
#Задача 7. Хватит ли зарплаты
#===============================================
# hours = int(input('количество отработанных часов: '))
# credit = int(input('остаток по кредиту: '))
# food = int(input('количество денег на еду: '))
# money = (200 * hours) / (2 ** 3) + hours
# life = food + credit
# if money >= life:
#     print('Часов хватает. Можно отдохнуть')
# else:
#     print('Часов не хватает. Придётся работать больше!')
#===============================================
#Задача 8. Максимальное число
#===============================================
# num1 = int(input('Enter num1: '))
# num2 = int(input('Enter num2: '))
# num3 = int(input('Enter num3: '))
# if num1 >= num2 and num3:
#     print(f'{num1} is MAX')
# elif num2 >= num3 and num1:
#     print(f'{num2} is MAX')
# else:
#     print(f'{num3} is MAX')
#===============================================
# Задача 3. Поступление
#===============================================

# place = int(input('your place: '))
# point = int(input('your points: '))

# if 1 <= place <= 10 and point >= 290:
#     print('Поздравляем, вы поступили!\nБонусом вам будет начисляться стипендия.')
# elif 1 <= place <= 10 and point < 290:
#     print('Поздравляем, вы поступили!\nНо вам не хватило баллов для стипендии.')
# else:
#     print('К сожалению, вы не поступили.')
#===============================================
# Задача 4. Опять двойка
#===============================================

# raiting = int(input('Что получил по математике ?: '))
# if raiting == 2 or raiting == 3:
#     print('Плохо. Марш учится!')
# elif raiting == 4 or raiting == 5:
#     print('Молодец! можешь отдохнуть.')
# else:
#     print('Error')
#===============================================
# Задача 5. Вася хочет выигрывать
#===============================================
# import random
# first = random.randint(1, 4)
# second = random.randint(1, 4)
# third = random.randint(1, 4)
# if first == second == third:
#     print('3')
# elif (first == second) or (second == third) or (first == third):
#     print('2')
# else:
#     print('0')
#===============================================
# Задача 6. Новоселье
#===============================================
# meter = int(input('площядь квартиры: '))
# money = int(input('стоимость квартиры: '))
# if meter >= 100 and money <= 10000000:
#     print('Квартира подходит!')
# elif meter >= 80 and money <= 7000000:
#     print('Квартира подходит!')
# else:
#     print('Квартира не подходит')
#===============================================
# Game
#===============================================
#===============================================
# import random
# import sys

# player = int(input('Enter number from 0 to 5: '))
# MyPoint = 0
# PCpoint = 0
# PC = random.randint(0, 1)

# if player == PC:
#     MyPoint += 1
#     print('player +1 point')
# elif player != PC:
#     PCpoint += 1
#     print('PC +1 point')
# player = int(input('Enter number from 0 to 5: '))
# PC = random.randint(0, 1)
# if player == PC:
#     MyPoint += 1
#     print('player +1 point')
# elif player != PC:
#     PCpoint += 1
#     print('PC +1 point')
# if MyPoint == 2:
#     print('Player WIN. Game Over')
# if PCpoint == 2:
#     print('PC WIN. Game Over')
# if MyPoint == 2 or PCpoint == 2:
#     print(sys.exit())
# else:
#     player = int(input('Enter number from 0 to 5: '))
# PC = random.randint(0, 1)
# if player == PC:
#     MyPoint += 1
#     print('player +1 point')
# elif player != PC:
#     PCpoint += 1
#     print('PC +1 point')
# if MyPoint == 2:
#     print('Player WIN. Game Over')
# if PCpoint == 2:
#     print('PC WIN. Game Over')
#===============================================
#===============================================
# 1. Values
#===============================================
# x1 = int(input('Enter first number : '))
# x2 = int(input('Enter second number : '))
# if x1 > x2:
#     print(f'{x1} is greatest')
# elif x2 > x1:
#     print(f'{x2} is greatest')
# else:
#     print('EQUEL')
#===============================================
# 2. Age
#===============================================
# x1 = int(input('Enter first age: '))
# x2 = int(input('Enter second age: '))
# x3 = int(input('Enter third age: '))
# if x1 >= x2 and x1 >= x3 and x2 >= x3:
#     print(f'{x1} is oldest and {x3} is youngest')
# elif x1 >= x2 and x1 >= x3 and x3 >= x2:
#     print(f'{x1} is oldest and {x2} is youngest')

# elif x2 >= x1 and x2 >= x3 and x1 >= x3:
#     print(f'{x2} is oldest and {x3} is youngest')
# elif x2 >= x1 and x2 >= x3 and x3 >= x1:
#     print(f'{x2} is oldest and {x1} is youngest')

# elif x3 >= x1 and x3 >= x2 and x1 >= x2:
#     print(f'{x3} is oldest and {x2} is youngest')
# elif x3 >= x1 and x3 >= x2 and x2 >= x1:
#     print(f'{x3} is oldest and {x1} is youngest')
#===============================================
# 3.Reverse
#===============================================
# rev = int(input('Enter number: '))
# rev = str(rev)
# print(rev[::-1])
#===============================================



