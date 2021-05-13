print("samsam")

a=["Je veux", "manger", "un", "autre cookie", ["mais", "je", "n'en ai", "plus"]]

#chaîne de caractères
def get_size_file(file):
    return len(file)

def is_a_folder(a):
    if type(a)==list :
        return True
    else:
        return False

def get_size(a):
    size=0
    if is_a_folder(a):
        for element in a:
            size += get_size(element)
    else:
        size+=get_size_file(a)
    return size

# example of recursive function
def function(a):
    print(a)
    if a>=1:
        function(a-1)










