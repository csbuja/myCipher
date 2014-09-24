class Node(object):
    def __init__(self, isIsland):
        if not isIsland:
            self.isIsland = False
        else:
            self.isIsland = True
        self.visited = False
    def shouldExplore(self):
        return (self.isIsland and (not self.visited))
    def printNode(self):
        if(self.isIsland and self.visited):
            print 'It is an Island and has been visited.'
        if(not self.isIsland and self.visited):
            print 'It is not an Island and has been visited.'
        if(self.isIsland and not self.visited):
            print 'It is an Island and has not been visited.'
        if(not self.isIsland and not self.visited):
            print 'It is not an Island and has not been visited.'
            