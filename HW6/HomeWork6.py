# Задача 1
# Заполнить массив элементами арифм прогрессии

# a1 = int(input('Введите первый элемент прогрессии: '))
# d = int(input('Введите разность прогрессии: '))
# n = int(input('Введите количество элементов прогрессии: '))

# def list_new(a1, d, n):
#     list_new = []
#     for i in range(n):
#         an = a1 + i * d
#         list_new.append(an)
#     return list_new

# print(list_new(a1, d, n))




# Задача 2
# определить индексы массива, значения которых принадлежат заданному диапазону

# n = int(input('Введите количество элементов массива: '))

# def add_array(n):
#     new_array = []
#     for i in range(n):
#         new_array.append(int(input(f'Введите элементы {i+1} массива: ')))
#     return new_array

# array_1 = add_array(n)

# a1 = int(input('Введите нижнюю границу диапазона: '))
# a2 = int(input('Введите верхнюю границу диапазона: '))

# for i in range(len(array_1)):
#     if a1 <= array_1[i] <= a2:
#         print(i)