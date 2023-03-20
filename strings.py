# Pythonda turli xil belgilarni qoshish uchun UNICODE saytidan foydalanamiz.

# Matnlarni qoshish uchun + dan foydalanamiz:
# phone = 'Redmi Note 12 Pro'
# print('Mening telefonim ' + phone)

# phone_production = 'Redmi'
# phone_model = 'Note 12 Pro'
# print('Mening telefonim ' + phone_production + ' ' + phone_model)

# F-STRING usuli:
# laptop = 'Macbook Air M1'
# print(f'Menda {laptop} bor')

# STRING METODLARI
# \t bilan boshliq qoshish mumkin:
# print('Mening ismim \tMirfayz')

# \n bilan matnni boshqa qatordan boshlash mumkin:
# print('Assalom deganda ochiladi gul,\nAssalom deganda sayraydi bulbul')

# upper() - barcha elementlarni kattalashtiradi.
# ism = 'Mirfayz'
# print(ism.upper())
# MIRFAYZ

# lower() - barcha elementlarni kichiklashtiradi.
# ism = 'Mirfayz'
# print(ism.lower())
# mirfayz

# title() - sozdagi birinchi harfni kattalashtiradi.
# ism = 'mirfayz irgashev'
# print(ism.title())
# Mirfayz Irgashev

# capitalize() - sozdagi eng birinchi harfni kattalashtiradi.
# ism = 'mirfayz irgashev'
# print(ism.capitalize())
# Mirfayz irgashev

# strip() - matn boshi va oxiridagi boshliqlarni ob tashlaydi
# apple = '       apple         '
# print(apple.strip())

# lstrip() - matn boshidagi boshliqlarni olib tashlaydi
# apple = '       apple         '
# print(apple.lstrip())

# rstrip() - matn oxiridagi boshliqlarni olib tashlaydi
# apple = '       apple         '
# print(apple.rstrip())

# BU METODLAR OZGARUVCHI ICHIDAGI ASL MATNNI OZGARTIRMAYDI


# INPUT - foydalanuvchiga qiymatni ozi berish imkoniyatini taqdim qilish.
# ism = input('Nomat chi?: ')
# print(f'Chto {ism.title()}')

# AMALIYOT:
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = 'Bodomzor'
# shahar = 'Samarqand'
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {shahar} shahri")

# kocha = str(input("Ko'chani nomini kiriting: "))
# mahalla = str(input("Mahallani nomini kiriting: "))
# tuman = str(input("Tumanni nomini kiriting: "))
# shahar = str(input("Shaharni nomini kiriting: "))
# print(f"{kocha.title()} ko'chasi,\n{mahalla.title()} mahallasi,\n{tuman.title()} tumani,\n{shahar.title()} shahri")

# manzil = f"{kocha.title()} ko'chasi,\n{mahalla.title()} mahallasi,\n{tuman.title()} tumani,\n{shahar.title()} shahri"
# print(manzil.title())
# print(manzil.upper())
# print(manzil.lower())
# print(manzil.capitalize())

# MAINPOINTS:
# "+" bilan matnlarni qoshish
# f-string
# \t, \n
# upper(), lower(), title(), capitalize(), strip(), lstrip(), rstrip()
# INPUT()







