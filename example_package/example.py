import pathlib

script_dir = pathlib.Path(__file__).resolve().parent

def add_one(number):
    return number + 1

def return_dir():
    return script_dir