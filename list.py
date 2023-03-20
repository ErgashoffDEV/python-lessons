# NEW DATA TYPE - LIST

# Creation of list:
# cars = ['Supra', 'Matiz', 'Gentra']

# Listda turli xil data typelar qatnashish mumkin. Arifmetik amallar bajarishda sonlardan ham foydalansa ham boladi
# prices = ['b', 'a', 'a', 1, 2, 3]
# overall = prices[3] + prices[4]
# print(overall)

# Indeks dasturlashda 0dan boshlanadi. Listdagi elementlarga string metodlarini ishlatsa ham boladi.

# Listdagi elementlarni olish:
# cars = ['Supra', 'Matiz', 'Gentra']
# print(cars[0])

# Listda elementlarni ozgartirish
# Elementlarni ozgartirish uchun ozgartirmoqchi bolgan elementni olib, unga yangi value beramiz
# cars = ['Supra', 'Matiz', 'Gentra']
# cars[0] = 'GTR'
# print(cars)

# APPEND() - listning oxiriga element qoshish:
# cars = ['Supra', 'Matiz', 'Gentra']
# cars.append('Nexia')
# print(cars)

# INSERT() - listning lyuboy joyiga element qoshish:
# insert ishlatishda birinchi index keyin value beriladi
# cars = ['Supra', 'Matiz', 'Gentra']
# cars.insert(1, 'Nexia 5')
# print(cars)

# DEL - listdan index boyicha element ochirish:
# cars = ['Supra', 'Matiz', 'Gentra']
# del cars[0]
# print(cars)

# REMOVE - listdan value boyicha element ochirish: Birinchi elementni ochiradi agar elementlar kop bolsa
# cars = ['Supra', 'Matiz', 'Gentra']
# cars.remove('Supra')
# print(cars)

# POP - listdagi elementni sugurib olish
# Agar popda index berilmasa, oxirgi element sugurib olinadi
# cars = ['Supra', 'Matiz', 'Gentra']
# matiz = cars.pop(1)
# print(matiz)

# APPEND BILAN POPNING MIXED VERSIYASI:
# guests = ['Nakamura']
# cars = []
# cars.append(guests.pop(0))
# print(cars)

# AMALIYOT:
# names = ['Said', 'Asil', 'Nurik']
# print(f"Salom, {names[0]} choyxona boramizmi?")
# print(f"Salom, {names[1]} choyxona boramizmi?")
# print(f"Salom, {names[2]} choyxona boramizmi?")

# numbers = [20, 20.0, -20]
# numbers[0] = 10
# overall = numbers[0] + numbers[1] + numbers[2]
# print(overall)

# t_shaxslar = ['Alisher Navoiy', 'Mirzo Ulugbek']
# z_shaxslar = ['Elon Musk', 'Jahongir Ortiqxojayev', 'Farhod Kadirov']
# t_shaxs = t_shaxslar.pop(0)
# z_shaxs = z_shaxslar.pop(0)
# print(f"Men tarixiy shaxslardan {t_shaxs} bilan, zamonaviy shaxslardan esa {z_shaxs} bilan suhbat qilishni istardim")

# friends = []
# friends.append('Mirfayz')
# friends.append('Said')
# friends.remove('Said')
# friends.insert(0, 'Asil')
# friends.insert(2, 'Nurik')
# guests = []
# first_guest = friends.pop(0)
# guests.append(first_guest)
# print(guests)

# MAINPOINTS:
# list, append(), insert(), pop(), del, remove()
# Listdagi elementlarni ozgartirish

