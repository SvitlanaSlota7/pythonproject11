import json
import sys
import os


def load_data(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Error: The file '{filename}' was not found.")

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def print_contacts(contacts):
    if not contacts:
        print("\nНічого не знайдено.")
        return
    print("\nРезультати пошуку:")
    for c in contacts:
        print(f"Ім'я: {c['first_name']} {c['last_name']}, Тел: {c['phone']}, Місто: {c['city']}, Область: {c['state']}")


def main():
    if len(sys.argv) < 2:
        print("Помилка: вказати ім'я файлу як перший аргумент.")
        print("Приклад: python phonebook.py my_contacts.json")
        return

    filename = sys.argv[1]

    try:
        phonebook = load_data(filename)
    except FileNotFoundError as e:
        print(e)
        return
    except json.JSONDecodeError:
        print("Помилка: файл має некоректний формат JSON.")
        return

    while True:
        print("\n--- Phonebook Menu ---")
        print("1. Додати новий запис")
        print("2. Пошук за ім'ям")
        print("3. Пошук за прізвищем")
        print("4. Пошук за повним ім'ям")
        print("5. Пошук за номером телефону")
        print("6. Пошук за містом або областю")
        print("7. Видалити запис за номером")
        print("8. Оновити запис за номером")
        print("9. Вийти та зберегти")

        choice = input("\nОберіть дію (1-9): ")

        if choice == '1':
            entry = {
                "first_name": input("Ім'я: "),
                "last_name": input("Прізвище: "),
                "phone": input("Телефон: "),
                "city": input("Місто: "),
                "state": input("Область: ")
            }
            phonebook.append(entry)
            print("Запис додано!")

        elif choice == '2':
            val = input("Введіть ім'я: ")
            res = [c for c in phonebook if c['first_name'].lower() == val.lower()]
            print_contacts(res)

        elif choice == '3':
            val = input("Введіть прізвище: ")
            res = [c for c in phonebook if c['last_name'].lower() == val.lower()]
            print_contacts(res)

        elif choice == '4':
            val = input("Введіть повне ім'я (Ім'я Прізвище): ")
            res = [c for c in phonebook if f"{c['first_name']} {c['last_name']}".lower() == val.lower()]
            print_contacts(res)

        elif choice == '5':
            val = input("Введіть номер телефону: ")
            res = [c for c in phonebook if c['phone'] == val]
            print_contacts(res)

        elif choice == '6':
            val = input("Введіть місто або область: ")
            res = [c for c in phonebook if val.lower() in [c['city'].lower(), c['state'].lower()]]
            print_contacts(res)

        elif choice == '7':
            phone = input("Введіть телефон для видалення: ")
            original_len = len(phonebook)
            phonebook = [c for c in phonebook if c['phone'] != phone]
            if len(phonebook) < original_len:
                print("Запис видалено.")
            else:
                print("Запис не знайдено.")

        elif choice == '8':
            phone = input("Введіть телефон запису, який треба змінити: ")
            found = False
            for c in phonebook:
                if c['phone'] == phone:
                    print("Введіть нові дані (залиште порожнім, щоб не змінювати):")
                    c['first_name'] = input(f"Ім'я [{c['first_name']}]: ") or c['first_name']
                    c['last_name'] = input(f"Прізвище [{c['last_name']}]: ") or c['last_name']
                    c['city'] = input(f"Місто [{c['city']}]: ") or c['city']
                    c['state'] = input(f"Область [{c['state']}]: ") or c['state']
                    found = True
                    print("Дані оновлено.")
                    break
            if not found:
                print("Запис із таким номером не знайдено.")

        elif choice == '9':
            save_data(filename, phonebook)
            print(f"Дані збережено у {filename}. До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()