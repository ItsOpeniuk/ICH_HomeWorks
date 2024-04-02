import sys
import subprocess

def run_python_file(file_path):
    try:
        subprocess.run(['python3', file_path], check=True)
        print(f"Файл {file_path} закрыт")
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
    except subprocess.CalledProcessError:
        print(f"Ошибка при запуске файла {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Не верное количество аргументов")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"Файл  {file_path} запущен!")
    run_python_file(file_path)
