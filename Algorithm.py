# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:10:44 2019

@author: Hp
"""

class Algorithm(object):
    HAS_CYCLE = False;  # because we want no negative cycles

    def calculateShortestPath(self, vertexList, edgeList, startVertex):
            startVertex.minDistance = 0
            for i in range(0, len(vertexList) - 1):
                for edge in edgeList:

                    u = edge.startVertex
                    v = edge.targetVertex
                    newDistance = u.minDistance + edge.weight

                    if newDistance < v.minDistance:
                        v.minDistance = newDistance
                        v.predecessor = u

                for edge in edgeList:
                        if self.hasCycle(edge):
                            print("negative cycle detected, hence the following graph is not a valid network.\n")
                            self.HAS_CYCLE = True
                            return



    def hasCycle(self, edge):
            if (edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
                return True
            else:
                return False



    def getShortestPathTo(self, targetVertex):
            if(self.HAS_CYCLE):
                print("bellman ford algorithm not applicable to given graph.")
            elif(targetVertex.minDistance < 0):
                print("Shortest path to targetVertex is negative.\nThis means we are getting paid for travelling from source to destination.\nHence distance is:\t", -1*targetVertex.minDistance)
                node = targetVertex

                while node is not None:
                    print("%s -> " % node.name)
                    node = node.predecessor
            else:
                print("shortest path to target vertex is positive and is given by",targetVertex.minDistance)

                node = targetVertex

                while node is not None:
                    print("%s -> " % node.name)
                    node = node.predecessor
