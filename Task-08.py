# Задача 8. Развлечение
import random

quantity_stick = int(input('Введите количество палок: '))
quantity_throws = int(input('Введите количество бросков: '))

all_stick = ['|' for _ in range(quantity_stick)]
all_stick_b = all_stick[:]

for i in range(quantity_throws):

    L_i = random.randint(0, quantity_stick)
    R_i = random.randint(0, L_i)

    all_stick_b = ['.' if L_i >= i >= R_i else '|'
                   for i in range(len(all_stick_b))]

    all_stick = ['.' if all_stick[i] == '.' or all_stick_b[i] == '.' else '|'
                 for i in range(len(all_stick_b))]

    print(f'Сбиты палки с номера {R_i + 1} по номер {L_i + 1}')
print('all_stick =', all_stick)

