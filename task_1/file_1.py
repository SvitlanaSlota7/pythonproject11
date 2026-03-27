file_name = "myfile.txt"

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        print("Вміст файлу:")
        print(content)
except FileNotFoundError:
    print(f"Помилка: Файл '{file_name}' не знайдено.")