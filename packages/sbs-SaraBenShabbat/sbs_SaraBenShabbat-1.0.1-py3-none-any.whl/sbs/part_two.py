# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 04:11:06 2020

@author: User
"""



# Define a class
class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_fruit_attributes(self):
        print('The fruit name is = ' + self.name)
        print('The fruit color is = ' + self.color)
