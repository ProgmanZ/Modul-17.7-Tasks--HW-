# Задача 9. Список списков

# Решение 1.
# def extract(n):
#     for i in n:
#         if type(i) == list:
#             extract(i)
#         else:
#             temp_list.append(i)
#     return temp_list

# print(extract(nice_list))

# Решение 2.
# result = []
# for i in nice_list:
#     for j in i:
#         for n in j:
#             result.append(n)

# print(result)

# Решение 3.
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

result = [number for third in nice_list for second in third for number in second]

print(result)
