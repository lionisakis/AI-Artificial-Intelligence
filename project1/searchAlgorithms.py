import util

def depthFirstSearch(problem):
    dist={}  # The distance so far for that node
    prev={}  # The previous node for knowing the path
    direc={}  # The way we got to the current node
    
    # The way with we will get the next value 
    stack=util.Stack() 

    start,tail= problem.getStartState()
    
    # Starting values for our Maps
    dist[start]=0
    prev[start]= None
    direc[start]=None
    stack.push((start,tail))  

    current=start
    while stack.isEmpty()==False:
        current,tail = stack.pop()

        # See if it is the Goal
        if problem.isGoalState(current)==True:
            problem.removeFinalOutline()
            problem.addFinalOutline(tail)
            break

        # Find the successors and put them to see them
        successors= problem.getSuccessors(current,tail)
        for i in range(0,len(successors)):
            stateSuccessor,directionSuccessor,cost=successors[i]
            state,tails=stateSuccessor

            # Put the values in the maps
            prev[state]=current
            direc[state]=directionSuccessor
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

    dist={}  # The distance so far for that node
    prev={}  # The previous node for knowing the path
    direc={}  # The way we got to the current node
    
    # The way with we will get the next value 
    queue=util.Queue() 

    start,tail= problem.getStartState()
    
    # Starting values for our Maps
    dist[start]=0
    prev[start]= None
    direc[start]=None
    queue.push((start,tail))  

    current=start
    while queue.isEmpty()==False:
        current,tail = queue.pop()

        # See if it is the Goal
        if problem.isGoalState(current)==True:
            problem.removeFinalOutline()
            problem.addFinalOutline(tail)
            break

        # Find the successors and put them to see them
        successors= problem.getSuccessors(current,tail)
        for i in range(0,len(successors)):
            stateSuccessor,directionSuccessor,cost=successors[i]
            x,y=stateSuccessor

            # Put the values in the maps if we have not seen them 
            if x not in prev.keys():
                prev[x]=current
                direc[x]=directionSuccessor
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
    
    dist={}  # The distance so far for that node
    prev={}  # The previous node for knowing the path
    direc={}  # The way we got to the current node
    
    # The way with we will get the next value 
    pq=util.PriorityQueue()

    # Starting values for our Maps
    start,tail= problem.getStartState()
    dist[start]=0
    prev[start]= None
    direc[start]=None
    pq.push((start,tail),0)  

    current=start
    while pq.isEmpty()==False:


        # Tell we have see them
        current,tail = pq.pop()

        # See if it is the Goal
        if problem.isGoalState(current)==True:
            problem.removeFinalOutline()
            problem.addFinalOutline(tail)
            break
        
        # Find the successors and put them to see them
        successors= problem.getSuccessors(current,tail)
        for i in range(0,len(successors)):
            stateSuccessor,directionSuccessor,cost=successors[i]

            state,tail=stateSuccessor

            # Check if we have already check it cost so far
            if state  in dist.keys():
                alt = dist[current] + cost

                # If the new cost path is less than the previous
                # replace everything with the new path
                if  alt < dist[state]:
                    dist[state]=alt
                    prev[state]=current
                    direc[state]=directionSuccessor
                    pq.update(stateSuccessor,dist[state])

            else:

                # We have not see this node again so put everything again
         
                alt = dist[current] + cost
                dist[state]=alt
                prev[state]=current
                direc[state]=directionSuccessor
                pq.push(stateSuccessor,dist[state])

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

    dist={}  # The distance so far for that node
    prev={}  # The previous node for knowing the path
    direc={}  # The way we got to the current node
    fcost={}  # For knowing the cost with the Hcost+ Gcost so far

    # The way with we will get the next value
    pq=util.PriorityQueue()      
    
    # Starting values for our Maps
    start,tail= problem.getStartState()
    dist[start]=0
    prev[start]= None
    direc[start]=None
    pq.push((start,tail),0)  


    fcost[start]=0
    current=start
    while pq.isEmpty()==False:
        current,tail = pq.pop()


        # See if it is the Goal
        if problem.isGoalState(current)==True:
            problem.removeFinalOutline()
            problem.addFinalOutline(tail)
            break

         
        # Find the successors and put them to see them
        successors= problem.getSuccessors(current,tail)
        for i in range(0,len(successors)):
            stateSuccessor,directionSuccessor,cost=successors[i]         

            state,tail=stateSuccessor
            
            # We cuclulate the new cost path with the new nodes
            hCost = heuristic(state,problem)
            gCost = dist[current] + cost
            fCost = hCost+gCost
            
            # Check if we have already check it cost so far
            if state  in fcost.keys() :
                
                # If the new cost path is less than the previous
                # replace everything with the new path
                if(fCost < fcost[state]):
                    dist[state]=gCost
                    prev[state]=current
                    direc[state]=directionSuccessor

                    fcost[state]=fCost
                    pq.update(stateSuccessor,fCost)

            else:
                # We have not see this node again so put everything again
                dist[state]=gCost
                prev[state]=current
                direc[state]=directionSuccessor

                fcost[state]=fCost
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

class Graph():  
    def __init__(self, verticesX,verticesY,game):  
        self.VX = verticesX-20
        self.VY = verticesX-20
        self.game=game
        self.path=[]
        self.start=(20,20)  
  
    def hamCycleUtil(self, path, pos):  
  
        if pos == self.start:  
            return True

        x,y=pos
        x=int(x)
        y=int(y)
        theNextPoint =self.nextPoints(pos)[-1]
        path[pos] = theNextPoint 
        if self.hamCycleUtil(path, theNextPoint) == True:  
            return True
        return False
  
    def nextPoints(self,point):
        queue=[]
        v1,v2=point
        # begin
        if (v1,v2)==(20,20):
            queue.append((20,40))
            return queue
        # the top line 
        elif v2==20:
            queue.append((v1-20,v2))
            return queue
        # the last line
        elif v1==self.VX:
            queue.append((v1,v2-20))
            return queue
        # when to go right
        elif int(v1/10)%4==0 and v2==40:
            queue.append((v1+20,v2))
            return queue
        # when to go up
        elif int(v1/10)%4==2 and v2==40:
            queue.append((v1,v2+20))
            return queue
        # when to go down
        elif int(v1/10)%4==2 and v2!=self.VY-20:
            queue.append((v1,v2+20))
            return queue
        # when to go up
        elif int(v1/10)%4==0 and v2!=self.VY-20:
            queue.append((v1,v2-20))
            return queue
        # when to go right
        elif v2==self.VY-20 and int(v1/10)%4==2:
            queue.append((v1+20,v2))
            return queue
        # when to go up
        elif v2==self.VY-20 and int(v1/10)%4==0:
            queue.append((v1,v2-20))
            return queue
        return queue
    

    def hamCycle(self,begin):  
        self.start=begin
        self.path={}
        for i in self.nextPoints(begin):
            self.path[begin] = i 
            if self.hamCycleUtil(self.path,i)==True:  
                return True
        print ("Solution does not exist\n")   
        return False
  
    def printSolution(self, path):  
        print ("Solution Exists: Following", 
                 "is one Hamiltonian Cycle") 
        for vertex in path:  
            print (vertex, end = " ") 
        print (path[0], "\n") 
