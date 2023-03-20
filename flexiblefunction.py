# *ARGS - istalgancha argument kiritsa boladi, bunda parametrlar TUPLEga joylanadi, doim oxirida yoziladi
# def calculate(*numbers):
#     print(sum(numbers))
# calculate(1,2,3,4,5)

# **KWARGS - keyword arguments, bunda key-valuedek yozish kk, bu ham args kabi istalgancha argument kiritaishda yordamchi
# Bunda yangi dictionary yaratilinib, oshani ichiga juftliklar qoshib boriladi
# def info(**information):
#     return information
# auto = info(color='qizil', model='BMW', price=10000)
# print(auto)

# AMALIYOT:
# def multiply(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
#
# print(multiply(4,5,6))

# def student_info(name, surname, **infos):
#     infos['name'] = name
#     infos['surname'] = surname
#     return infos
# first_student = student_info('Mirfayz', 'Irgashev', age=17, faculty='Computer Science')
# print(first_student)

# MAINPOINTS:
# *ARGS, **KWARGS
