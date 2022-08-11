import os
import subprocess

def read_config():
    with open("config.txt","r") as txt:
        params_list = txt.readlines()
        for param in params_list: params_list[params_list.index(param)] = params_list[params_list.index(param)].replace("\n","")
        params_list[0] = params_list[0].replace("/","\\")
        return params_list
    # Lines
    # Path where folders with projects
    # Path to VScode
    

def make_project(name):
    params = read_config()
    os.mkdir(f"{params[0]}\{name}")
    os.mkdir(f"{params[0]}\{name}\source")
    with open(f'{params[0]}\{name}\main.py', 'w') as f:
        f.write(f'project - {name}')
    



def main():
    make_project(input("Enter name project - "))


if __name__ == "__main__":
    main()