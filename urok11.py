#  # Задача 1
def factorial(num0):
    if num0 == 1 or num0 == 0:
        return 1
    else:
        return num0 * factorial(num0 - 1)

def obrfactorial(num1):
    a = []
    for i in range(num1, 0, -1):
        a.append(factorial(i))
    return a

num = int(input())
fact = factorial(num)
print(obrfactorial(fact))

# Задача 2
import collections

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        }
    }
}

def get_suf(age):
    if age % 10 == 1 and age % 100 != 11:
        return "лет"
    elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
        return "года"
    else:
        return "лет"


def get_pet(ID):
    return pets.get(ID, False)

def pets_list():
    if not pets:
        print("База данных пуста.")
        return
    for ID, data in pets.items():
        for name, info in data.items():
            suf = get_suf(info["Возраст питомца"])
            print(f'ID {ID}: Это {info["Вид питомца"]} по кличке {name}. Возраст питомца: {info["Возраст питомца"]} {suf}. Имя владельца: {info["Имя владельца"]}')


def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1
    name = input("Введите имя питомца: ")
    pet_type = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца (только число): "))
    owner = input("Введите имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner,
        }
    }
    print(f'Питомец "{name}" успешно добавлен с ID {new_id}')


def read():
    ID = int(input("Введите ID запрашиваемого питомца: "))
    pet = get_pet(ID)
    if not pet:
        print("Данного животного нет в базе")
    else:
        for name, info in pet.items():
            suf = get_suf(info["Возраст питомца"])
            print(f'Это {info["Вид питомца"]} по кличке "{name}". Возраст питомца: {info["Возраст питомца"]} {suf}. Имя владельца: {info["Имя владельца"]}')


def update():
    ID = int(input("Введите ID запрашиваемого питомца: "))
    pet = get_pet(ID)
    if not pet:
        print("Данного животного нет в базе")
        return
    for name in pet:
        print(f"Обновляем данные питомца по кличке '{name}'")
        new_name = input("Введите новую кличку (оставьте пустым, если не меняете): ") or name
        new_pet_type = input("Введите новый вид (оставьте пустым, если не меняете): ") or pet[name]["Вид питомца"]
        new_age = input("Введите новый возраст (оставьте пустым, если не меняете): ")
        new_owner = input("Введите новое имя владельца (оставьте пустым, если не меняете): ") or pet[name][
            "Имя владельца"]

        new_age = int(new_age) if new_age else pet[name]["Возраст питомца"]
        pets[ID] = {
            new_name: {
                "Вид питомца": new_pet_type,
                "Возраст питомца": new_age,
                "Имя владельца": new_owner
            }
        }
        print(f"Информация о питомце с ID {ID} обновлена.")


def delete():
    ID = int(input("Введите ID запрашиваемого питомца: "))
    pet = get_pet(ID)
    if ID in pets:
        del pets[ID]
        print(f'Питомец с ID {ID} удален')
    else:
        print("Питомец не найден")


print("База данных ветклиники. Доступны команды : create, read, update, delete, list, stop")
while True:
    command = input("\nВведите команду: ").strip().lower()
    if command == "stop":
        print("Завершение работы")
        break
    elif command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    else:
        print("Такой команды нет, попробуйте снова")