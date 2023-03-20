# If-Elif-Else ketma-ketligi: Bu ketma-ketlikda biron shart bajarildimi, boldi, boshqa shartlarni Python tekshirmaydi
# ism = input('Programming language: ')
# if ism.lower() == 'python':
#     print('Salom')
# elif ism.lower() == 'javascript':
#     print('Xayr')
# else:
#     print('Lyubaya biznes xarasha')

# OR operatori - bunda shartlardan bittasi bajarilsa agar value Truega teng boladi
# month = input('Oyni kiriting: ')
# if month.lower() == 'dekabr' or month.lower() == 'noyabr':
#     print('Yangi yilga kam qopti')
# else:
#     print('Uxlayveringlar')

# AND operatori - bunda shartlarning barchasi bajarilsagina value True boladi
# day = input('Kunni kiriting: ')
# temperature = int(input('Haroratni kiriting: '))
# if day.lower() == 'yakshanba' and temperature < 30:
#     print('Chomilgani kettik')
# else:
#     print('Hali barvaqt')

# AND va OR operatorlarini aralashtirib yozish:
# kun = input('Kun: ')
# harorat = int(input('Harorat: '))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:

# Shartlarni ketma-ket tekshirish uchun faqat if operatoridan foydalanish kk
# True = 1
# False = 0

# IN va NOT IN:
# Tarkibni tekshirashda kerak boladigan metodlar
# cars = ['GTR']
# check = 'GTR' in cars
# print(check)

# cars = ['GTR']
# check = 'GTR' not in cars
# print(check)

# cars = ['Sakura', 'GTR', 'Supra']
# car = input('Type name of car: ')
# if car in cars:
#     print('Bu mashina bizda bor')
# else:
#     print('Yoqol')

# menu = ['osh', 'manti', 'palov']
# order = ['osh', 'qozon']
# for meal in order:
#     if meal in menu:
#         print(f"Bizda {meal} bor")
#     else:
#         print(f"Bizda {meal} yo'q")

# AMALIYOT:
# number = int(input('JUft son kiriting: '))
# if number % 2 == 0:
#     print('Rahmat')
# else:
#     print('Juft son kiriting')

# age = int(input('Yoshiz nechida? '))
# if age < 4 or age > 60:
#     price = 0
# elif age <= 18:
#     price = 10000
# elif 18 <= age < 60:
#     price = 12000
# print(f"Chipta narxi {price} so'm")

# first_number = int(input('Birinchi sonni kiriting: '))
# second_number = int(input('Ikkinchi sonni kiriting: '))
# if first_number == second_number:
#     print('Sonlar teng')
# elif first_number < second_number:
#     print(f"{first_number} {second_number}dan kichik")
# else:
#     print(f"{first_number} {second_number}dan katta")

# meals = ['Spaghetti', 'Chicken', 'Burger', 'Sandwich', 'Pad Thai', 'Beef', 'Pizza', 'Roasted Chicken', 'Rolls', 'Taco']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(5):
#     savat.append(input(f"{n+1}-ovqatni kiriting: "))
# for meal in savat:
#     if meal in meals:
#         print(bor_mahsulotlar.append(meal))
#     else:
#         print(mavjud_emas.append(meal))


# users = ['said', 'ali', 'vali', 'asil']
# user = input('Login kiriting: ')
# if user.lower() not in users:
#     print("Login band, yangi login tanlang")
# else:
#     print('Salom', user.title())

# number = int(input('Son kiriting: '))
# for n in range(2, 11):
#     if number % n == 0:
#         print(f"{number} {n}ga qoldiqsiz bolinadi")

# MAINPOINTS:
# if-elif-else, or, and, in, not in,




