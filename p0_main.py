from p0_inputReader import InputReader

data = InputReader()
data.readIn()

for lineidx, line in enumerate(data.map.matrix):
	for nodeidx, node in enumerate(line):
		if ( node.shouldExplore() ):
			node.visited = True
			data.map.exploreIsland([nodeidx,lineidx])
			data.map.addAnotherIsland()		

data.map.printAverageIslandSize()
