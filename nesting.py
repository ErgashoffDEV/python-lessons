# LIST ICHIDA DICTIONARY:
# fruits = {
#     "apple": "red",
#     "banana": "yellow",
#     "kiwi": "brown",
#     "orange": "orange",
#     "grape": "purple"
# }
# languages = {
#     "Python": "Guido van Rossum",
#     "Java": "James Gosling",
#     "JavaScript": "Brendan Eich",
#     "C++": "Bjarne Stroustrup",
#     "Ruby": "Yukihiro Matsumoto"
# }

# dictionaries = [fruits, languages]
# for dictionary in dictionaries:
#     print(dictionary)

# Indeks boyicha murojaat qilish:
# dictionaries = [fruits, languages]
# print(dictionaries[0]['orange'])

# Bosh royxatni dictionary bilan toldirish
# cars = []
# for number in range(3):
#     car = {
#         "brand": "Toyota",
#         "model": "Camry",
#         "year": 2022,
#         "color": "Silver",
#         "transmission": "Automatic",
#         "price": 26750.00
#     }
#     cars.append(car)
# for car in cars:
#     print(car)

# Dictionary ichida list:
# dasturchilar = {
#     'ali': ['python', 'c++'],
#     'vali': ['html', 'css', 'js'],
# }
# for key, value in dasturchilar.items():
#     print(f"{key.title()} quyidagi dasturlash tillarini biladi: ")
#     for val in value:
#         print(val)

# Dictionary ichida dictionary: tavsiya etilmaydigan metod
# hamkasblar = {
#     'ali': {'familiya': 'valiyev',
#             'tyil': 1995,
#             'malumot': 'oliy',
#             'tillar': ['python', 'c++']
#             },
#     'vali': {'familiya': 'aliyev',
#              'tyil': 2001,
#              'malumot': "o'rta-maxsus",
#              'tillar': ['html', 'css', 'js']}
# }

# end - printni oxiriga biron narsa qoshish uchun
# print('Hello', end='')
# print('world')

# AMALIYOT:
# languages = {
#     "Python": "Guido van Rossum",
#     "Java": "James Gosling",
#     "JavaScript": "Brendan Eich",
#     "C++": "Bjarne Stroustrup",
#     "Ruby": "Yukihiro Matsumoto"
# }
# languages1 = {
#     "Python": "Guido van Rossum",
#     "Java": "James Gosling",
#     "JavaScript": "Brendan Eich",
#     "C++": "Bjarne Stroustrup",
#     "Ruby": "Yukihiro Matsumoto"
# }
# dicts = [languages, languages1]
# dicts[0]['R'] = 'Mark Zuckerberg'
# dicts[1]['R'] = 'Steve Jobs'
# for language in dicts:
#     print(language['R'])

# fav_movies = {
#     'Ali': ['Megan', 'Meg'],
#     'Vali': ['Megan', 'Meg'],
#     'Said': ['Megan', 'Meg']
# }
# for key, value in fav_movies.items():
#     print(f"{key}ning sevimli kinolari: ")
#     for val in value:
#         print(val)

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
#     "aqsh": {'poytaxt': "vashington",
#              'maydon': 9_631_418,
#              'aholi': 327_000_000,
#              'pul birligi': "dollar"},
#     "malayziya": {'poytaxt': "kuala-lumpur",
#                   'maydon': 329750,
#                   'aholi': 25_000_000,
#                   'pul birligi': "rinngit"}
# }

# country = input('Biron davlat kiriting: ')
# print(davlatlar.get(country, 'Bizda bunday davlat yoq'))       FIRST WAY

# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")       SECOND WAY

# MAINPOINTS:
# dictionary ichida list, list ichida dictionary, bosh listni dictionary bilan toldirish