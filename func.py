import datetime, sys, os
import user_state

def quit():
    sys.exit()

def help():
    print(" 'help' = посмотреть актуальные команды")
    print(" 'echo' = выввести свой текст")
    print(" 'calc' = калькулятор")
    print(" 'whoami' = узнать имя профиля")
    print(" 'clear' = очистить терминал")
    print(" 'yes' = проспамить свой текст")
    print(" 'pfetch' = показать сведения о системе")
    print(" 'pwd' = просмотр текущей дериктории")
    print(" 'useradd' = создать нового пользователя")
    print(" 'quit' = выйти из ос")
    print(" ")
    print(" 'ls ' = просмотреть содержимое текущей дериктории")
    print(" 'mkdir' = создать папку со своим названием")
    print(" 'rm' = удалить файл")
    print(" 'rm -rf' = удалить директорию")
    print(" 'run' = запустить файл (пока поддерживаються только .py")

def echo(args):
    result = " ".join(args)
    print(result)

def calculator():
    try:
        expr = input("введи выражение: ")
        if not expr.strip():
            print("вы ничего не ввели, введите еще раз")
            return
        print(eval(expr))
    except ZeroDivisionError:
        print("на 0 делить нельзя")
    except Exception:
        print("неизвестные числа/операторы вычисления")

def whoami():
    print(user_state.current_user)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def yes(args):
    text = " ".join(args)
    for i in range(50):
        print(text)

def pwd():
    print(os.getcwd())

def useradd(args):
    if not args:
        print("укажите новое имя пользователя")
        return False
        
    new_user = args[0]
    
    if new_user in user_state.users:
        print("пользователь уже существует")
        return False
        
    user_state.users.append(new_user)
    user_state.current_user = new_user
    print(f"создан новый пользователь {new_user}")
    return True
        
def error(e):
    print(f"извините, произошла непредвиденная ошибка {e} ")
