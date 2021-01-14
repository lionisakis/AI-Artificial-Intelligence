# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    Current={} # a Map in which we saw which nodes we have seen
    dist={}  # The distance so far for that node
    prev={}  # The previous node for knowing the path
    direc={}  # The way we got to the current node
    
    # The way with we will get the next value 
    stack=util.Stack() 

    start= problem.getStartState()
    
    # Starting values for our Maps
    dist[start]=0
    prev[start]= None
    direc[start]=None
    stack.push(start)  

    current=start
    while stack.isEmpty()==False:
        current = stack.pop()

        # If we have seen them go to next
        if current in Current.keys():
            continue
        
        # Tell we have see the node
        Current[current]=1

        # See if it is the Goal
        if problem.isGoalState(current)==True:
            break

        # Find the successors and put them to see them
        successors= problem.getSuccessors(current)
        for i in range(0,len(successors)):
            stateSuccessor,directionSuccessor,cost=successors[i]
        
            # If we have seen it skip it
            if stateSuccessor in list(Current.keys()):
                continue

            # Put the values in the maps
            prev[stateSuccessor]=current
            direc[stateSuccessor]=directionSuccessor
            stack.push(stateSuccessor)


    # Check if the current value is the goal
    # and not because we run out of nodes to explore
    if problem.isGoalState(current)==True:
        path=[]
        # Insert the way we got it from last to start
        while(True):
            if(current==start):
                return path
            path.insert(0,direc[current])
            current = prev[current]
    else:
        return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    Current={} # a Map in which we saw which nodes we have seen
    dist={}  # The distance so far for that node
    prev={}  # The previous node for knowing the path
    direc={}  # The way we got to the current node
    
    # The way with we will get the next value 
    queue=util.Queue() 

    start= problem.getStartState()
    
    # Starting values for our Maps
    dist[start]=0
    prev[start]= None
    direc[start]=None
    queue.push(start)  

    current=start
    while queue.isEmpty()==False:
        current = queue.pop()

        # If we have seen them go to next
        if current in Current.keys():
            continue
        
        # Tell we have see the node
        Current[current]=1

        # See if it is the Goal
        if problem.isGoalState(current)==True:
            print (1)
            break

        # Find the successors and put them to see them
        successors= problem.getSuccessors(current)
        for i in range(0,len(successors)):
            stateSuccessor,directionSuccessor,cost=successors[i]
        
            # If we have seen it skip it
            if stateSuccessor in Current.keys():
                continue

            # Put the values in the maps if we have not seen them 
            if stateSuccessor not in prev.keys():
                prev[stateSuccessor]=current
                direc[stateSuccessor]=directionSuccessor
                queue.push(stateSuccessor)


    # Check if the current value is the goal
    # and not because we run out of nodes to explore
    
    if(problem.isGoalState(current)):
        path=[]
        # Insert the way we got it from last to start
        while(True):
            if(current==start):
                return path
            path.insert(0,direc[current])
            current = prev[current]
    else:
        return []
    
    # we have not find a solution
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    Current={}     # a Map in which we saw which nodes we have seen 
    dist={}  # The distance so far for that node
    prev={}  # The previous node for knowing the path
    direc={}  # The way we got to the current node
    
    # The way with we will get the next value 
    pq=util.PriorityQueue()

    # Starting values for our Maps
    start= problem.getStartState()
    dist[start]=0
    prev[start]= None
    direc[start]=None
    pq.push(start,0)  

    current=start
    while pq.isEmpty()==False:


        # Tell we have see them
        current = pq.pop()

        # If we have seen them go to next
        if current in Current.keys():
            continue

        # We say that we saw it
        Current[current]=1


        # See if it is the Goal
        if problem.isGoalState(current)==True:
            break
        
        # Find the successors and put them to see them
        successors= problem.getSuccessors(current)
        for i in range(0,len(successors)):
            stateSuccessor,directionSuccessor,cost=successors[i]


            # If we have seen them go to next
            if stateSuccessor in Current.keys():
                continue

            # Check if we have already check it cost so far
            if stateSuccessor  in dist.keys():
                alt = dist[current] + cost

                # If the new cost path is less than the previous
                # replace everything with the new path
                if  alt < dist[stateSuccessor]:
                    dist[stateSuccessor]=alt
                    prev[stateSuccessor]=current
                    direc[stateSuccessor]=directionSuccessor
                    pq.update(stateSuccessor,dist[stateSuccessor])

            else:

                # We have not see this node again so put everything again
         
                alt = dist[current] + cost
                dist[stateSuccessor]=alt
                prev[stateSuccessor]=current
                direc[stateSuccessor]=directionSuccessor
                pq.push(stateSuccessor,dist[stateSuccessor])

    # Check if the current value is the goal
    # and not because we run out of nodes to explore
    if(problem.isGoalState(current)):
        path=[]
        # Insert the way we got it from last to start
        while(True):
            if(current==start):
                return path
            path.insert(0,direc[current])
            current = prev[current]
    else:
        return []

def aStarSearch(problem, heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    Current={}     # a Map in which we hace seen 
    dist={}  # The distance so far for that node
    prev={}  # The previous node for knowing the path
    direc={}  # The way we got to the current node
    fcost={}  # For knowing the cost with the Hcost+ Gcost so far

    # The way with we will get the next value
    pq=util.PriorityQueue()      
    
    # Starting values for our Maps
    start= problem.getStartState()
    dist[start]=0
    prev[start]= None
    direc[start]=None
    pq.push(start,0)  


    fcost[start]=0
    current=start
    while pq.isEmpty()==False:
        current = pq.pop()

        # If we have seen them go to next
        if current in Current.keys():
            continue
        
        # We say that we saw it
        Current[current]=1

       
        # See if it is the Goal
        if problem.isGoalState(current)==True:
            break

         
        # Find the successors and put them to see them
        successors= problem.getSuccessors(current)
        for i in range(0,len(successors)):
            stateSuccessor,directionSuccessor,cost=successors[i]         

            
            # If we have seen them go to next
            if stateSuccessor in Current.keys():
                continue
            
            # We cuclulate the new cost path with the new nodes
            hCost = heuristic(stateSuccessor,problem)
            gCost = dist[current] + cost
            fCost = hCost+gCost
            
            # Check if we have already check it cost so far
            if stateSuccessor  in fcost.keys() :
                
                # If the new cost path is less than the previous
                # replace everything with the new path
                if(fCost < fcost[stateSuccessor]):
                    dist[stateSuccessor]=gCost
                    prev[stateSuccessor]=current
                    direc[stateSuccessor]=directionSuccessor

                    fcost[stateSuccessor]=fCost
                    pq.update(stateSuccessor,fCost)

            else:
                # We have not see this node again so put everything again
                dist[stateSuccessor]=gCost
                prev[stateSuccessor]=current
                direc[stateSuccessor]=directionSuccessor

                fcost[stateSuccessor]=fCost
                pq.push(stateSuccessor,fCost)
    
    # Check if the current value is the goal
    # and not because we run out of nodes to explore
    if(problem.isGoalState(current)):
        path=[]
        # Insert the way we got it from last to start                    
        while(True):
            if(current==start):
                return path

            path.insert(0,direc[current])
            current = prev[current]

    else:
        return []