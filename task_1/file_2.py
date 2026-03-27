from pathlib import Path

p = Path('.')

print("Список файлів:")

for file in p.iterdir():
    if file.is_file():
        print(f"Файл: {file.name}")