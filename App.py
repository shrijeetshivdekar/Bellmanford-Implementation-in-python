# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:11:11 2019

@author: Hp
"""

from Algorithm import Algorithm
from Node import Node
from Edge import Edge

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")


edge1= Edge(5,node1,node2)
edge2= Edge(3,node2,node3)
edge3= Edge(2,node3,node4)
edge4= Edge(-6,node2,node4)
edge5= Edge(4,node1,node4)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge5)
node2.adjacenciesList.append(edge4)
node2.adjacenciesList.append(edge2)
node3.adjacenciesList.append(edge3)

vertexList=[node1,node2,node3,node4]
edgeList=[edge1,edge2,edge3,edge4,edge5]

algorithm = Algorithm()
algorithm.calculateShortestPath(vertexList,edgeList,node1)
algorithm.getShortestPathTo(node4)

"""
neg cycle proof
edge1= Edge(5,node1,node2)
edge2= Edge(3,node2,node3)
edge3= Edge(2,node3,node4)
edge4= Edge(-6,node4,node2)
edge5= Edge(4,node1,node4)

node1.adjacenciesList.append(edge1)
node1.adjacenciesList.append(edge5)
node2.adjacenciesList.append(edge2)
node3.adjacenciesList.append(edge3)
node4.adjacenciesList.append(edge4)

vertexList=[node1,node2,node3,node4]
edgeList=[edge1,edge2,edge3,edge4,edge5]
"""
