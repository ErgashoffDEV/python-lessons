# TRY_EXCEPT:
# try - xato kuzatilishi mumkin bolgan kod
# except - xatolik bolganda bajaralishi kk bolgan amal
# age = input('Yoshizni kiriting: ')
# try:
#     age = int(age)
#     print(f"Siz {2023-age}-yilda tug'ilgansiz")
# except:
#     print('Siz butun son kiritmadingiz')

# TRY-EXCEPT- ELSE: upgraded version of try-except
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")

# Malum turdagi xatolarni exceptning yoniga qoshib ham ishlatishimiz mumkin:
# except ZeroDivisionError
# except FileNotFoundError
# except ValueError
# except IndexError
# except KeyError

# TRY-EXCEPT-EXCEPT - bir nechta xatolarni ushlash uchun
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError: # agar foydalanuvchi butun son kiritmasa
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
#     print("0 ga bo'lib bo'lmaydi")
# else:
# print(f"x={x}")

# PASS - xuddi continuega otib, skip qiladi. Xatolik mavjud bolsa, uni otkazib yuboradi
# age = input('Yoshizni kiriting: ')
# try:
#     age = int(age)
#     print(f"Siz {2023-age}-yilda tug'ilgansiz")
# except:
#     pass

# isdigit() - element raqamdan oboratmi yoqmi shuni tekshiradi

# while + if:
# while True:
#     yosh = input("Yoshingizni kiriting: ")
#     if yosh.isdigit():
#         yosh = int(yosh)
#         break
#
# print(f"Siz {2021-yosh} yilda tug'ilgansiz")


