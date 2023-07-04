#!/usr/bin/python3
'''Module for LockedClass.'''


class LockedClass:
    '''A class demonstrating locked slots prevents creating attributes.'''
    __slots__ = 'first_name',

