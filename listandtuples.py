# SORT() - listdagi elementlarni sortirovka qiladi
# Sort metodini ishlatishda harflarni bir xil korinishga olib kelish kk
# cars = ['Supra', 'Lacetti', 'Gentra']
# cars.sort()
# cars.sort(reverse=True) - sort metodining qarama-qarshi varianti
# print(cars)

# SORTED() - listdagi elementlarni ozgartirmagan holda sortirovka qilish
# cars = ['Supra', 'Lacetti', 'Gentra']
# print(sorted(cars, reverse=True)) - sortedga reverse metodini qoshish
# print(sorted(cars))

# REVERSE() - listni oxiridan boshiga qarab sort qilish
# cars = ['Supra', 'Lacetti', 'Gentra']
# cars.reverse()
# print(cars)

# LEN() - listning uzunligini aniqlash
# cars = ['Supra', 'Lacetti', 'Gentra']
# print(len(cars))

# RANGE() - sonlar ketma-ketligini yaratish
# Range har doim ikkinchi indeksdan bitta avval toxtaydi
# numbers = list(range(0, 11))
# print(numbers)

# RANGE VA QADAM
# numbers = list(range(0, 11, 2)) 0dan 11 gacha 2 qadam bilan sonlar royxati
# numbers = list(range(0, 101, 10)) 0dan 101 gacha 10 qadam bilan sonlar royxati
# print(numbers)

# MIN() - listdagi minimum qiymatga ega bolgan elementni korsatadi
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# print(min(narhlar))

# MAX() - listdagi maksimum qiymatga ega bolgan elementni korsatadi
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# print(max(narhlar))

# SUM() - listdagi elementlarning barchasini yigindisini korsatadi
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# print(sum(narhlar))

# LISTNI KESISH
# cars = ['Supra', 'Lacetti', 'Gentra']
# print(cars[0:3]) 0, 1, 2 elementlarini oldi
# print(cars[:3]) 0dan boshlab 3-elementgacha
# print(cars[2:]) 2 dan boshlab oxirigacha bolgan elementlarni oladi

# LISTDAN NUSXA OLISH
# cars = ['Supra', 'Lacetti', 'Gentra']
# my_cars = cars   BU NUSXA OLISHMAS, BUNDA BITTA LISTGA IKKITA NOM BERYAPMIZ
# my_cars = cars[:]  NUSXA OLISH
# print(my_cars)

# TUPLES - OZGARTIRIB BOLMAYDIGAN LIST

# CREATION OF TUPLES
# toys = (1, 2, 3, 4)

# TUPLENI LISTGA OZGARTIRISH
# toys = (1, 2, 3, 4)
# toys = list(toys)
# print(toys)

# LISTNI TUPLEGA OZGARTIRISH
# toys = [1, 2, 3, 4]
# toys = tuple(toys)
# print(toys)

# AMALIYOT:
# countries = ['Zimbabwe', 'Italy', 'England', 'Russia']
# print(len(countries))
# print(sorted(countries, reverse=True))
# countries.reverse()
# countries.sort(reverse=True)
# print(countries)

# numbers = list(range(120, 1201, 2))
# print(sum(numbers))
# print(len(numbers))
# print(max(numbers) - min(numbers))
# print(numbers[:20])
# print(numbers[-20:])
# print(numbers)

# taomlar = ['osh']
# nonushta = taomlar[:]
# nonushta.append('tuxum')
# nonushta.append('sariyog')
# print(taomlar)
# print(nonushta)
# nonushta = tuple(nonushta)


# MAINPOINTS:
# sort(), sorted(), reverse(), len()
# range(), min(), max(), sum()
# copy from the list
# tuple()