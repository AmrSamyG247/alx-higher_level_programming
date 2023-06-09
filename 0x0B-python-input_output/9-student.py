#!/usr/bin/python3
'''
class Student that defines a student by
Public instance attributes
'''


class Student:
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Constructor method '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Method that returns directory description '''
        return self.__dict__.copy()
