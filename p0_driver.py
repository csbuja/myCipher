from p0_inputReader import InputReader

data = InputReader()
data.readIn()

#go through every node on the island
#if there is an island worth exploring, explore it then add its size to the to the total size and increment the number Islands seen
if __name__ == "__main__":
	for lineidx, line in enumerate(data.map.matrix):
		for nodeidx, node in enumerate(line):
			if ( node.shouldExplore() ):
				#the node is now visited, so we don't explore this section of the island again and get an error
				node.visited = True 
				data.map.exploreIsland([nodeidx,lineidx])
				#increment the number of islands seen thus far
				data.map.addAnotherIsland()		

	data.map.printAverageIslandSize()
