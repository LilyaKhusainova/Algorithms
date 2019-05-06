# -*- coding: utf-8 -*-
# Хусаинова Л. Р., 05-703, Нахождение наибольшей возрастающей
# последовательности (путём восстановления её по двум массивам)

a = []  # создание пустого массива
f = open('Sequence.txt') # открытие файла, в котором находятся числа
for line in f:
    a += map(int, (line.split()))# применение к каждой подстроке строки line
    # функции int()
f.close()
print('Массив исходных значений: ', a)
n = len(a)
d=[1]*n # создание массива из единиц размера n (массив количеств "скачков"
# для каждого значения из массива a)

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j]+1:
            d[i] = d[j]+1 # если значение, стоящее до i-ого, меньше, а количество
# "скачков" i-ого значения меньше необходимого, приравниваем их
print('Массив количеств "скачков": ', d)
maxInd = 0
# вычисление индекса максимального числа в массиве d
for i in range(n):
    if d[maxInd] < d[i]:  maxInd = i

k = maxInd
b = [a[k]]# b-массив значений одной из наибольших возрастающих
# последовательностей
# восстановление наибольшей возрастающеё последовательности
for j in range(maxInd-1, -1, -1):
    if a[j] < a[k] and d[j] == d[k]-1:
        k = j
        b.append(a[k])
print('Наибольшая возрастающая последовательность: ', b[::-1]) # вывод массива
# b в обратном порядке