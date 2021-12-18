# Задача 6. Сжатие списка

n_element = int(input("Введите количество элементов списка: "))
n_list = [int(input(f'Введите {i + 1} элемент списка: ')) for i in range(n_element)]

print('Текущий список: ', n_list)

len_n_list = len(n_list)

n_list = [i for i in n_list if i != 0]

list_zero = [0 for i in range(len_n_list - len(n_list))]

print('Список с нулевыми значениями в конце:', n_list + list_zero)
print('Список без нулевых значений:', n_list)
