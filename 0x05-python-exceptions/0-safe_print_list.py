#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        breezy = 0
        for i in range(x):
            print(my_list[i], end="")
            breezy += 1
    except IndexError:
        pass
    finally:
        print()
        return breezy
