import func
import fs
import pfetch

def run_command(command, args):
    if command == "quit":
        func.quit()
    elif command == "clear":
        func.clear()
    elif command == "help":
        func.help()
    elif command == "whoami":
        func.whoami()
    elif command == "yes":
        func.yes(args)
    elif command == "echo":
        func.echo(args)
    elif command == "calc":
        func.calculator()
    elif command == "ls":
        fs.list_files()
    elif command == "rm":
        fs.remove_file(args)
    elif command == "cd":
        fs.change_dir(args)
    elif command == "mkdir":
        fs.make_dir(args)
    elif command == "pfetch":
        pfetch.fetch()
    elif command == "pwd":
        func.pwd()
    elif command == "useradd":
        func.useradd(args)
    elif command == "run":
        fs.run_python(args)
    else:
        print(f"неизвестная команда {command}")
