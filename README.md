# AirBnB clone - The console

![](https://i.ibb.co/vc5S8my/65f4a1dd9c51265f49d0.png)


## Description
This project is a command interpreter that allows users to interact with the application through a command-line interface. It provides a set of commands that can be used to perform various actions.

## Command Interpreter
The command interpreter is a Python program that reads user input from the command line, interprets the input, and executes the corresponding commands. It provides a user-friendly interface for interacting with the application.

## Requirements
python3 (version 3.8.5) has to be installed if you desire to use the console:
```bash
sudo apt-get install python3
```

## Installation
To install the shell, follow these steps:
1. Clone the project repository:
```bash
git clone https://github.com/Ghelder/holbertonschool-AirBnB_clone.git
```

2. Navigate to the project directory:
```bash
cd holbertonschool-AirBnB_clone
```

3. Run the command interpreter:
```bash
python3 console.py
```

or
```bash
./console.py
```

## How to Use the Command Interpreter

You can use the following commands:

- Your shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

- This console also works in non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

- All tests should also pass in non-interactive mode
```bash
echo "python3 -m unittest discover tests" | bash
```
or
```bash
python3 -m unittest discover tests
```
## Usage
To execute a command, type the command followed by any required arguments or options. Press Enter to submit the command. The command interpreter will then execute the command and display the result.

## Examples
Examples of how to use the command interpreter:
- This command is to create a new BaseModel, and return an "id": create <class_name>
```bash
(hbnb) create BaseModel
b2f3db9e-8df6-427b-9241-441baa5042d8
(hbnb)
```
- This command follow by the id of the BaseModel, display only the content of that BaseModel: show <class_name> <_id>
```bash
(hbnb) show BaseModel b2f3db9e-8df6-427b-9241-441baa5042d8
[BaseModel] (b2f3db9e-8df6-427b-9241-441baa5042d8) {'id': 'b2f3db9e-8df6-427b-9241-441baa5042d8', 'created_at': datetime.datetime(2023, 7, 13, 11, 16, 59, 826974), 'updated_at': datetime.datetime(2023, 7, 13, 11, 16, 59,827007)}
(hbnb)
```
- This command goes with the BaseModel, id, and the field to add, in the next example we are adding the fiel "first_name": update <class_name> <_id>
```bash
(hbnb) update BaseModel b2f3db9e-8df6-427b-9241-441baa5042d8 first_name "allie"
(hbnb) show BaseModel b2f3db9e-8df6-427b-9241-441baa5042d8
[BaseModel] (b2f3db9e-8df6-427b-9241-441baa5042d8) {'id': 'b2f3db9e-8df6-427b-9241-441baa5042d8', 'created_at': datetime.datetime(2023, 7, 13, 11, 30, 47, 847415), 'updated_at': datetime.datetime(2023, 7, 13, 11, 30, 47,847449), 'first_name': 'allie'}
(hbnb)
```
- This command follow by the id of the BaseModel, delete the BaseModel: destroy <class_name> <_id>
```bash
(hbnb) destroy BaseModel b2f3db9e-8df6-427b-9241-441baa5042d8
(hbnb) show BaseModel b2f3db9e-8df6-427b-9241-441baa5042d8
** no instance found **
(hbnb)
```

- This command is to exit the console:
```bash
(hbnb) quit
$
```

## Documentation 
For more information and a full list of available commands, refer to the project documentation.

## Author
- `Ghelder` | [Github](https://github.com/Ghelder)
