# Задача 3. Случайные соревнования

import random


def result_generator(number):
    result_list = [round(random.uniform(5.0, 10.0), 2) for _ in range(number)]
    return result_list


participants = 20
team_1 = result_generator(participants)
team_2 = result_generator(participants)
record_list = [team_1[i] if team_1[i] > team_2[i] else team_2[i] for i in range(participants)]

print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', record_list)
