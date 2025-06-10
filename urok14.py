def rec(my_list, a=0):
    if a >= len(my_list):
        print("Конец списка")
        return
    print(my_list[a])
    rec(my_list, a + 1)

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
rec(my_list)
