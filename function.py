# CREATION OF FUNCTION:
# def greet():        # funksiya boshi
#     print('Hey, yoo')
# greet()             # funksiyani chaqirish

# FUNKSIYAGA PARAMETR BERISH: FUNKSIYAGA BIR NECHTA PARAMETR UZATISH MUMKIN
# def greet(name, surname):      # qavsni ichida PARAMETR
#     print('Hey yooo', name.title())
# greet('Mirfayz')      # qavsni ichida ARGUMENT

# DOCSTRING - kak podskazka ishlaydi dasturchilar uchun
# def meaning():
#     """Docstring shu tarzda uchta qoshtirnoq bilan yoziladi"""
# meaning()
# print(meaning.__doc__) - docstringni konsolga chiqarish

# ARGUMENTGA PARAMETR NOMI BILAN MUROJAAT QILISH:
# def greet(name, surname):
#     print(f"{name.title()} {surname.title()}")
# greet(name='mirfayz', surname='irgashev')

# PARAMETRGA STANDART QIYMAT BERISH
# def yosh_hisobla(tugilgan_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# AMALIYOT:
# def find_birth_date(name, age):
#     print(f'{name.title()} {2023-age}-yilda tugilgansiz')
# find_birth_date('mirfayz', 30)

# def calculate(number):
#     print(f'{number}: {number ** 2} kvadrat, {number**3} kub')
# calculate(10)

# def even_odd(number):
#     if number % 2 == 0:
#         print(f"{number} soni juft")
#     else:
#         print(f"{number} soni toq")
# even_odd(10)

# def numurate(x, y=2):
#     print(f"{x} and {y}")
# numurate(5)

# def evaluate(first_number, second_number):
#     if first_number > second_number:
#         print(first_number)
#     elif first_number < second_number:
#         print(second_number)
#     else:
#         print('Sonlar teng')
# evaluate(10, 10)

# def read(number):
#     for n in list(range(2, 11)):
#         if number % n == 0:
#             print(n)
# read(20)

# MAINPOINTS:
# function, docstring, parametr, argument
