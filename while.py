# CREATION OF WHILE:
# number = 1
# while number < 5:
#     print(number)
#     number += 1

# while va input()
# quest = 'Lyuboy sonni kiriting (dasturni stop qilish uchun EXIT deb yozing): '
# value = ''
# while value != 'exit':
#     value = input(quest)
#     if value != 'exit':
#         print(int(value) ** 2)

# ISHORA(FLAG):
# quest = 'Lyuboy sonni kiriting (dasturni stop qilish uchun EXIT deb yozing): '
# ishora = True
# while ishora:
#     value = input(quest)
#     if value != 'exit':
#         print(int(value) ** 2)
#     else:
#         ishora = False

# BREAK operatori: while siklini  toxtatuvchi operator
# quest = 'Lyuboy sonni kiriting (dasturni stop qilish uchun EXIT deb yozing): '
# while True:
#     value = input(quest)
#     if value != 'exit':
#         print(int(value) ** 2)
#     else:
#         break

# BREAK for sikli uchun ham ishlatilinadi:
# sonlar = list(range(1,10))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# CONTINUE operatori: SKIP vazifasini bajaradi
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# AMALIYOT:
# quest = 'Sevimli kitobingizni kiritin(dasturni toxtaish uchun EXIT deng): '
# while True:
#     value = input(quest)
#     if value == 'exit':
#         break
# print('Dastur tugadi')

# quest = 'Chipta sotvolasizmi?(dasturni toxtatish uchun EXIT deb yozing): '
# while True:
#     value = input(quest)
#     if value == 'exit':
#         break
#     elif int(value) < 7:
#         print('Chipta narxi 1000')
#     elif int(value) < 18:
#         print('Chipta narxi 3000')
#     elif int(value) < 65:
#         print('Chipta narxi 5000')
#     else:
#         print('Chipta bepul')
# print('Dastur tugadi')

# MAINPOINTS:
# While, while and combination of input, ishora(flag), break, continue

