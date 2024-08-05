#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        num = x
        new_list = [item for item in my_list if isinstance(item, int)]

        count = 0
        if x <= 5:
            for i in range(x):
                print("{:d}".format(new_list[i]), end = '')
                count += 1
            print()
            return count
        elif x > 5 and x <= 8:
            x = 5
            for i in range(x):
                print("{:d}".format(new_list[i]), end = '')
                count += 1
            print()
            return count
        elif x > 8:
                for i in range(x):
                    print("{:d}".format(new_list[i]), end = '')
                    count += 1
                return count
    except TypeError:
        pass
