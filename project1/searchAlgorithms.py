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
    def __init__(self, verticesX,verticesY,game,problem,heuristic):  
        self.VX = verticesX-20
        self.VY = verticesX-20
        self.game=game
        self.path={}
        self.start=(20,20)  
        self.heuristic=heuristic
        self.problem=problem
        
        current,tail=problem.getStartState()
        successors= problem.getSuccessors(current,tail)
        stateSuccessor,d,_=successors[0]
        nextc,tail=stateSuccessor
        x,y=current
        nx,ny=nextc
        self.path[x]=nx
        self.prev={}
        current=nextc
        see=[]
        while True:
            # See if it is the start
            if problem.isGoalState(current)==True:
                keys=self.path.keys()
                for i in keys:
                    if self.path[i]==current:
                        self.prev[current]=i
                break

                
            # Find the successors and put them to see them
            m=-1
            nextc=current
            successors= problem.getSuccessors(current,tail)
            for i in range(0,len(successors)):
                stateSuccessor,directionSuccessor,cost=successors[i]         

                state,tail=stateSuccessor

                if state in see:
                    continue

                # We cuclulate the new cost path with the new nodes
                hCost = self.heuristic(state,problem)
                if m<hCost:
                    m=hCost
                    nextc=state 
            x,y=current
            nx,ny=nextc
            self.path[x]=nx
            self.prev[nx]=x
            see.append(current)
            current=nextc
        self.staticPath=self.path
        self.staticPrev=self.prev

    def getDiraction(self,path,snake):
        previous=None
        diractions={}
        previous = snake
        current=path[snake]
        while current!=snake:
            xp,yp=previous
            xc,yc=current
            diractions[previous]=util.giveDiraction(xc,yc,xp,yp)
            previous=current
            current=path[previous]
        diractions[previous]=util.giveDiraction(xc,yc,xp,yp)
        return diractions

    def normCycle(self,snake):
        diraction=self.getDiraction(self.staticPath,snake)
        return list(diraction.values())