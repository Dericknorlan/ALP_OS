import os
import shutil
import sys

def ls():
    """List files and directories in the current directory."""
    try:
        items = os.listdir()
        for item in items:
            print(item)
    except Exception as e:
        print(f"Error: {e}")

def pwd():
    """Print the current working directory."""
    try:
        print(os.getcwd())
    except Exception as e:
        print(f"Error: {e}")

def cd(path):
    """Change the current working directory."""
    try:
        os.chdir(path)
        print(f"Changed directory to {os.getcwd()}")
    except Exception as e:
        print(f"Error: {e}")

def mkdir(directory):
    """Create a new directory."""
    try:
        os.mkdir(directory)
        print(f"Directory '{directory}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def rmdir(directory):
    """Remove an empty directory."""
    try:
        os.rmdir(directory)
        print(f"Directory '{directory}' removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def touch(filename):
    """Create a new empty file."""
    try:
        with open(filename, 'w') as f:
            pass
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")

def rm(filename):
    """Remove a file."""
    try:
        os.remove(filename)
        print(f"File '{filename}' removed successfully.")
    except Exception as e:
        print(f"Error: {e}")

def cp(source, destination):
    """Copy a file."""
    try:
        shutil.copy(source, destination)
        print(f"File '{source}' copied to '{destination}'.")
    except Exception as e:
        print(f"Error: {e}")

def mv(source, destination):
    """Move or rename a file/directory."""
    try:
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}'.")
    except Exception as e:
        print(f"Error: {e}")

def help_command():
    """Display the list of available commands."""
    commands = {
        'ls': 'List files and directories in the current directory.',
        'pwd': 'Print the current working directory.',
        'cd': 'Change the current working directory.',
        'mkdir': 'Create a new directory.',
        'rmdir': 'Remove an empty directory.',
        'touch': 'Create a new empty file.',
        'rm': 'Remove a file.',
        'cp': 'Copy a file.',
        'mv': 'Move or rename a file/directory.',
        'help': 'Display the list of available commands.',
        'clear': 'Clear the terminal screen.',
        'exit': 'Exit the CLI.',
        'search': 'Search for files/directories matching a pattern.',
        'tree': 'Display the directory structure as a tree.',
        'log': 'Log a command to a log file.'
    }
    for cmd, desc in commands.items():
        print(f"{cmd}: {desc}")

def clear():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def search(pattern):
    """Search for files or directories matching a pattern."""
    try:
        for root, dirs, files in os.walk(os.getcwd()):
            for name in dirs + files:
                if pattern in name:
                    print(os.path.join(root, name))
    except Exception as e:
        print(f"Error: {e}")

def tree(path=".", level=0):
    """Display the directory structure as a tree."""
    try:
        for entry in os.listdir(path):
            print("  " * level + f"|- {entry}")
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                tree(full_path, level + 1)
    except Exception as e:
        print(f"Error: {e}")

def log(command):
    """Log a command to a log file."""
    try:
        with open("command_log.txt", "a") as log_file:
            log_file.write(command + "\n")
        print(f"Command '{command}' logged successfully.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        try:
            user_input = input("CLI > ").strip()
            log(user_input)  # Log the command

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0]
            args = parts[1:]

            if command == "ls":
                ls()
            elif command == "pwd":
                pwd()
            elif command == "cd":
                cd(args[0]) if args else print("Usage: cd <path>")
            elif command == "mkdir":
                mkdir(args[0]) if args else print("Usage: mkdir <directory>")
            elif command == "rmdir":
                rmdir(args[0]) if args else print("Usage: rmdir <directory>")
            elif command == "touch":
                touch(args[0]) if args else print("Usage: touch <filename>")
            elif command == "rm":
                rm(args[0]) if args else print("Usage: rm <filename>")
            elif command == "cp":
                cp(args[0], args[1]) if len(args) == 2 else print("Usage: cp <source> <destination>")
            elif command == "mv":
                mv(args[0], args[1]) if len(args) == 2 else print("Usage: mv <source> <destination>")
            elif command == "help":
                help_command()
            elif command == "clear":
                clear()
            elif command == "exit":
                print("Exiting CLI. Goodbye!")
                break
            elif command == "search":
                search(args[0]) if args else print("Usage: search <pattern>")
            elif command == "tree":
                tree(args[0]) if args else tree()
            elif command == "log":
                log(' '.join(args)) if args else print("Usage: log <command>")
            else:
                print(f"Unknown command: {command}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
