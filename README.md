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

1. Clone the repository or copy the `ALP_OS.py` script to a local directory.
2. Open a terminal or command prompt and navigate to the directory containing the `ALP_CLI.py` file.
3. Execute the program with the command:

```bash
python ALP_CLI.py

## Example Usage

Below is an example interaction with the CLI application:

```bash
CLI > pwd
/home/user/my_projects

CLI > mkdir example_folder
Directory 'example_folder' successfully created.

CLI > cd example_folder
Switched to /home/user/my_projects/example_folder

CLI > touch file.txt
File 'file.txt' created.

CLI > ls
file.txt

CLI > search file
/home/user/my_projects/example_folder/file.txt

CLI > tree
|- file.txt

CLI > log "Created example_folder and file.txt"
Command logged: "Created example_folder and file.txt"

CLI > exit
Goodbye!

