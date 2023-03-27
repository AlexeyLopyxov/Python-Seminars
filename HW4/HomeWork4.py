# Задача 22
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# import random
# count_1 = int(input('Введите количество элементов 1-го множества: '))
# array_1 = []
# for i in range(count_1):
#     array_1.append(random.randint(-10, 10))

# count_2 = int(input('Введите количество элементов 2-го множества: '))
# array_2 = []
# for i in range(count_1):
#     array_2.append(random.randint(-10, 10))

# print(array_1)
# print(array_2)

# nums_1 = set(array_1)
# nums_2 = set(array_2)

# i = nums_1.intersection(nums_2)
# print(i)

# nums_array = list(i)
# nums_array.sort()
# print(nums_array)



# Задача 24
# В фермерском хозяйстве в Карелии выращивают чернику.

# n = int(input())
# arr = list()

# for i in range(n):
#     x = int(input())
#     arr.append(x)

# arr_count = list()
# for i in range(len(arr) - 1):
#     arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
# arr_count.append(arr[-2] + arr[-1] + arr[0])
# print(max(arr_count))