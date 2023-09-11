#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listidx = 0
    while listidx < x:
        try:
            print("{}".format(my_list[listidx]), end="")
        except IndexError:
            break
        listidx += 1
    print("")
    return listidx
