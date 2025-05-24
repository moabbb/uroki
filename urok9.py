# Задача 1
n = int(input())
razn = set()
for i in range(n):
    N = int(input())
    if N in razn:
        print("Одинаковое")
    else:
        razn.add(N)
print(len(razn))

# Задача 2
n1 = int(input("Введите количество чисел в первом списке: "))
ns1 = set()
for i in range(n1):
    N1 = int(input("Введите число: "))
    ns1.add(N1)

n2 = int(input("Введите количество чисел во втором списке: "))
ns2 = set()
for i in range(n2):
    N2 = int(input("Введите число: "))
    ns2.add(N2)

b = ns1.intersection(ns2)
print("Общее количество чисел в обоих списках:", len(b))

# Задача 3
a = list(map(int, input().split()))
sp = set()
for i in a:
    if i in sp:
        print("Yes")
    else:
        print("No")
        sp.add(i)