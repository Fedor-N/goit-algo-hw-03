import argparse
from pathlib import Path
import shutil
import os  # Don't forget to import the os module


def parse_argv():
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    parser.add_argument("-s", "--source", type=Path,
                        required=True, help="Папка з файлами")
    parser.add_argument("-o", "--output", type=Path,
                        default=Path("output"), help="Папка для копіювання")
    return parser.parse_args()


def recursive_copy(source: Path, output: Path):
    for el in source.iterdir():
        try:
            if el.is_dir():
                recursive_copy(el, output)
            else:
                if el.exists() and el.is_file() and os.access(el, os.R_OK):
                    # Використовуємо розширення як папку
                    folder = output / el.suffix[1:]
                    folder.mkdir(exist_ok=True, parents=True)
                    shutil.copy(el, folder)
        except Exception as e:
            print(f"Помилка при копіюванні {el}: {e}")


def main():
    args = parse_argv()
    try:
        args.output.mkdir(exist_ok=True, parents=True)
        recursive_copy(args.source, args.output)
        print("Копіювання завершено")
    except Exception as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
