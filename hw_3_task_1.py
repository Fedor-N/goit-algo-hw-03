import os
import shutil
import argparse


def copy_and_sort(src_dir, dest_dir):
    # Перевірка існування та створення теки призначення
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            src_path = os.path.join(root, file)

            try:
                # Отримання розширення файлу
                _, extension = os.path.splitext(file)
                # Видалення крапки з початку розширення
                extension = extension[1:]

                # Створення піддиректорії на основі розширення файлу
                dest_subdir = os.path.join(dest_dir, extension)
                if not os.path.exists(dest_subdir):
                    os.makedirs(dest_subdir)

                # Формування шляху для копіювання файлу
                dest_path = os.path.join(dest_subdir, file)

                # Копіювання файлу
                shutil.copy2(src_path, dest_path)

                print(f"Копіювання {file} до {dest_path}")
            except Exception as e:
                print(f"Помилка при обробці файлу {file}: {str(e)}")


def main():
    # Парсинг аргументів командного рядка
    parser = argparse.ArgumentParser(
        description="Рекурсивне копіювання та сортування файлів.")
    parser.add_argument("source_dir", help="Шлях до вихідної директорії")
    parser.add_argument("destination_dir", nargs="?", default="dist",
                        help="Шлях до директорії призначення (за замовчуванням: dist)")
    args = parser.parse_args()

    # Виклик функції копіювання та сортування
    copy_and_sort(args.source_dir, args.destination_dir)


if __name__ == "__main__":
    main()
