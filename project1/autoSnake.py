import tkinter
import random
import time
import util

RIGHT = "RIGHT"
LEFT = "LEFT"
DOWN = "DOWN"
UP = "UP"
NONE = "NONE"
DIRACTIONS=[RIGHT,LEFT,DOWN,UP,NONE]
class GameWord:
    def __init__(self,size,speed):
        self.speed=speed
        self.top = tkinter.Tk()
        self.width=size
        self.height=size
        self.score=0
        self.scoreText="Score: " + str(self.score)
        self.w= tkinter.Canvas(self.top, bg="black", height=self.height, width=self.width)
        self.scoreLabel = self.w.create_text(40,10,fill="white",text=self.scoreText,tag="score")
        self.w.tag_raise("score")
        self.Food= False
        self.foodPosition=(0,0)
        self.snake=(self.width/2-self.width/2%20,self.height/2-self.height/2%20+20)
        self.diraction=0
        self.inGame=True
        self.begin=True
        self.flag=False
        self.tails=[]
        self.listDiraction=[LEFT,DOWN,LEFT,UP]

    def border(self):
        # make the vertical border
        for i in range(0,self.width):
            theBorder=i,0,i+15,15
            self.w.create_rectangle(theBorder,fill="purple",outline="purple",tag="border")
            theBorder=i,self.height-15,i+15,self.height
            self.w.create_rectangle(theBorder,fill="purple",outline="purple",tag="border")

        #  make the orizontal border
        for i in range(0,self.height):
            theBorder=0,i,15,i+15
            self.w.create_rectangle(theBorder,fill="purple",outline="purple",tag="border")
            theBorder=self.width-15,i,self.width,i+15
            self.w.create_rectangle(theBorder,fill="purple",outline="purple",tag="border")
        self.w.pack()
        self.w.tag_raise("score")


    def addFood(self):
        if self.Food ==False:
            time=0
            xsnake,ysnake=self.snake
            x,y=(xsnake,ysnake)
            flag=False
            # this while is to not have the same space as with a tail
            while True:
                # this while is to not have the same space with the head
                while True:
                    x=random.randint(20,self.width-22)
                    while x%20!=0:
                        x=random.randint(20,self.width-22)
                        time+=1
                        if (time>1000):
                            self.destroy()
                    y=random.randint(20,self.height-22)
                    while y%20!=0:
                        y=random.randint(20,self.height-22)
                    # end while
                    if (x,y)!=(xsnake,ysnake):
                       break
                # reset the flag to true
                flag=False
                for i in self.tails:
                    position,flag2=i
                    # see if there is a common space 
                    if position==(x,y):
                        flag=True
                        break
                # there is no tail 
                if self.tails==[]:
                    break
                # there is no common space
                if  not flag:
                    break       
            Position=x+1,y+1,x+19,y+19
            self.foodPosition=(x,y)
            self.w.create_rectangle(Position, fill="green", outline = 'green',tag="food")
            self.Food=True

    # spawn a Snake
    def spawnSnake(self):
        x,y=self.snake
        self.w.create_rectangle(x,y,x+20,y+20,fill="blue",outline="red",tag="snake")
        self.flag=False

    # check the Collisions
    def checkCollisions(self):
        x,y=self.snake
        # check if the snake is out of the border
        if x<20 or x>=self.width-20 or y<20 or y>=self.height-20:
            self.inGame=False
            return
        
        # check if the snake is over his tail
        theSnake=self.snake
        for i in range(len(self.tails)):
            position,flag=self.tails[i]
            if flag and position==theSnake:
                self.inGame=False
                return  
        
        # see if the snake has eaten the food
        if self.snake==self.foodPosition:
            # delete the previous one and add a new one
            self.w.delete("food")
            self.Food=False
            self.addFood()
            # add to the score and spawn a new tail 
            self.score+=1
            self.spawnTail()
            return
        self.flag=True

    # spawn a tail
    def spawnTail(self):
        # this function does not spawn the tail imediatly but
        # it adds to the snake the position that the snake
        # eat the food
        # so when the snake leaves that position
        # then it can die
        if(self.diraction!=0):
            self.tails.append((self.snake,False))
            self.flag=False

    def moveSnake(self):
        # move the snake
        def moveBody(x,y):
            flag2=True
            # check if there was a food eaten
            for i in range(len(self.tails)):
                position,flag=self.tails[i]
                sx,sy=position
                if not flag:
                    flag2=False
                    self.tails.pop(i)
                    # and tell that this tail can be dangerous
                    self.tails.append(((sx,sy),True))
                    # add a tail to the position  
                    self.w.create_rectangle(sx,sy,sx+20,sy+20,fill="blue",outline="White",tag="tail")
                    break

            sx,sy=self.snake
            # add a tail to the old head
            if self.tails!=[] and flag2 :
                self.w.create_rectangle(sx,sy,sx+20,sy+20,fill="blue",outline="White",tag="tail")
                self.tails.append(((sx,sy),True))
                tougther=self.w.find_withtag("tail")
                self.w.delete(tougther[0])
                self.tails.pop(0)

            # remove the head so it can be moved
            tougther=self.w.find_withtag("snake")
            self.w.delete(tougther[0])    
            # add the new head
            self.w.create_rectangle(sx+x,sy+y,sx+x+20,sy+y+20,fill="blue",outline="red",tag="snake")
            self.snake=(sx+x,sy+y)

        # if there are moves        
        if self.listDiraction!=[]:
            self.diraction=util.takeDiraction(self.listDiraction[0])
            self.listDiraction.pop(0)
            # add the new tail and haed
            x,y=self.diraction
            moveBody(x,y)

        
    def printScore(self):
        self.scoreText="Score: " + str(self.score)
        self.w.delete("score")
        self.w.create_text(50,10,fill="white",text=self.scoreText,tag="score")
        self.w.tag_raise("score")

    # add the outline of the end position of the snake
    def addWall(self,sx,sy):
        self.w.create_rectangle(sx,sy,sx+20,sy+20,outline="White",tag="wall")
    
    def change(self,sx,sy):
        self.w.create_rectangle(sx,sy,sx+20,sy+20,outline="red",tag="wall")
    
    # delete the outline of the end position of the snake
    def removeWall(self):
        tougther=self.w.find_withtag("wall")
        for i in range(len(tougther)):
            self.w.delete(tougther[i])         


    def getSnake(self):
        return self.snake
    
    def getFood(self):
        return self.foodPosition
    
    def getTail(self):
        tail=[]
        for i in self.tails:
            tail.append(i)
        return tail

    def play(self,diraction):
        self.listDiraction=diraction
        self.checkCollisions()
        self.printScore()
        if(self.listDiraction==[]):
            return 0
        if self.inGame:
            self.moveSnake()
            time.sleep(self.speed)
            self.top.update()
            return 1
        else:
            self.destroy()
            return -1        
    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width
    def update(self):
        self.top.update()
    def destroy(self):
        self.top.destroy()

