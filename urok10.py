# Задача 1
pets = {}

pet_name = input("Введите имя питомца: ")
pet_type = input("Введите вид питомца: ")
pet_age = int(input("Введите возраст питомца (только число): "))
owner_name = input("Введите имя владельца: ")

pets[pet_name] = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

age = pets[pet_name]["Возраст питомца"]
if 11 <= age % 100 <= 14:
    year_word = "лет"
elif age % 10 == 1:
    year_word = "год"
elif 2 <= age % 10 <= 4:
    year_word = "года"
else:
    year_word = "лет"

print("Это", pets[pet_name]["Вид питомца"], 'по кличке "' + pet_name + '".',
      "Возраст питомца:", str(age), year_word + ".", "Имя владельца:", pets[pet_name]["Имя владельца"])


# Задача 2
# # Если вводим любые числа
my_dict = dict()
n = int(input())

for i in range(n):
    k = int(input())
    my_dict[k] = k ** k

print(my_dict)

# # Если делаем как по задачи от 10 до -5 включительно
my_dict = {}

for i in range(10, -6, -1):
    my_dict[i] = i ** i

print(my_dict)
