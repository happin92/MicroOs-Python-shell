import os
import shutil

root_dir = os.path.abspath(".")
home_dir = os.path.join(root_dir, "home")

if not os.path.exists(home_dir):
    os.makedirs(home_dir)

def list_files():
    files = os.listdir(".")
    for f in files:
        prefix = "[DIR]" if os.path.isdir(f) else "[FILE]"
        print(f"{prefix} {f}")

def make_dir(args):
    if not args:
        print("вы не ввели название папки")
        return
    name = args[0]
    try:
        os.makedirs(name)
        print(f"папка {name} создана")
    except FileExistsError:
        print("папка с таким названием уже есть")

def remove_file(args):
    if not args:
        print("вы не ввели название папки или файла")
        return

    if args[0] == "-rf":
        if len(args) < 2:
            print("укажите название папки чтобы полностью очистить ее")
            return

        folder_name = args[1]
        if os.path.exists(folder_name) and os.path.isdir(folder_name):
            shutil.rmtree(folder_name)
            print(f"вы полностью удалили папку '{folder_name}' ")
        else:
            print(f" '{folder_name}' не папка")
    else:
        name = args[0]
        if os.path.exists(name) and os.path.isfile(name):
            os.remove(name)
            print(f"файл '{name}' удален")
        else:
            print("файл не найден или это папка")

def change_dir(args):
    if not args:
        os.chdir(home_dir)
        print(f"вы в домашней директории {os.getcwd()}")
        return

    path = args[0]
    old_path = os.getcwd()

    try:
        os.chdir(path)
        new_path = os.path.abspath(os.getcwd())

        if not new_path.startswith(home_dir):
            os.chdir(old_path)
        else:
            print(f"вы в {os.getcwd()}")

    except FileNotFoundError:
        print(f"папка '{path}' не найдена")
    except NotADirectoryError:
        print(f" {path}' это файл, а не папка")


def run_python(args):
    if not args:
        print("ошибка: укажите файл (например: run game.py)")
        return

    filename = args[0]

    if not os.path.exists(filename):
        print(f"ошибка: файл '{filename}' не найден")
        return

    if not filename.endswith(".py"):
        print(f"ошибка: {filename} не является файлом python")
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()

        print(f"запуск {filename}...")
        print("-" * 20)
        print(" ")
        try:
            exec(code, {"__name__": "__main__"})
        except SystemExit:
            print("завершено")

        print("-" * 20)
        print("завершено")
        print(" ")
    except Exception as e:
        print(f"ошибка при выполнении {filename}: {e}")
