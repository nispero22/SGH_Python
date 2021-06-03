
import os

def get_size_file(file):
    return os.path.getsize(file)

def is_a_folder(a):
    if os.path.isdir(a):
        return True
    else:
        return False

def get_size(a):
    size=0
    if is_a_folder(a):
        for element in os.listdir(a):
            size += get_size(f"{a}/{element}")
    else:
        size+=get_size_file(a)
    return size


def get_number_of_file(a):
    number_of_file=0
    if is_a_folder(a):
        for element in os.listdir(a):
            number_of_file += get_number_of_file(f"{a}/{element}")
    else:
        number_of_file+=1
    return number_of_file
