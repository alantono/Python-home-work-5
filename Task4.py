# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data = list(
    map(str, input('Введите последовательность символов через пробел:').split()))
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
m = 1
n = len(data)

for i in range(0, len(data) - 1):
    if data[i] == data[i + 1]:
        m = m + 1
    else:
        list1.append(m)
        m = 1
        list1.append(data[i])
list1.append(m)
list1.append(data[n - 1])

a = ''.join(map(str, list1))
print(a)
f = open('RLE.txt', 'w')
f.write(a)
f.close()

f = open('RLE.txt', 'r')
data1 = f.read()
f.close()

list2 = list(data1)

for i in range(0, len(list2), 2):
    list3.append(list2[i])
    list4.append(list2[i + 1])

for i in range(len(list3)):
    list5.append(int(list3[i]) * list4[i])

a = ''.join(map(str, list5))
print(a)
f = open('RLE.txt', 'a')
f.write(a)
f.close()
