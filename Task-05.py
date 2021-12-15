# Задача 5. Разворот

user_string = input('Введите строку: ')

left_new_user_string = user_string[:user_string.index('h') + 1]
center_user_string = user_string[user_string.index('h') + 1:]
right_user_string = center_user_string[center_user_string.index('h'):]
center_user_string = center_user_string[:center_user_string.index('h')]

result = left_new_user_string + center_user_string[::-1] + right_user_string

print(result)
