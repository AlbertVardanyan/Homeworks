#Lesson 2
# 1. Write a python program which have two input and compute the area 
# of a rectangle.

# a = int(input('Enter number: '))
# b = int(input('Enter number: '))
# S = a * b
# print(S)


#2. Write a python program which have one input and compute the area 
#of a square.

# a = int(input('Enter number: '))
# S = a**2 
# print(S)


#3. Create 20 legal variables. for example: country =“Armenia”

# myname = 'Albert'
# MyName = 'Albert'
# My2Name = 'Albert'
# My_name_Is = 'Albert'
# _Name = 'Albert'
# etc.


# 4. Write a python program which will check the type of your 
# variables.(int, str , float , bool)

# a = 4
# b = 'Albert'
# c = 5.5
# print(type(a), type(b), type(c))

#-----------------------------------------------------------
#Lesson 3

#1. Write code to print pypypypython

# text1 = 'pypypypython'
# print(text1)


#2.Write code to print 7p7p7p79

# text2 = '7p7p7p79'
# print(text2)


#3.Write code to print 9999999
# text3 = 9999999
# print(text3)


#4.Write a Python program that checks how much money you have on your card. 
# At first, your balance is 0, and you have 3 inputs and add each of them to the 
# card

# card = 0
# card +=(int(input()))
# card +=(int(input()))
# card +=(int(input()))
# print(card)


#5.Create 7 legal variables and check type of them.

# a = 0.7
# MyCountry = 'Hayastan'
# My_City = 'Byureghavan'
# _My_Name_Is = 'Albert'
# b = 24
# _HeLLo_WOrLd = 'Hello World'
# My2name = 'Davit'

# print(type(a), type(MyCountry), type(My_City), type(_My_Name_Is), type(b), type(_HeLLo_WOrLd), type(My2name) )


# 7.Create a python program which convert the pound in 
# kilograms.

# pound = float(input('Enter number: '))
# kg = pound * 0.45
# print(f'{kg}(kilogram)')


# 8.Create a python program which convert the miles in 
# kilometers.

# miles = (float(input("Enter number: ")))
# km = miles * 1.6
# print(f'{km}(kilometer)')

#------------------------------------------------------------
#Lesson 4

# 1. You have one input where you write  
# number (Celsius) and your program will say  
# how much fahrenheit is your Celsius.

# C = float(input('Enter Number: '))
# F = C * 9/5 + 32
# print(f'{F}(Fahrenheit)')


# 3. Convert Minutes into Seconds you have one input.

# M = float(input('Enter Number: '))
# S = M * 60
# print(f'{S}(Seconds)')


# 4. Convert Day into Minutes and Seconds you have one 
# input.
# And check the type of result

# D = int(input('Enter number: '))
# M = D * 1440
# S = D * 86400
# print(f'{D}(Day) = {M}(Minutes)\n {D}(Day) = {S}(Seconds)',)


# 5. Write a python program which have 2 input (float or
# int) and two of them less than 90 you will check that 
# triangle have 90 degree angle.

# a = int(input('Enter number: '))
# b = int(input('Enter number: '))
# c = 180-a-b 
# print(c)


# 8.Write a python program which have one  
# input(int or float) and check ,
# if modulo 400 is 0 True, otherwise False.

# a = int(input('Enter number: '))
# b = 400 % a
# print(b == 0)


# 9. You have a wheel: and have one input the  
# radius of wheel and calculate how much  
# meter it will pass after 5 turn.

# Radius = float(input('Enter Number: '))
# Meter = Radius * 3.14 * 5
# print(Meter)

#-----------------------------------------------------
#The Python Workbook

#2.Write a program that asks the user to enter his or her name. The program should
#respond with a message that says hello to the user, using his or her name

# name = input('Enter your name: ')
# print(f'Hello {name}')

# 3.Write a program that asks the user to enter the width and length of a room. Once
# these values have been read, your program should compute and display the area of
# the room. The length and the width will be entered as floating-point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.

# width = float(input('Enter your room width in meters: '))
# length = float(input('Enter your room length in meters: '))
# S = width * length
# print(f'S = {S}(meters)')


#4.Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.

# width = int(input('Enter width in feet: '))
# length = int(input('Enter length in feet: '))
# Sfeet = width * length
# Sacres = Sfeet / 43560
# print(Sacres)


#5.In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and two digits to the right of the decimal point.


# bottle1 = float(input('Enter how many bottles of 1 liter or less do you have?:  '))
# bottle2 = float(input('Enter how many bottles over 1 liter do you have?: '))
# money1 = bottle1 * 0.10
# money2 = bottle2 * 0.25
# both = money1 + money2
# print(f'here\'s your money ${both}')


#8.An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos from the user. Then your program should compute
# and display the total weight of the parts.

# widget = int(input('How many widget do you want to buy?: '))
# gizmo = int(input('How many gizmos do you want to buy?: '))
# total = widget * 75 + gizmo * 112
# print(f'total weight is {total}(gram)')


#9.Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added to the
# balance of the savings account. Write a program that begins by reading the amount of
# money deposited into the account from the user. Then your program should compute
# and display the amount in the savings account after 1, 2, and 3 years. Display each
# amount so that it is rounded to 2 decimal places.

# dep = float(input('write the amount of the initial deposit: '))
# year1 = round(dep * 1.04, 2)
# year2 = round(year1 * 1.04, 2)
# year3 = round(year2 * 1.04, 2)
# print(f'first year {year1}(money)\nsecond year {year2}(money)\nthird year {year3}(money)') 


#10.Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of a**b

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))

# sum = a + b
# dif = a - b
# product = a * b
# quot = a // b
# rem = a % b
# square = a ** b
# print(f'a + b={sum}\na - b={dif}\na * b={product}\na // b={quot}\na % b={rem}\na ** b={square}')
