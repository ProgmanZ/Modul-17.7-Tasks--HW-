# Задача 1. Гласные буквы


user_text = input('Введите текст: ')

letter_list = 'аеёиоуыя'
used_letters = [letter for letter in user_text if letter in letter_list]

print('\nСписок гласных букв:', used_letters)
print('Длина списка:', len(used_letters))
