# Задача 34
# Про Винни- Пуха

# song = "пара-ра-рам рам-пам-папам па-ра-па-да"
# song_new = song.split()
 
# print(song_new)
 
# list_1 = [(sum(x in 'аеёиоуыэюя' for x in word)) for word in song_new]
 
# if len(set(list_1)) == 1 :
#     res = "Парам пам-пам"  
# else: res = "Пам парам"
 
# print(res)






# Задача 36
# Нумерация строк и столбцов

# rows = int(input('Количество строк: '))
# coloms = int(input('Количество столбцов: '))

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for x in range(1, num_rows + 1):
#         for y in range(1, num_columns + 1):
#             print(operation(x, y), end= '\t')
#         print()

# print_operation_table(lambda x, y: x * y, rows, coloms)