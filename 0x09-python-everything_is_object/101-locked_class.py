#!/usr/bin/python3
'''Module for LockedClass.'''


class LockedClass:
    '''A class demonstrating locked slots and prevents user from dynamically creating new instance attributes.'''
    __slots__ = 'first_name',
