
import math
import sys
import tsplib95


class node  :
    
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.visited = False
       
def printTourDistance(s):
    print("Distance >>  " + str(calculateTotalDistance(s)))

 

def calculateDistance(city1, city2):

    x_distance = abs(city1.x - city2.x)
    y_distance = abs(city1.y - city2.y)
    
    return int(round(math.sqrt(x_distance * x_distance + y_distance * y_distance)))
   
  
def preProcess(coordinates):
    vertices = []
    for idx in range(1, len(coordinates)+1):
        numArray = []
        numArray = coordinates[idx]
        # for num in lineNumbers:
        #     numArray.append(int(num))
        vertices.append(node(idx, numArray[0], numArray[1]))
    return vertices

def preProcess_Octagon_NN_1():

    r = 1000
    print("Make Octagon... Order {3,4,6,8,7,5,2,1}")

    vertices = []
    vertices.append(node(3, r * math.cos(math.radians(30)), r * math.sin(math.radians(30))))
    vertices.append(node(4, r * math.cos(math.radians(60)), r * math.sin(math.radians(60))))
    vertices.append(node(6, r * math.cos(math.radians(150)), r * math.sin(math.radians(150))))
    vertices.append(node(8, r * math.cos(math.radians(280)), r * math.sin(math.radians(280))))
    vertices.append(node(7, r * math.cos(math.radians(210)), r * math.sin(math.radians(210))))
    vertices.append(node(5, r * math.cos(math.radians(100)), r * math.sin(math.radians(100))))
    vertices.append(node(2, r * math.cos(math.radians(10)), r * math.sin(math.radians(10))))
    vertices.append(node(1, r * math.cos(math.radians(0)), r * math.sin(math.radians(0))))
 
    return vertices

def preProcess_Octagon_NN_2():

    r = 1000
    print("Make Octagon... Order {4,2,6,8,7,5,3,1}")

    vertices = []
    vertices.append(node(4, r * math.cos(math.radians(60)), r * math.sin(math.radians(60))))
    vertices.append(node(2, r * math.cos(math.radians(10)), r * math.sin(math.radians(10))))
    vertices.append(node(6, r * math.cos(math.radians(150)), r * math.sin(math.radians(150))))
    vertices.append(node(8, r * math.cos(math.radians(280)), r * math.sin(math.radians(280))))
    vertices.append(node(7, r * math.cos(math.radians(210)), r * math.sin(math.radians(210))))
    vertices.append(node(5, r * math.cos(math.radians(100)), r * math.sin(math.radians(100))))
    vertices.append(node(3, r * math.cos(math.radians(30)), r * math.sin(math.radians(30))))
    vertices.append(node(1, r * math.cos(math.radians(0)), r * math.sin(math.radians(0))))

    return vertices


def preProcess_Octagon_2Opt():

    r = 1000
    print("Make Octagon... 2 Swaped {1,8,3,2,7,6,5,4}")

    vertices = []
    vertices.append(node(1, r * math.cos(math.radians(0)), r * math.sin(math.radians(0))))
    vertices.append(node(8, r * math.cos(math.radians(280)), r * math.sin(math.radians(280))))
    vertices.append(node(3, r * math.cos(math.radians(30)), r * math.sin(math.radians(30))))
    vertices.append(node(2, r * math.cos(math.radians(10)), r * math.sin(math.radians(10))))
    vertices.append(node(7, r * math.cos(math.radians(210)), r * math.sin(math.radians(210))))
    vertices.append(node(6, r * math.cos(math.radians(150)), r * math.sin(math.radians(150))))
    vertices.append(node(5, r * math.cos(math.radians(100)), r * math.sin(math.radians(100))))
    vertices.append(node(4, r * math.cos(math.radians(60)), r * math.sin(math.radians(60))))

    return vertices

def calculateTotalDistance(route):

    tot = 0
    for idx in range(0, len(route)-1):
        tot += calculateDistance(route[idx], route[idx+1])
    tot += calculateDistance(route[len(route)-1], route[0])
    
    return tot

def testVertices(route1, route2):
    # This will check if vertice count of both routes are same or not and 
    # also checks from original route if all vertices are present in the optimized orute
    if(len(route1) != len(route2)):
        print("The result edges count is not same as the main edges count")
    match = 0
    notMatch = 0
    for i in range(len(route1)):
        checkPoint = route1[i]
        found = False
        for j in range(len(route2)):
            if(checkPoint.id ==route2[j].id):
                found = True
                match +=1
                break
            if(j == len(route2)-1 and found ==False):
                print("Point not found", checkPoint['x'], checkPoint['y'])
                notMatch += 1
    if(notMatch == 0):
        print("Test result: Success >>",{"Matches": match, "No Matches":notMatch})
    else:
        print("Test result: Failure >>",{"Matches": match, "No Matches":notMatch})
    
def printTour(verticies):
    for node in verticies:
        print(node.id, end=",")

    print("")
    
