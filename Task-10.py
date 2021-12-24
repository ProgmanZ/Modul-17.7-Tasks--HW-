# Задача 10. Шифр Цезаря (сделайте по желанию)
#
# def cesar_code(let, i):
#     i = dictionary.index(let) - len(dictionary) + i
#     return dictionary[i]


dictionary = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuwvxyz'
user_letters = str(input('Введите сообщение: '))
user_letters.lower()
k = int(input('Введите сдвиг: '))

# result = [cesar_code(letter, k) if (letter != ' ') else ' ' for letter in user_letters]
result = [dictionary[dictionary.index(letter) - len(dictionary) + k] if (letter != ' ') else ' '
          for letter in user_letters]

print(''.join(result))
