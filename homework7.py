# Ex 1. 
# =========================================
# mydict = {
#     'a':15,
#     'b':20,
#     'c':5,
#     'd':10
# }
# myv = sorted(mydict.values())
# print(myv)
# =========================================
# Ex 2.
# =========================================
# mydict = {
#     'a':15,
#     'b':20,
#     'c':5,
# }
# mydict['d'] = 10
# print(mydict)
# =========================================
# Ex 3.
# =========================================
# mydict = {
#     'a':15,
#     'b':20,
#     'c':5,
# }
# print('a' in mydict)
# =========================================
# Ex 5.
# =========================================
# value = 1
# mydict = {
#     'a':15,
#     'b':1,
#     'c':2,
# }
# for i in mydict.values():
#     value *= i
# print(value)
# =========================================
# Ex 6.
# =========================================
# mydict = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# val = sorted(mydict.values(), reverse = True)
# print(val[:3])
# =========================================
# Ex 1.
# =========================================
# mydict = {
#     'Albert': 10,
#     'Gago': 3,
#     'Vzgo': 4,
#     'Artak': 2,
#     'Lyova': 5,
#     'Shirak': 9,
#     'Narine': 6,
#     'Vardan': 1,
#     'Tyom': 10,
#     'Lara': 7,
# }
# print(mydict)
# =========================================
# Ex 2.
# =========================================
# count = 0
# num = 0
# mydict = {
#     'Albert': 10,
#     'Gago': 3,
#     'Vzgo': 4,
#     'Artak': 2,
#     'Lyova': 5,
#     'Shirak': 9,
#     'Narine': 6,
#     'Vardan': 1,
#     'Tyom': 10,
#     'Lara': 7,
# }
# for i in mydict.values():
#     count += 1
#     num += i
# print(f'the arithmetic average of rating students: {num / count}')
# =========================================
# Ex 3. 4. 5.
# =========================================
# mydict = {
#     'Albert': 10,
#     'Gago': 3,
#     'Vzgo': 4,
#     'Artak': 2,
#     'Lyova': 5,
#     'Shirak': 9,
#     'Narine': 6,
#     'Vardan': 1,
#     'Tyom': 10,
#     'Lara': 7,
# }
# good = [student for student, i in mydict.items() if i > 5]
# bad = [student for student, i in mydict.items() if i <= 5]
# print('good students')
# for student in good:
#     print(student)
# print('bad students')
# for student in bad:
#     print(student)
# =========================================
# Ex 6. Name
# =========================================
# mydict = {
#     'Albert': 10,
#     'Gago': 3,
#     'Vzgo': 4,
#     'Artak': 2,
#     'Lyova': 5,
#     'Shirak': 9,
#     'Narine': 6,
#     'Vardan': 1,
#     'Tyom': 10,
#     'Lara': 7,
# }
# name = input('Enter name: ')
# for i in mydict.items():
#     if name in i:
#         print(i)
#         break
# else:
#     print('name not found')
# =========================================

# =========================================
