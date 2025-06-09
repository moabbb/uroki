import random
def pl(x):
    for i in x:
        print(*i)

a = int(input("Введите первый размер матрицы: "))
b = int(input("Введите второй размер матрицы: "))

matrix_1 = [[random.randint(-100, 100) for i in range(a)] for i in range(b)]
matrix_2 = [[random.randint(-100, 100) for i in range(a)] for i in range(b)]
matrix_3 = [[0 for i in range(a)] for i in range(b)]

for i in range(b):
    for j in range(a):
        matrix_3[i][j] = matrix_1[i][j] + matrix_2[i][j]


print("Матрица 1: ")
pl(matrix_1)
print("Матрица 2: ")
pl(matrix_2)
print("Матрица 3: ")
pl(matrix_3)