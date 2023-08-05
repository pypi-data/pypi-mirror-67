#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 22:37:23 2020

@author: Sara Ben Shabbat
"""

import sbs


# Define a variable
author_name = 'Sara Ben Shabbat'

# Define a function
def hello_world() -> None:
    print('Hello World !')
    
# Define a class
class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_fruit_attributes(self):
        print('The fruit name is = ' + self.name)
        print('The fruit color is = ' + self.color)

