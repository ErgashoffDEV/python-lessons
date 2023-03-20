# DATETIME kutubxonasi:
# datetime.now() - hozirgi vaqtni oladi
import datetime as dt
# now = dt.datetime.now()
# print(now)

# date() - faqat sanani ajratib oladi
# print(now.date())

# time() - faqat vaqtni ajratib oladi
# print(now.time())

# hour - faqat soatni ajratib oladi
# print(now.hour)

# minute - faqat daqiqani ajratib oladi
# print(now.minute)

# second - faqat sekundni ajratib oladi
# print(now.second)

# Bugungi sanani ajratib olish
# date = dt.date.today()
# print(date)

# Ozimizdan sana qoshish:
# tomorrow = dt.date(2023, 9, 10)
# print(tomorrow)

# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(f"Hozir soat: {vaqtHozir}")

# bugun = dt.date.today()
# ramazon = dt.date(2023, 3, 23)
# farq = ramazon-bugun
# print(f"Qurbon Hayitiga {farq.days} kun qoldi") #farq.days faqat kunni ajratib oladi

# strftime() - vaqtni ozmizni vaqtga aylantirish
# today = dt.datetime.today()
# time = today.strftime("%H:%M:%S")
# print(f"Hozir: {time}")

# KUN-OY-YIL
# today = dt.datetime.today()
# sana = today.strftime("%d-%m-%Y")
# print(f"Bugun sana: {sana}")

# KUN/OY/YIL
# today = dt.datetime.today()
# sana_vaqt = today.strftime("%d/%m/%Y, %H:%M")
# print(sana_vaqt)

# MATH: matematik funksiyalar
# PI qiymati
import math as m
# PI = m.pi
# print(PI)

# e natural logarifm asosi
# E = m.e
# print(E)

# MATH modulida sin, cos, tan, arccos hamma trigonometrik elementlar mavjud. Degrees and radians

# Logarifm
# print(m.log(10))

# Sonlarni yaxlitlash
# ceil() - sonlarni tepaga qarab yaxlitlaydi
# import math
# x = 4.6
# print(math.ceil(x))

# floor() - sonlarni pastga qarab yaxlitlaydi
# import math
# x = 4.6
# print(math.floor(x))

# PPRINT() - matnlarga chiroyli ishlov beradi
# from pprint import pprint
# pprint(smth)

# REGEX (Regular expressions) - Andoza bilan ishlash
# match funksiyasi element andozaga togri keladimi yoqmi shuni tekshiradi
# import re
# andoza = '^t...r$'
# first = 'temir'
# print(re.match(andoza, first))

# ihateregex.io - turli xil andozalar mavjud bolgan sayt

# findall - berilgan matnni ichidan andozani topadi
# import re
# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

# andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# email = re.findall(andoza,matn)
# print(email)

# Kuchli Parolni tekshirish + ihateregex
# import re
# andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
# msg = "Yangi parol kiriting (kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf,"
# msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '
#
# while True:
#     password = input(msg)
#     if re.match(andoza, password):
#         print("Maxfiy so'z qabul qilindi")
#         break
#     else:
#         print("Maxfiy so'z talabga javob bermadi")

# AMALIYOT:
# import datetime as dt
# date = dt.datetime.now()
# another_date = dt.date(2023, 4, 2)
# print(date)
# print(another_date)

# import datetime as dt
# date = dt.date.today()
# ramazon = dt.date(2023, 3, 23)
# qurbon = dt.date(2023, 8, 29)
# difference = ramazon - date
# difference_second = qurbon - date
# print(difference)
# print(difference_second)

# import datetime as dt
# date = dt.date.today()
# birth_date = dt.date(2022, 9, 10)
# difference = date - birth_date
# print(difference)

# import re
# andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# word = '919367788755'
# print(re.match(andoza, word))

# import re
# andoza = '^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
# msg = 'Telefon raqamizni kiriting: '
# while True:
#     question = input(msg)
#     if re.match(andoza, question):
#         print('Telefon raqam togri')
#         break
#     else:
#         print('Qaytadan telefon raqam kiriting')

# import re
# andoza = 'https://youtu.be/vsxJPRLXpgI'
# matn = 'Assalom alaykum hurmatli do\'stlar. Navbatdagi darsimiz YouTubega yuklandi: ' \
#        'https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida ' \
#        'klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o\'rganamiz'
# print(re.findall(andoza, matn))
