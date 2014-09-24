import sys

class Robot(object):
    def __init__(self):
        self.inputString = ''
        self.x = 0
        self.y = 0
        self.direction = 'N'
    def printBot(self):
        print (str(self.x) + ' ' + str(self.y) + ' ' + self.direction)
    def readIn(self):
        self.inputString = sys.stdin.readline().rstrip('\n')
    def followInputDirections(self):
        for val in self.inputString: #make the robot move!
            self.movePosition(val)
    def movePosition(self, char):
        if char == 'C': #clockwise
            if self.direction == 'N':
                self.direction = 'NE'
            elif self.direction == 'NE':
                self.direction = 'E'
            elif self.direction == 'E':
                self.direction = 'SE'
            elif self.direction == 'SE':
                self.direction = 'S'
            elif self.direction == 'S':
                self.direction = 'SW'
            elif self.direction == 'SW':
                self.direction = 'W'
            elif self.direction == 'W':
                self.direction = 'NW'
            elif self.direction == 'NW':
                self.direction = 'N'
            else:
                print 'Bad Direction'
        elif char == 'A': #counter-clockwise
            if self.direction == 'N':
                self.direction = 'NW'
            elif self.direction == 'NE':
                self.direction = 'N'
            elif self.direction == 'E':
                self.direction = 'NE'
            elif self.direction == 'SE':
                self.direction = 'E'
            elif self.direction == 'S':
                self.direction = 'SE'
            elif self.direction == 'SW':
                self.direction = 'S'
            elif self.direction == 'W':
                self.direction = 'SW'
            elif self.direction == 'NW':
                self.direction = 'W'
            else:
                print 'Bad Direction'
        elif char == 'S': #step
            if self.direction == 'N':
                self.y += 1 
            elif self.direction == 'NE':
                self.x += 1
                self.y += 1
            elif self.direction == 'E':
                self.x += 1
            elif self.direction == 'SE':
                self.x += 1
                self.y -= 1
            elif self.direction == 'S':
                self.y -= 1
            elif self.direction == 'SW':
                self.x -= 1
                self.y -= 1
            elif self.direction == 'W':
                self.x -= 1
            elif self.direction == 'NW':
                self.x -= 1
                self.y += 1
            else:
                print 'Bad Direction'
        else:
            print 'Bad Input String'
