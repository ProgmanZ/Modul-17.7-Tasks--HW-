# Задача 10. Шифр Цезаря (сделайте по желанию)

dictionary = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuwvxyz'
user_letters = str(input('Введите сообщение: '))
user_letters.lower()
k = int(input('Введите сдвиг: '))

result = [dictionary[dictionary.index(letter) - len(dictionary) + k] if (letter != ' ') else ' '
          for letter in user_letters]

print(''.join(result))
