# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:09:26 2019

@author: Hp
"""
import sys


class Node(object):

    def __init__(self,name):
        self.name = name
        self.visited = False
        self.adjacenciesList = []
        self.predecessor = None
        self.minDistance = 9999;

