# mkpy
A simple command line tool for linux to create python projects.

# Dependencies
To use mkpy, you must have Python installed. In order to create projects in a specific version, you must have pyenv set up (not required to use the package)

# Installation
To install, simply clone this repository to your home directory
```
cd
git clone https://github.com/Anonymous4045/mkpy.git
```
Then, run the `install.sh` script
```
mkpy/install.sh
```
This creates a directory `/usr/local/mkpy/` and adds `mkpy` to `/usr/local/bin/`.

# Usage
You can now use the command `mkpy` in any directory. Navigate to your projects folder and run the following
```
mkpy
```
You will then need to enter one to two things. The first argument is required, whish is the project name. Type any valid directory name. The second argument is optional. If you have pyenv installed, you may specify a python version you have installed. 

Note; multiple options must be entered seperated by a space

Examples:
```
mkpy
Name,version: MyProject
```
```
mkpy
Name,version: SomeProject 3.10.4
```


# Making changes to the script
The python file that is ran is located at `/usr/local/mkpy/mkpy.py`. Open this with your favorite editor and make whichever changes you like.
