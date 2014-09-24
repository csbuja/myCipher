import sys
from islandmap import IslandMap
from islandnode import Node

class InputReader(object):
    def __init__(self):
        self.map = IslandMap();
    def readIn(self):
        #update dimensions of the map
        self.map.dimensions = int (sys.stdin.readline().rstrip('\n') )
        if (self.map.dimensions <= 0): 
            return # this makes the number of islands 0

        #for each line after the dimensions line create nodes constructed using the number seen on that row
        #add that line to the map of nodes
        count = 0
        while True:
            line = sys.stdin.readline().rstrip('\n')
            nodeLine = []
            for item in line:
                nodeLine.append(Node(int(item)))

            self.map.append(nodeLine)
            count += 1
            if count == self.map.dimensions:
                break
