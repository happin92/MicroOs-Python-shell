import urllib.request
import json
import os
import zipfile

REPO_URL = "https://raw.githubusercontent.com/happin92/MicroOs-Packet-manager/main/apps.json"

def load_apps():
    with urllib.request.urlopen(REPO_URL) as r:
        return json.loads(r.read().decode())

def install(app_name):
    apps = load_apps()

    if app_name not in apps:
        print("такого приложения нет в репозитории")
        return

    url = apps[app_name]

    zip_path = f"{app_name}.zip"

    print("скачиваю пакет...")
    urllib.request.urlretrieve(url, zip_path)

    if os.path.exists(app_name):
        print("удаляю старую версию...")
        import shutil
        shutil.rmtree(app_name)

    print("распаковка...")
    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(".")

    os.remove(zip_path)

    print(f"приложение '{app_name}' установлено")
    