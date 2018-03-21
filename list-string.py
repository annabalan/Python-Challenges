# Write a python program to concatenate all elements in a list into a string and return it.

def concatenate_list():
    l= ["a", "b", "c", "d", "e", "f"]
    l_str = ""
    for i in l:
        l_str += str(i) + " "
    l_str = l_str[:-1]
    print(l_str)

concatenate_list()


