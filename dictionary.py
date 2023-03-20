# CREATION OF DICTIONARY:
# Dictionary ikkita elementdan oborat boladi, key va value
# car = {'model': 'Supra', 'color': 'red'}

# print(car['model'])   dictionarydan element olish value bilan

# car['country'] = 'USA'  dictionaryga yangi juftlik qoshish

# Dictionarydan juftlikni ochirish
# car = {'model': 'Supra', 'color': 'red'}
# del car['model']

# GET METODI:
# GET metodi xuddi search va if-elsening jamlanmasiga oxshaydi. Dictionarydan elementni qidirib koradi, agar element bolsa
# elementni qaytaradi, agar bolmasa boshqa amalni bajaradi.
# car = {'model': 'Supra', 'color': 'red'}
# el = car.get('country', 'Bunday element mavjud emas')
# print(el)

# AMALIYOT:
# father = {
#     'name': 'Umid',
#     'city': 'Bukhara',
#     'date': 1983
# }
# print(f"Otamning ismi {father['name']}, {father['date']}-yilda, {father['city']}da tug'ilgan")

# meals = {
#     'Ali': 'osh',
#     'Vali': 'manti',
#     'Said': 'qatiq'
# }
# print(f"Alining sevimli taomi {meals['Ali']}")
# print(f"Valining sevimli taomi {meals['Vali']}")

# language_dict = {
#     "Python": "A high-level, interpreted programming language.",
#     "Interpreter": "A program that reads and executes code in real-time.",
#     "Syntax": "The set of rules that defines the structure and format of Python code.",
#     "Variable": "A named storage location in memory that holds a value.",
#     "List": "A collection of items, ordered and mutable.",
#     "Tuple": "A collection of items, ordered and immutable.",
#     "Dictionary": "A collection of key-value pairs, unordered and mutable.",
#     "Function": "A reusable block of code that performs a specific task.",
#     "Module": "A file containing Python code that can be imported and used in other programs.",
#     "Exception": "An error that occurs during the execution of a Python program.",
# }

# GET METHOD:
# termin = str(input('Atama kiriting: '))
# print(language_dict.get(termin, 'Bunday atama mavjud emas'))

# IF_ELSE:
# termin = str(input('Atama kiriting: '))
# if termin in language_dict:
#     print(language_dict[termin])
# else:
#     print('Bizda bunday atama mavjud emas')

# MAINPOINTS:
# creation of dictionary, editing, deleting, get()
