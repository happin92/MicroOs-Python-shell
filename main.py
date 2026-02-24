import os, time, func, executor, user_state

def main():
    home = os.path.abspath("home")

    if not os.path.exists(home):
        os.makedirs(home)

    os.chdir(home)
    
    print("Micro Os loading...")
    time.sleep(1)

    func.clear()

    print("you r in os, get ready")
    print(" ")
    time.sleep(1.5)

    while True:
        current_path = os.getcwd()
        try:
            current_path = os.path.abspath(os.getcwd())

            if not current_path.startswith(home):
                os.chdir(home)

            user_input = input(f"{user_state.current_user}@micro-os {os.path.basename(current_path)} $: ")
            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()
            args = parts[1:]

            executor.run_command(command, args)

        except KeyboardInterrupt:
            print("чтобы выйти введите 'quit' ")

        except Exception as e:
            func.error(e)

if __name__ == "__main__":
    main()