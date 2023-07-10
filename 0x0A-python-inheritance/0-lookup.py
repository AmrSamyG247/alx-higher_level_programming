#!/usr/bin/python3
"""lookup function that returns the list objects"""


def lookup(obj):
    """returns list of dir()"""
    return([x for x in dir(obj)])

