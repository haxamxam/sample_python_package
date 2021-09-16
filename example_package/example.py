import pathlib

#use for current working directory
script_dir = pathlib.Path().resolve()

#if want to check where script is being run
#script_dir = pathlib.Path(__file__).resolve().parent

def add_one(number):
    return number + 1

def return_dir():
    return script_dir