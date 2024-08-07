#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                # Try to format and print the integer
                print("{:d}".format(my_list[i]), end="")
                count += 1
            else:
                pass
        print()
    except (TypeError):
        pass

    return count
