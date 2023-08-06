[![PyPI version](https://badge.fury.io/py/mpp.svg)](https://badge.fury.io/py/mpp)

# My Python Project

## Description

A simple tool to create a project with Python, an executable and an installer.

It's only for Windows, but future versions will make it independent of the operating system.

## Installation

`mpp` can be installed using the pip package manager:

```
$ pip install mpp
```

## Usage

We will see the main commands here. For more information, check the [Wiki](https://github.com/deplanty/mpp/wiki)!

Let's create a project together:

```
$ mkdir mpp_tuto
$ cd mpp_tuto
```

### Setup your project easily

Just answer the questions, where the default values are between square brackets:

```
$ mpp setup
What is your project name? [mpp_tuto] mpp Tuto
What is your author name? [username] Name

The project's version is 0.0.0.
The project's icon can be found here: resources/images/icon.ico.
The `main.py` file can now be edited.

Use `mpp --help` to display all possible commands.
Use `mpp <command> -h` to display the help for a command.
Use `mpp config --list` to show your project settings.
```

### Show your configuration

```
$ mpp config --list
 -→ name = MPP Tuto
 -→ author = Name
 -→ version = 0.0.0
 -→ resources = ['resources', '.mpp_config']
 -→ icon = resources/images/icon.ico
 -→ console = True
 -→ hidden-imports = []
```

### Edit your configuration

```
$ mpp config author version
What is your author name? [Name] John
What is the new version? [0.0.0] 0.0.1

Are you sure of your modifications (y/n)? y
```

### Process your project version

Show your project version:

```
$ mpp version
Project 0.0.0
```

Increment the version:

```
$ mpp version +
Project 0.0.1

$ mpp version ++
Project 0.1.0

$ mpp version +++
Project 1.0.0
```

### Freeze your project with [PyInstaller](https://www.pyinstaller.org/)

```
$ mpp freeze
It seems that PyInstaller is not installed.
Please, consider using `pip install PyInstaller`.
Current pip is path/to/pip.
Do you want to install it now (y/n)? [y]
[pip output]

[PyInstaller outpout]

Executable can be found here: target/Project/Project.exe
```

### Create an installer for your project with [NSIS](https://nsis.sourceforge.io/Main_Page)

```
$ mpp installer
NSIS needs "ShellExecAsUser" in order to create the installer.
Do you want to download it (y/n)? [y]

Downloading... Done
[NSIS output]

Installer can be found here: target/Project_setup.exe
```

## Credits

This project was originally inspired from [fbs](https://github.com/mherrmann/fbs).
