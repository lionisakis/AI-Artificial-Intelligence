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
    def __init__(self):
        self.top = tkinter.Tk()
        self.width=300
        self.height=300
        self.score=0
        self.scoreText="Score: " + str(self.score)
        self.w= tkinter.Canvas(self.top, bg="black", height=self.height, width=self.width)
        self.scoreLabel = self.w.create_text(50,10,fill="white",text=self.scoreText,tag="score")
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
        for i in range(0,self.width):
            theBorder=i,0,i+19,17
            self.w.create_rectangle(theBorder,fill="purple",outline="purple",tag="border")
            theBorder=i,self.height-20,i+19,self.height
            self.w.create_rectangle(theBorder,fill="purple",outline="purple",tag="border")
    
        for i in range(-3,self.height):
            theBorder=0,i,19,i+19
            self.w.create_rectangle(theBorder,fill="purple",outline="purple",tag="border")
            theBorder=self.width-20,i+280,self.width,i+19
            self.w.create_rectangle(theBorder,fill="purple",outline="purple",tag="border")
        self.w.pack()
        self.w.tag_raise("score")


    def addFood(self):
        if self.Food ==False:
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

    def spawnSnake(self):
        x,y=self.snake
        self.w.create_rectangle(x,y,x+20,y+20,fill="blue",outline="red",tag="snake")
        self.flag=False

    def checkCollisions(self):
        x,y=self.snake
        if x<20 or x>=self.width-20 or y<20 or y>=self.height-20:
            self.inGame=False
            return
        
        theSnake=self.snake
        for i in range(len(self.tails)):
            position,flag=self.tails[i]
            if flag and position==theSnake:
                self.inGame=False
                return  
        if self.snake==self.foodPosition:
            x,y=self.foodPosition
            Position=x+1,y+1,x+19,y+19
            self.w.delete("food")
            self.Food=False
            self.addFood()
            self.score+=1
            self.spawnTail()
            return
        self.flag=True

    def spawnTail(self):
        if(self.diraction!=0):
            self.tails.append((self.snake,False))
            self.flag=False

    def moveSnake(self):

        def directionToVector(action):
            if action==UP:
                return(0,-20)
            elif action==DOWN:
                return(0,+20)
            elif action==RIGHT:
                return(+20,0)
            elif action==LEFT:
                return(-20,0)

        def moveBody(x,y,flag):
            sx,sy=self.snake
            if(flag):
                self.w.create_rectangle(sx,sy,sx+20,sy+20,fill="blue",outline="black",tag="tail")
                self.tails.append(((sx,sy),True))
            self.w.create_rectangle(sx+x,sy+y,sx+x+20,sy+y+20,fill="blue",outline="red",tag="snake")
            self.snake=(sx+x,sy+y)
            for i in range(len(self.tails)):
                position,flag=self.tails[i]
                if flag==False:
                    x,y=position
                    self.w.create_rectangle(x,y,x+20,y+20,fill="blue",outline="black",tag="tail")
                    self.tails.pop(i)
                    self.tails.append((position,True))
                    break


        def deletePrevious():
            tougther=self.w.find_withtag("snake")
            self.w.delete(tougther[0])         
            
            tougther=self.w.find_withtag("tail")
            if(tougther!=()):
                self.w.delete(tougther[0])
                self.tails.pop(0)
                return True
            return False

        
        if self.listDiraction!=[]:
            self.diraction=directionToVector(self.listDiraction[0])
            self.listDiraction.pop(0)
            flag=deletePrevious()
            x,y=self.diraction
            moveBody(x,y,flag)

        
    def printScore(self):
        self.scoreText="Score: " + str(self.score)
        self.w.delete("score")
        self.w.create_text(50,10,fill="white",text=self.scoreText,tag="score")
        self.w.tag_raise("score")

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
            time.sleep(0.1)
            self.top.update()
            return 1
        else:
            print("ERROR",self.snake,self.tails)
            self.top.destroy()
            return -1        
    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width
    def update(self):
        self.top.update()
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

    def getSuccessors(self,state,tail):
        def directionToVector(action):
            if action==UP:
                return(0,-20)
            elif action==DOWN:
                return(0,+20)
            elif action==RIGHT:
                return(+20,0)
            elif action==LEFT:
                return(-20,0)
        successors = []
        for action in [RIGHT,LEFT,DOWN,UP]:
            position,goals=state
            x,y = position
            dx, dy = directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            flag=False
            for i in range(len(tail)):
                position,flag2=tail[i]
                if (nextx,nexty)==position and flag2!=False:
                    flag=True
                    break
            if flag:
                continue
            if not(nextx<20 or nextx>=self.width-20 or nexty<20 or nexty>=self.height-20):
                newSnake=(nextx,nexty)
                nextTails=tail
                if len(nextTails)!=0:
                    nextTails.pop(0)
                    nextTails.append(((x,y),True))
                print(newSnake,nextTails)
                q=((newSnake,self.food),nextTails)
                successors.append( ( q, action,1) )
        return successors
class World:

    def __init__(self,search,heuristic=None):        
        game = GameWord()
        game.border()
        game.addFood()
        game.spawnSnake()
        solution=-2
        theSolution=[]
        while(solution!=-1):
            if(solution==0):         
                problem=Problem(game.getFood(),game.getSnake(),game.getTail(),game.getHeight(),game.getWidth(),game)
                if heuristic==None:
                    theSolution=search(problem)
                else:
                    theSolution=search(problem,heuristic)
            solution=game.play(theSolution)
            if(solution==0):
                game.update()


def heuristic(state,problem):
    x,y=state
    return problem.heuristic(x)