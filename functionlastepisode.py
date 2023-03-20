# LAMBDA: nomsiz funksiya yokida bir martalik funksiya
# Oddiy funksiya:
# def calculate(x,y):
#     return x ** y
# print(calculate(5,7))

# LAMBDAlik funksiya
# calculate = lambda x, y: x ** y
# print(calculate(5, 6))

# LAMBDA + FUNKSIYA
# def daraja(n):
#     return lambda x : x**n
#
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")

# MAP() - Argument sifatida funksiya va listni oladi
# numbers = list(range(11))
# def calculate(x):
#     return x * x
# print(list(map(calculate, numbers)))

# LAMBDA+MAP
# kvadratlar = list(map(lambda x:x*x, numbers))
# print(kvadratlar)

# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x,y:x+y,a,b))
# print(a_plus_b)

# FILTER() - Argument sifatida funksiya va royxat oladi. Bu yerda True va False ham rol oynaydi
# import random as r
#
# # sample - berilgan sonlar ichidan tasodifiy sonlar tanlaydi. range(100), 20 - 100ta son orasidan 20 ta tasodifiy son
# numbers = r.sample(range(100), 10)
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(numbers)
# print(even_numbers)

# startswith() - matn belgilangan harfdan boshlanadimi yoqmi tekshiruvchi metod
# mevalar = ['olma', 'anor', 'anjir', 'avokado']
# sorted_mevalar = list(filter(lambda text: text.startswith('a'), mevalar))
# print(sorted_mevalar)

# MAINPOINTS:
# lambda, filter, map, startswith, random.sample
