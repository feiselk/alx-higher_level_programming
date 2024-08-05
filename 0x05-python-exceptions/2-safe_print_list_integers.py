#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        new_list = []
        for i in range(len(my_list)):
            if isinstance(my_list[i], int):
                new_list.append(my_list[i])

     
        for i in range(x):
            print("{:d}".format(new_list[i]), end = '')
            count += 1

        if i <= x:
            print()
            try:
                if count > 5:
                    raise IndexError
            except IndexError:
                print("IndexError: list index out of range")
    except TypeError:
        pass               
        
    return count
