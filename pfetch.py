import platform
import user_state

def fetch(): 
    os_name = "Micro-Os 1.1"
    host = "micro-os"
    py_ver = platform.python_version()

    print(f"""
                   .--.              user: {user_state.current_user}
                  |o_o |             os: {os_name}
                  |:_/ |             host: {host}
                 //   \ \            python: {py_ver}
                (|     | )           shell: bash
               /'\_   _/`\           terminal: konsole
               \___)=(___/           kernel: linux
         """)