class Problem:
    def __init__(self,food,head,tails,height,width,game):
        self.head=head
        self.tails=tails
        self.width=width
        self.height=height
        self.food=food
        self.game=game
        
    def isGoalState(self,state):
        x,y=state
        return x==y

    def getStartState(self):
        return ((self.head,self.food),self.tails)
    
    def heuristic(self,state):
        return util.manhattanDistance(state,self.food)

    def addFinalOutline(self,tail):
        for i in range (len(tail)):
            position,flag=tail[i]
            if flag:
                x,y=position
                self.game.addWall(x,y)
        self.game.update()
    
    def change(self,tail):
        for i in range (len(tail)):
            position,flag=tail[i]
            if flag:
                x,y=position
                self.game.change(x,y)
        self.game.update()

    def removeFinalOutline(self):
        self.game.removeWall()

    def getSuccessors(self,state,tail):
        # return the diractions

        successors = []
        # check all available moves
        for action in [RIGHT,LEFT,DOWN,UP]:
            position,goals=state
            x,y = position
            dx, dy = util.takeDiraction(action)
            nextx, nexty = int(x + dx), int(y + dy)
            nextTails=[]
            flag=False
            # see that it has not eaten a tail
            for i in range(len(tail)):
                position,flag2=tail[i]
                # see if that tail is dangerous or not
                if (nextx,nexty)==position and flag2!=False:
                    flag=True
                    break
            if flag:
                continue
            
            # check if it is not out of boundries
            if not(nextx<20 or nextx>=self.width-20 or nexty<20 or nexty>=self.height-20):
                newSnake=(nextx,nexty)
                for i in tail:
                    nextTails.append(i)
                
                # check if a food has been eaten recently
                for i in range(len(nextTails)):
                    position,flag=nextTails[i]
                    if flag==False:
                        x,y=position
                        # make it that it can be a danger
                        nextTails.pop(i)
                        nextTails.append((position,True))
                        break
                # remove the last tail
                if len(nextTails)!=0:
                    nextTails.pop(0)
                    nextTails.append((newSnake,True))

                q=((newSnake,self.food),nextTails)
                successors.append( ( q, action,1) )
        
        return successors

from searchAlgorithms import Graph, aStarSearch
class World:

    def __init__(self,search,speed,flag=False,which="n"):        
        
        # create the world
        game = GameWord(280,1/speed)
        game.border()
        game.addFood()
        game.spawnSnake()
        # this is for the searchs
        solution=-2
        theSolution=[]
        # time variable is to cheack if the
        # algorithm cannot find a solution
        times=0
        if flag:
            problem=Problem((20,20),(20,20),game.getTail(),game.getHeight(),game.getWidth(),game)
            graph=Graph(int((game.getHeight())),int((game.getWidth())),game,problem,heuristic)

        while(solution!=-1):

            if(solution==0):         
                # find a the path
                if flag:
                    if which=="n":
                        theSolution=graph.normCycle(game.getSnake())
                    else:
                        return 
                else:
                    problem=Problem(game.getFood(),game.getSnake(),game.getTail(),game.getHeight(),game.getWidth(),game)
                    if search!=aStarSearch:
                        theSolution=search(problem)
                    else:
                        theSolution=search(problem,heuristic)
            # there is no path so end the game
            if theSolution==[] and times!=0:
                time.sleep(0.2)
                game.destroy()
                return
            
            # move the game
            solution=game.play(theSolution)
            if(solution!=0):
                times=0
            else:
                times+=1

def heuristic(state,problem):
    x,y=state
    return problem.heuristic(x)