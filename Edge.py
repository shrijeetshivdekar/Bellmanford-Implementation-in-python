# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:09:59 2019

@author: Hp
"""

class Edge(object):

    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex
