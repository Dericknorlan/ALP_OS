# Command Line Interface (CLI) Python Script

## Overview

This Python script implements a simple command-line interface (CLI) that provides various functionalities to interact with the file system. It allows users to perform common file and directory operations, such as creating, listing, removing files or directories, and more. The script also includes utility commands for searching, logging, and viewing the directory structure.

## Features

The script supports the following commands:

- **ls**: Lists all files and directories in the current working directory.
- **pwd**: Prints the current working directory path.
- **cd**: Changes the current working directory to the specified path.
- **mkdir**: Creates a new directory with the specified name.
- **rmdir**: Removes an empty directory.
- **touch**: Creates a new empty file with the specified name.
- **rm**: Deletes a file with the specified name.
- **cp**: Copies a file from the source to the destination path.
- **mv**: Moves or renames a file or directory.
- **help**: Displays a list of available commands and their descriptions.
- **clear**: Clears the terminal screen.
- **search**: Searches for files or directories matching a given pattern.
- **tree**: Displays the directory structure as a tree, starting from the specified or current directory.
- **log**: Logs a command to a log file (`command_log.txt`) for record-keeping.
- **exit**: Exits the CLI application.

## How to Run the Program

Ensure that Python 3 is installed on your system.

1. Clone the repository or copy the `OS.py` script to a local directory.
2. Open a terminal or command prompt and navigate to the directory containing the `OS.py` file.
3. Execute the program with the command:

```bash
python OS.py
```

## Command Usage

```bash
CLI >
# List files and directories
CLI > ls
# Displays all files and directories in the current working directory.

# Print the current directory
CLI > pwd
# Displays the absolute path of the current working directory.

# Change directory
CLI > cd /path/to/directory
# Changes the current working directory to the specified path.

# Create a directory
CLI > mkdir new_folder
# Creates a new directory named new_folder in the current directory.

# Remove an empty directory
CLI > rmdir empty_folder
# Deletes the directory named empty_folder if it is empty.

# Create a new file
CLI > touch new_file.txt
# Creates an empty file named new_file.txt in the current directory.

# Delete a file
CLI > rm unwanted_file.txt
# Deletes the file unwanted_file.txt from the current directory.

# Copy a file
CLI > cp source.txt destination.txt
# Copies the file source.txt to destination.txt. The destination can also be a directory.

# Move or rename a file or directory
CLI > mv old_name.txt new_name.txt
# Renames or moves old_name.txt to new_name.txt or another directory.

# Display help information
CLI > help
# Lists all available commands with descriptions.

# Clear the terminal
CLI > clear
# Clears the terminal screen. Useful for reducing clutter.

# Search for files or directories
CLI > search pattern
# Searches for files or directories whose names contain the specified pattern.

# Display the directory structure
CLI > tree
# Displays the directory structure of the current directory in a tree format.
CLI > tree /path/to/directory
# Optionally, specify a directory path.

# Log a command
CLI > log any_command_here
# Logs the specified command or text to command_log.txt for record-keeping.

# Exit the CLI
CLI > exit
# Ends the CLI session and exits the application.
