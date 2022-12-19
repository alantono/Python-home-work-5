# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Решение без filter

# f = open('Task1.txt', 'r', encoding="utf-8")
# data = f.read() + ' '
# f.close()
# print(data)
# data1 = data.split()
# for i in data1:
#     if "абв" in i:
#         print(str(i))
#         data1.remove(str(i))
# print(' '.join(data1))

# Решение c filter
f = open('Task1.txt', 'r', encoding="utf-8")
data = f.read() + ' '
f.close()
print(data)
data1 = data.split()
data1 = list(filter(lambda i: "абв" not in i, data.split()))
print(' '.join(data1))
