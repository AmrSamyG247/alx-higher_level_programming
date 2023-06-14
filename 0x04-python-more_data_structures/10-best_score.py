#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxvale = 0
    maxkey = None
    for key, valu in a_dictionary.items():
        if valu > maxvalu:
            maxvalu = v
            maxkey = k
    return maxkey
