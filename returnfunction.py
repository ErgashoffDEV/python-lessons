# RETURN - xuddi printdek ishlaydi lekin buning asosiy vazifasi berilgan funksiyadan bir necha marta foydalanish
# uchun yordam berish. Funksiyani biron bir ozgaruvchiga yuklash muhim.
# def message(name, surname):
#     full_name = f"{name.title()} {surname.title()}"
#     return full_name
# man = message('mirfayz', 'irgashev')

# FUNKSIYA ICHIDAGI OZGARUVCHILAR ICHKI YOKI MAHALLIY VARIABLE DEYILADI. OR LOCAL VARIABLES

# IXTIYORIY ARGUMENTLAR YARATISH - bunda user xohlasa argument kiritadi, xohlasa yoq
# def desirable_creation(name, surname=''):    #prosta bosh qoldirsa boldi ixtiyoriy argument uchun
#     full_name = f"{name} {surname}"
#     return full_name
# message = print(desirable_creation("Mirfayz"))

# FUNKSIYA ICHIDA DICTIONARY:
# def auto_info(company, model, color, price):
#     auto = {
#         'company': company,
#         'model': model,
#         'color': color,
#         'price': price
#     }
#     return auto
# first_auto = auto_info('BMW', 'Maybach', 'Black', 30000)
# second_auto = auto_info('TOYOTA', 'Supra', 'White', 20000)
# autos = [first_auto, second_auto]
# for auto in autos:
#     print(f"Company: {auto['company']}, "
#           f"Model: {auto['model']}, "
#           f"Color: {auto['color']}, "
#           f"Price: {auto['price']} ")

# FUNKSIYA ICHIDA LIST + RANGE
# def gap(min, max):
#     numbers = []
#     while min < max:
#         numbers.append(min)
#         min += 1
#     return numbers
# print(gap(0,5))

# FUNKSIYA + SIKL
# def auto_info(company, modell, color, machine, date, price):
#     auto = {
#         'company': company,
#         'model': modell,
#         'color': color,
#         'machine': machine,
#         'date': date,
#         'price': price
#     }
#     return auto
#
#
# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end='')
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#
#     avtolar.append(auto_info(kompaniya, model, rangi, korobka, yili, narhi))
#
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break

# AMALIYOT:
# def mijoz_info(ism, familiya, tyil, tjoy, email='',tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'yoshi':2020-tyil,
#              'tjoy':tjoy,
#              'email':email,
#              'telefon':tel}
#     return mijoz
#
# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar =[]
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break
#
# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#           f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}")

# def calculate(first, second, third):
#     if first > second and first > third:
#         print(first)
#     elif second > first and second > third:
#         print(second)
#     else:
#         print(third)
# calculate(5, 0, 10)

# MAINPOINTS:
# RETURN, ixtiyoriy argument, funskiya ichida dictionary, funksiya ichida list, funksiya + sikl