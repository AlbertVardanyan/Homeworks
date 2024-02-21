# def func(a, b):
#     if a > b:
#         return f'{a} is MAX'
#     else:
#         return f'{b} is MAX'
# print(func(5, 4))
# ==================================================
# def func(numbers):
#     res = 0
#     for i in numbers:
#         res += i
#     return res
# num_list = [1, 6, 6, 8, 6, 3, 5]
# res = func(num_list)
# print(res)
# ==================================================
# def func(numbers):
#     res = 1
#     for i in numbers:
#         res *= i
#     return res
# num_list = [1, 4, 5]
# res = func(num_list)
# print(res)
# ==================================================
# def func(x):
#     resault = 0
#     resault += (x * 1000 // 140 * 0.25 + 4)
#     return resault
# print(func(2.8)) 
# ==================================================
# def func(n):
#     resault = 0
#     resault += (10.95 + 2.95 * (n - 1))
#     return resault
# print(func(5))
# ==================================================
# def func(x, y, z):
#     num = [x, y, z]
#     num.sort()
#     return num[1]
# print(func(60, 30, 15))
# ==================================================
# def func(num):
#     if 1 > num > 12:
#         return ''
#     text = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'] 
#     return text[num - 1]
# print(func(int(input('Enter num 1 - 12: '))))
# ==================================================
# def func(num1, num2, num3):
#     if num1 >= num2 + num3 or num2 >= num1 + num3 or num3 >= num1 + num2:
#         return False
#     elif num1 <= 0 or num2 <= 0 or num3 <= 0:
#         return False
#     else:
#         return True
# print(func(1, 4, 5))
# ==================================================
