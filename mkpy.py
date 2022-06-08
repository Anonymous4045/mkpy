from os import system

args = input('Name,version: ')

s = args.count(' ')

if not s:
    name = args
    system(f'mkdir {name}; cd {name}; touch main.py')
elif s == 1:
    name, version = args.split()
    system(f'mkdir {name}; cd {name}; touch main.py; pyenv local {version}')

system(f'cd {name}; python3 -m venv Venv; . Venv/bin/activate')
