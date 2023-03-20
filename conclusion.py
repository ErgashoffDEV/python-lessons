# father = {
#     'name': 'Umidjon',
#     'date_of_birth': '1983',
#     'city': 'Buxoro'
# }
#
# mother = {
#     'name': 'Nargiza',
#     'date_of_birth': '1984',
#     'city': 'Buxoro'
# }
#
#
# print(f"{father['name']} {father['date_of_birth']}-yilda {father['city']}da tug\'ilgan")
# print(f"{mother['name']} {mother['date_of_birth']}-yilda {mother['city']}da tug\'ilgan")

# favourite_meal = {
#     'Said': 'osh',
#     'Asil': 'salat',
#     'Nurik': 'sushi',
#     'Amir': 'manti'
# }
#
# print(f"Alining sevimli taomi {favourite_meal['Said']}")

# python_izohli_lugati = {
#     'integer': "Butun son",
#     'float': "O'nlik son",
#     'string': "Matn",
#     'list': "Ro'yxat",
#     'tuple': "O'zgarmas ro'yxat"
# }

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

# for key, value in sorted(python_izohli_lugati.items()):
#     print(f"{key} == {value}")

# for key in sorted(python_izohli_lugati.keys()):
#     print(key.title())
#
# for value in sorted(python_izohli_lugati.values()):
#     print(value.lower())

# countries = {
#     'Uzbekistan': 'Tashkent',
#     'Greece': 'Afina'
# }
# country = input('Biron davlat kiriting: ')
# print(countries.get(country, 'Bunday davlat mavjud emas'))

# menu = {
#     'osh': 10,
#     'manti': 5,
#     'sushi': 6,
#     'rolli': 7,
#     'makaron': 9
# }
#
# savat = []
#
# for n in range(3):
#     meal = input(f'{n+1}-ovqatga nima yeysiz?')
#     savat.append(meal)
#
# for savatcha in savat:
#     if savatcha in menu:
#         print(f"{menu[savatcha]}")
#     else:
#        print("Yo'qol")
#
# alisher_navoiy = {
#     'masterpiece': 'Xamsa'
# }
#
# bobur = {
#     'masterpiece': 'Agra'
# }
#
# abdulla_avloniy = {
#     'masterpiece': 'Turkiston'
# }
#
# alisher_navoiy['ism'] = "Alisher Navoiy"
# bobur['ism'] = 'Zahiriddin Muhammad Bobur'
# abdulla_avloniy['ism'] = 'Abdulla Avloniy'
#
# arboblar = [alisher_navoiy, bobur, abdulla_avloniy]
#
# for arbob in arboblar:
#     print(f"{arbob['ism']}ning mashhur asari - {arbob['masterpiece']}")

# favourite_movies = {
#     'Malika': ['Megan', 'Shiro'],
#     'Ali': ['Vali', 'Salim']
# }
#
# for key, movie in favourite_movies.items():
#     print(f"{key}ning yoqtirgan filmlari: {movie}")

# davlatlar = {
#     "o'zbekiston": {'poytaxt': "toshkent",
#                     'maydon': 448978,
#                     'aholi': 33_000_000,
#                     'pul birligi': "so'm"
#                     },
#     "rossiya": {'poytaxt': "moskva",
#                 'maydon': 17_098_246,
#                 'aholi': 144_000_000,
#                 'pul birligi': "rubl"
#                 },
# }
#
# country = input('Biron davlat kiriting: ')
# print(davlatlar.get(country, 'Error'))

# question = "Yaxshi ko'rgan kitobizni yozing. "
# question += "Bu jarayonni to'xtatish uchun STOP deb yozing. "
#
# while True:
#     value = input(question)
#     if value == 'stop':
#         break
# print("Dastur tugadi")

# savol = "Musbat son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     qiymat = int(input(savol))
#     if qiymat < 0:
#         continue
#     elif qiymat == 'exit':
#         break
#     else:
#         print(f"{qiymat} ning ildizi {float(qiymat) ** 0.5} ga teng")
# print('Dastur tugadi')


# while True:
#     price = input('Chipta kerakmi?')
#     if price == 'exit' or price == 'quit':
#         break
#     age = int(price)
#
#     if age <= 7:
#         print(f'Chipta narxi 2000 so\'m')
#     elif 7 <= age < 18:
#         print(f"Chipta narxi 3000 so\'m")
#     elif 18 < age <= 65:
#         print(f"Chipta narxi 10000 so\'m")
#     elif age > 65:
#         print('Kirish bepul')
#
# print("Xaridingiz uchun rahmat")

# ismlar = []
# n = 1  # ismlarni sanash uchun o'zgaruvchi
# while True:
#     ism = input(f"{n}-do'stingiz ismini kiriting:")
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     n += 1
#     if javob == "yo'q":
#         break

# dostlar = {}
# while True:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)  # ism kalit, yosh qiymat
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         break
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
# while 'nexia' in cars:  # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia')  # nexia ni ro'yxatdan olib tashla
# print(cars)

# orders = []
# while True:
#     order = input(f'Buyurtma berishingiz mumkin: ')
#     orders.append(order)
#     javob = input(f"Yana buyurtma bermoqcchisizmi (ha/yo'q)?: ")
#     if javob == "yo'q":
#         break
#
# print('Siz buyurtma bergan ovqatlar')
# for order in orders:
#     print(f"{order.title()}")

# orders = {}
# while True:
#     order = input(f'Buyurtma berishingiz mumkin: ')
#     price = input(f"Buyurtma ni narxi qancha?: ")
#     print(f"{order.title()} savatga qo'shildi va uning narxi {price} so'm")
#     javob = input(f"Yana buyurtma bermoqcchisizmi (ha/yo'q)?: ")
#     orders[order] = int(price)
#
#     if javob == "yo'q":
#         break
#
# print('Siz buyurtma bergan ovqatlar')
# for order, price in orders.items():
#     print(f"{order.title()}. Narxi {price} so'm")
# ask = input(f'Mahsulotni tekshiring: ')
# print(orders.get(ask, 'Bizda bunday mahsulot yoq'))

# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}
#
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} - {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")

