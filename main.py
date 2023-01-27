

import math
import sys
import time
import tsplib95
import copy
import random
from os import listdir

from helpers import preProcess,preProcess_Octagon_NN_1, preProcess_Octagon_NN_2, preProcess_Octagon_2Opt,printTourDistance,testVertices, printTour
from nearest_neighbor import nearestNeighbor
from two_opt import twoOptHeuristicSoln

def main(fileName, timeForTwoOpt):
        tspData = tsplib95.load('./exercise04/test_cases/'+fileName)       
        s = preProcess(tspData.node_coords)
        print("\n1st solution > ")

        printTourDistance(s)

        routeCopy = copy.deepcopy(s)
        nearestNeighborRes = nearestNeighbor(routeCopy)

        print("\nNew Distane after running nearest neighbor heuristic algorithm: ")  
        printTourDistance(nearestNeighborRes)

        twoHeuristicSolnAns = twoOptHeuristicSoln(nearestNeighborRes, timeForTwoOpt)

        print("\nAFTER 2OPT")  
        printTourDistance(twoHeuristicSolnAns)
        print("Testing Output of original and nearesr neighbor solution")
        testVertices(s, nearestNeighborRes)
        print("Testing Output of original and 2Opt solution")
        testVertices(s, twoHeuristicSolnAns)

def main_OctagonTest():

        print("Test NN 1:")
        routeCopy = preProcess_Octagon_NN_1()
        printTour(routeCopy)
        nearestNeighborRes = nearestNeighbor(routeCopy)
        printTour(nearestNeighborRes)
        print("\n\n")

        print("Test NN 2:")
        routeCopy = preProcess_Octagon_NN_2()
        printTour(routeCopy)
        nearestNeighborRes = nearestNeighbor(routeCopy)
        printTour(nearestNeighborRes)
        print("\n\n")

        
        print("Test 2Opt:")
        routeCopy = preProcess_Octagon_2Opt()
        printTour(routeCopy)
        twoHeuristicSolnAns = twoOptHeuristicSoln(routeCopy, 10)
        printTour(twoHeuristicSolnAns)


print("Choose 1 to run all files test, 2 to run for single file of choice, 8 to run for simple Octagon Testcase")
choice = int(input())
timeForTwoOpt = 100.0
if(choice == 1):
    print("Enter how many files you want to test. Value should be lest than or equal to 28")
    fileCount = int(input())
    filesList = listdir(path="./exercise04/test_cases/")
    print(fileCount, "files will be tested.")
    for i in range(len(filesList)):
        if(i>=fileCount):
            break
        print("\nTesting file >> ",filesList[i] )
        main(filesList[i],timeForTwoOpt )

elif(choice== 2):
    # Please choose the file you want to test
    fileName = "02_dj38.tsp"
    main(fileName, timeForTwoOpt)

elif(choice== 8):
    main_OctagonTest()
    



