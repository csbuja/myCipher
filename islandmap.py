class IslandMap(object):
    def __init__(self):
        self.matrix = []
        self.numIslands = 0
        self.dimensions = 0
        self.totalSize = 0 #the total size of all islands
    def append(self, line):
        self.matrix.append(line)

    #Prints the map inputted from stdin
    def printGeography(self):
        for item in self.matrix:
            line = []
            for val in item:
                if(val.isIsland):
                    line.append(1)
                else:
                    line.append(0)
            print line

    #Prints which nodes have been visited on the map
    def printVisited(self):
        for item in self.matrix:
            line = []
            for val in item:
                if(val.visited):
                    line.append(1)
                else:
                    line.append(0)
            print line
            
    #Used for conditionals during the exploration of an island
    #the argument nodePos is passed as coordinate [x,y]
    def canMoveHere(self, nodePos): 
        if (nodePos[0] < 0) or (nodePos[0] >= self.dimensions) or (nodePos[1] < 0) or (nodePos[1] >= self.dimensions):
            return False
        #it is a node
        if self.matrix[nodePos[1]][nodePos[0]].shouldExplore():
            return True
        else:
            return False

    #Explores the island, marking everything explored as visited
    #The argument nodePos is passed as coordinate [x,y]
    #Modifies self.totalsize when the exploration is done
    def exploreIsland(self, nodePos):
        stack = [ [nodePos[0],nodePos[1]] ]
        #if tuple of [x,y] can be reached then add it to the stack as [x,y]
        # make the pushed node visited by referencing matrix as [y,x]
        size = 1

        while len(stack) is not 0:  
            nodePos = stack[len(stack)-1]
            size+=1
            if self.canMoveHere([ nodePos[0]+1, nodePos[1] ]):  #can move right
                self.matrix[ nodePos[1] ][ nodePos[0]+1 ].visited = True
                stack.append([ nodePos[0]+1 , nodePos[1] ])
            elif self.canMoveHere([ nodePos[0] ,nodePos[1]-1]):  #can move up
                self.matrix[nodePos[1]-1][nodePos[0]].visited = True
                stack.append([nodePos[0],nodePos[1]-1])
            elif self.canMoveHere([ nodePos[0]-1 , nodePos[1] ]):  #can move left
                self.matrix[nodePos[1]][nodePos[0]-1].visited = True
                stack.append([ nodePos[0]-1 , nodePos[1] ])
            elif self.canMoveHere([ nodePos[0] , nodePos[1]+1 ]): #can move down
                self.matrix[nodePos[1]+1][nodePos[0]].visited = True
                stack.append([ nodePos[0] , nodePos[1]+1] )
            else:
                stack.pop()
                size-=1 #only add to size if you have moved

        self.totalSize += size # add island size to total size of all islands

    #divide aggregate total island size by the number of islands
    #convert that number to an integer
    def printAverageIslandSize(self):
        if(self.numIslands == 0 ):
            print 0
        else:
            print int( self.totalSize / self.numIslands)
    def addAnotherIsland(self):
        self.numIslands+=1
