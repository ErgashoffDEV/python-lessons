# ITEMS() METODI: Bu metod bilan juftliklarni chiqarish mumkin
# honda = {
#     "model": "Civic",
#     "year": 2021,
#     "color": "blue",
#     "mileage": 15000
# }
# print(honda.items())

# for bilan tushunarliroq qilib items()ni chiqarish
# for key, value in honda.items():
#     print(f"{key}: {value}")

# KEYS() METODI: Bu metod bilan dictionaryda kalitlarni(keylarni) chiqarish mumkin
# honda = {
#     "model": "Civic",
#     "year": 2021,
# }
# for key in honda.keys():
#     print(f"{key}")

# SORTED() - Dictionaryda elementlarni tartib bilan chiqaradi
# honda = {
#     "model": "Civic",
#     "year": 2021,
#     "average": 200
# }
# for key in sorted(honda):
#     print(f"{key.title()}")

# VALUES() - Bu metod bilan dictionaryda qiymatlarni(valuelarni) chiqarish mumkin
# honda = {
#     "model": "Civic",
#     "year": 2021,
#     "average": 200
# }
# for key in honda.values():
#     print(f"{key.title()}")

# SET METODI - Bu metod bilan dictionarydagi takrorlangan elementlardan bittasini qoldiradi kak sortirovka
# honda = {
#     "model": "Civic",
#     "year": 2021,
#     "average": 200,
#     "km/h": 200
# }
# for key in set(honda.values()):
#     print(f"{key}")

# SET() MALUMOT TURI - Bu malumot turida bir xil elementlar bolmaydi, tartibda saqlanmaydi, indeks bilan murojaat qilib
# bolmaydi
# toys = {'toy', 'boy', 'oy', 'toy'}
# print(toys)

# AMALIYOT:
# my_dict = {
#     'apple': 1,
#     'banana': 2,
#     'orange': 3,
#     'grape': 4,
#     'kiwi': 5,
#     'watermelon': 6,
#     'mango': 7,
#     'pineapple': 8,
#     'pear': 9,
#     'peach': 10
# }
#
# for key, value in sorted(my_dict.items()):
#     print(f"{key.title()}: {value}")

# countries = {
#     'USA': 'Washington, D.C.',
#     'Canada': 'Ottawa',
#     'Mexico': 'Mexico City',
#     'Brazil': 'Brasília',
#     'United Kingdom': 'London',
#     'France': 'Paris',
#     'Germany': 'Berlin',
#     'Spain': 'Madrid',
#     'Japan': 'Tokyo',
#     'Australia': 'Canberra'
# }
# for key in sorted(countries.keys()):
#     print(key)

# for value in sorted(countries.values()):
#     print(value)

# poytaxt = str(input('Biron davlat kiriting: '))
# print(countries.get(poytaxt, 'Bizda bu davlat haqida malumot yoq'))

# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f'{n + 1}-ovaqtni kiriting: '))
#
# for buyurtma in buyurtmalar:
#     if buyurtma in countries:
#         print(countries[buyurtma])
#     else:
#         print('Bizda bu narsa yoq')

# MAINPOINTS:
# items(), keys(), values(), sorted(), set(), set-malumot turi

