# WHILE BILAN ROYXATNI TOLDIRISH
# names = []
# n = 1
# while True:
#     quest = f"{n}-dositingizni ismi nima? "
#     name = input(quest)
#     names.append(name)
#     again = input('Yana ism qoshasizmi? ')
#     if again == 'ha':
#         n += 1
#     else:
#         break
# for n in names:
#     print(n.title())

# WHILE BILAN DICTIONARYNI TOLDIRISH
# names = {}
# while True:
#     name = input("Dostizni ismini kiriting: ")
#     age = input(f"{name.title()} yoshi nechida: ")
#     names[name] = int(age)
#     again = input('Yana malumot qoshasizmi? ')
#
#     if again == 'yoq':
#         break
#
# for ism, yosh in names.items():
#     print(f"{ism.title()}ning yoshi {yosh}da")

# ROYXATDAN DICTIONARYGA ELEMENT KOCHIRISH
# students = ['Ali', 'Vali']
# marked_students = {}
# while students:
#     student = students.pop()
#     mark = input(f"{student}ning bahosini kiriting: ")
#     marked_students[student] = int(mark)
# for key, value in marked_students.items():
#     print(f"{key}: {value}")

# AMALIYOT:
# orders = []
# n = 1
# while True:
#     value = input(f'{n}-zakazni kiriting: ')
#     orders.append(value)
#     again = input('Yana zakaz bormi? ')
#
#     if again == 'ha':
#         n += 1
#     else:
#         break
# for order in orders:
#     print(order.title())

# things = {}
# while True:
#     name = input('Mahsulot nomini kiriting: ')
#     price = input(f'{name.title()} narxini kiriting: ')
#     things[name] = int(price)
#     again = input('Yana mahsulot qoshasizmi? ')
#     if again == 'yoq':
#         break
# for key, value in things.items():
#     print(f'{key}: {value}')
