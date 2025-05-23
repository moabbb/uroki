# Задача 1
a = int(input())
num = []

for i in range(a):
    x = int(input())
    num.append(x)
num.reverse()
for j in num:
    print(j, end=" ")

# Задача 2
a = int(input())
b = list(map(int, input().split()))

b = [b[-1]] + b[:-1]
print(*b)

# Задача 3
n = int(input("Количесвто рыбаков: "))
m_max = int(input("Максимальная грузоподъемность лодки: "))

weights = []
for i in range(n):
    weight = int(input("Вес рыбака: "))
    weights.append(weight)
weights.sort()

i = 0
j = n - 1
cnt_boat = 0

while i <=j:
    if weights[i] + weights[j] <= m_max:
        i += 1
    j -= 1
    cnt_boat += 1
print(cnt_boat)



