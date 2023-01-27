import sys
from helpers import calculateDistance

## This function takes an arbitrary route and returns the approximation route using the nearest neighbor heuristic algoriithm
## Time complexity = O(n²)
def nearestNeighbor(route):
    new_route = []
    current_node = route.pop(0)
    new_route.append(current_node)
    while route != []:
        next = findClosestNeighbor(current_node, route)
        ## Switching to the closest node and setting the pointer on it
        current_node = next
        route.remove(next)
        new_route.append(current_node)
        
    return new_route
        
            
def findClosestNeighbor(v, route):
    ## This function loops through the whole set and finds the smallest distance from the souce node
    shortestEdgeLength = float('inf')
    closestNeighbor = None
    for c in route:
        ## Checking if we are not getting the same node
        if c.id != v.id:
            distance = calculateDistance(v, c)
            ## If found length smaller than current then replacing the node
            if shortestEdgeLength > distance:
                closestNeighbor = c
                shortestEdgeLength = distance
                
    return closestNeighbor
    