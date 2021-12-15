# Задача 2. Генерация

number = int(input('Введите длину списка: '))

user_list = [i % 5 if i % 2 == 1 else 1 for i in range(number)]

print('Результат:', user_list)
