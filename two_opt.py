import time
import sys
from helpers import calculateTotalDistance



def twoOptHeuristicSoln(s, timeAvailable):       
    improvement = True
    start = time.time()
    end = start + timeAvailable
    while improvement: 
        improvement = False
        best_distance = calculateTotalDistance(s)
        i = 0
        while i < len(s):
            for k in range(i+1, len(s)):
                new_route = twoOptSwap(s, i, k)
                new_distance = calculateTotalDistance(new_route)
                if new_distance < best_distance:
                    s = new_route
                    best_distance = new_distance
                    improvement = True
                    i = 0
                if time.time() > end:
                    
                    return s
            i+=1  
    print("time takes for 2opt>>", time.time() - start)
    return s  

   
def twoOptSwap(route, i, k):
    new_route = []
    
    # adding route[0] to route[i] to the new route
    for index in range(0, i+1):
        new_route.append(route[index])
    
    # reversing route[i+1] to route[k] and adding them to the new route(Route[k]  >towards> Route[i+1])
    for index in range(k, i, -1):
        new_route.append(route[index])
    
    # adding route[k+1] to the end to the new route
    for index in range(k+1, len(route)):
        new_route.append(route[index])
    
    return new_route
