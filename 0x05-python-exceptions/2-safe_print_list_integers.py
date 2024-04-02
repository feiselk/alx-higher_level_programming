#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    breezy = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], x):
                print("{:d}".format(my_list=[i]), end="")
                breezy += 1
        except (ValueError, TypeError):
            pass
    print()
    return breezy
