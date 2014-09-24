import sys
from islandmap import IslandMap
from islandnode import Node

class InputReader(object):
    def __init__(self):
        self.map = IslandMap();
    def readIn(self):
        self.map.dimensions = int (sys.stdin.readline().rstrip('\n') )
        if (self.map.dimensions <= 0): 
            return # this makes the number of islands 0

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
