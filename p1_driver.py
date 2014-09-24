from p1_robot import Robot

if __name__ == "__main__":
	roboExplorer = Robot()
	roboExplorer.readIn()
	roboExplorer.followInputDirections()
	roboExplorer.printBot()