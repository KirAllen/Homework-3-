#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
lst = [1.19, 3.42, 6.57, 8.22, 4.67]

def part(lst):
    for i in range(len(lst)):
        while lst[i] > 1:
            lst[i] = round(lst[i] - 1, 2)

def difference(lst):
    min_part = min(lst)
    max_part = max(lst)
    result = max_part - min_part
    print(round(result,2))

part(lst)
difference(lst)