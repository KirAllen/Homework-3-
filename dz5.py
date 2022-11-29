#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

num = int(input())
a, b = 1,1
fibonacci = []
for i in range(num):
    fibonacci.append(a)
    a, b = b, a + b

a, b = 0, 1
for i in range(num+1):
    fibonacci.insert(0, a)
    a,b = b, a - b
print(fibonacci)