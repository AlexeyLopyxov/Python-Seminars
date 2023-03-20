# # Задача 10
# # Задача про монетки

# import random
# count_mon = int(input('Введите количество монеток: '))
# array = []
# for i in range(count_mon):
#     array.append(random.randint(0, 1))
# print(array)

# reshka = 0
# orel = 1

# count_reshka = 0
# count_orel = 0
# for i in range(count_mon):
#     if(reshka == array[i]):
#         count_reshka += 1
#     elif(orel == array[i]):
#         count_orel += 1
# print(f'Количество решек: {count_reshka}')
# print(f'Количество орлов: {count_orel}')

# if(count_reshka <= count_orel):
#     print(f'Нужно перевернуть {count_reshka} монет')
# else:
#     print(f'Нужно перевернуть {count_orel} монет')





# # Задача 12 
# # Задача про сумму и произведение чисел
# import math

# sum = int(input('Введите сумму чисел: '))
# prod = int(input('Введите произведение чисел: '))

# y1 = (sum + math.sqrt(sum ** 2 - 4 * prod))/2
# y2 = (sum - math.sqrt(sum ** 2 - 4 * prod))/2
# x1 = sum - y1
# x2 = sum - y2

# print(f'Первое число равно {int(x1)}, второе число равно {int(y1)}')
# print(f'Первое число равно {int(x2)}, второе число равно {int(y2)}')





# # Задача 14
# # Задача про степени двойки до числа N

# number = int(input('Введите число: '))

# for i in range(number):
#     step = 2 ** i
#     if(step <= number):
#         print(step, end = ' ')