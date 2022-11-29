# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
num = int(input())
lst = []
while num > 0:
    tmp = num % 2
    lst.append(tmp)
    num = num // 2

for i in range(len(lst)-1, -1, -1):
    print(lst[i], end="")