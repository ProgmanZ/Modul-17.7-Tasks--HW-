# Задача 7. Двумерный список

'''

[   [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11],
    [4, 8, 12]]

    [[1], [2], [3], [4]]
    [[1, 5], [2, 6]]]
'''

list_n = [[i for i in range(1, 12)] for j in range(1, 12, 4)]

print(list_n)