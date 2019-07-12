# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих.
# Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
#1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578
n = 50
l=[]
a = 0
b = 1
for i in range(2, n + 1):
    c = a + b
    a, b = b, c # присваиваем значение следующей паре
    if c < 4000000:
        if c%2==0:
            l.append(c)
    else:
        break
print(sum(l))