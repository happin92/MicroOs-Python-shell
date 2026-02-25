import urllib.request
import json
import os
import zipfile
import shutil

# Обязательно RAW ссылка, иначе скачается HTML страница!
REPO_URL = "https://raw.githubusercontent.com/happin92/MicroOs-Packet-manager/main/apps.json"

def load_apps():
    try:
        with urllib.request.urlopen(REPO_URL) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        print(f"ошибка подключения: {e}")
        return {}

def install(args):
    if not args:
        print("укажите действие или название пакета")
        return

    # ВОТ ТУТ ЛОГИКА ФЛАГОВ, КАК В ТВОЕМ RM
    command = args[0]

    if command == "install":
        if len(args) < 2:
            print("укажите название пакета после install")
            return
        
        app_name = args[1]
        apps = load_apps()
        
        if app_name not in apps:
            print(f"пакета '{app_name}' нет в репозитории")
            return

        url = apps[app_name]
        zip_path = f"{app_name}.zip"

        try:
            print(f"скачиваю {app_name}...")
            urllib.request.urlretrieve(url, zip_path)

            if os.path.exists(app_name):
                print("удаляю старую версию...")
                shutil.rmtree(app_name)

            print("распаковка...")
            with zipfile.ZipFile(zip_path, 'r') as z:
                z.extractall(".")

            os.remove(zip_path)
            print(f"приложение '{app_name}' успешно установлено")
        except Exception as e:
            print(f"ошибка установки: {e}")

    elif command == "list":
        apps = load_apps()
        print("доступные пакеты:")
        for name in apps:
            print(f"- {name}")

    else:
        print(f"неизвестный флаг: {command}")
