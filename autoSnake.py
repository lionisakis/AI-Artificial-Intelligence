import tkinter
import random
import time

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
            x,y=self.snake
            x=random.randint(20,self.width-20)
            while x%20!=0:
                x=random.randint(10,260)
            y=random.randint(20,self.height-20)
            while y%20!=0:
                y=random.randint(10,220)
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
        
        theSnake=self.w.find_withtag("snake")[0]
        for i in self.w.find_withtag("tail"):
            if x==0:
                x=1
                continue
            if self.w.coords(i)==self.w.coords(theSnake) and i!=theSnake and self.flag:
                self.inGame=False
                return
            x+=2
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
        x,y=self.snake
        self.w.create_rectangle(x,y,x+20,y+20,fill="blue",outline="black",tag="tail")
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
                self.tails.append((sx,sy))
            self.w.create_rectangle(sx+x,sy+y,sx+x+20,sy+y+20,fill="blue",outline="red",tag="snake")
            self.snake=(sx+x,sy+y)


        def deletePrevious():
            tougther=self.w.find_withtag("snake")
            self.w.delete(tougther[0])
            tougther=self.w.find_withtag("tail")
            if(tougther!=()):
                self.w.delete(tougther[0])
                if self.tails!=[]:
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
        return self.tails

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
            self.top.destroy()
            return -1        
    def getHeight(self):
        return self.height
    def getWidth(self):
        return self.width
    def update(self):
        self.top.update()
class Problem:
    def __init__(self,food,head,tails,height,width):
        self.head=head
        self.tails=tails
        self.width=width
        self.height=height
        self.food=food
        
    def isGoalState(self,state):
        x,y=state
        return x==y

    def getStartState(self):
        return (self.head,self.food)
    
    def getSuccessors(self,state):
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
            nextTails=[]
            flag=False
            for xTails,yTails in self.tails:
                if nextx==int(xTails+dx) and nexty==int(yTails+dy):
                    flag=True
                else:
                    nextTails.append((int(xTails+dx),int(yTails+dy)))
            if flag:
                continue
            if not(nextx<20 or nextx>=self.width-20 or nexty<20 or nexty>=self.height-20):
                newSnake=(nextx,nexty)
                q=(newSnake,self.food)
                successors.append( ( q, action,1) )
        return successors
class World:
    def __init__(self,search):        
        game = GameWord()
        game.border()
        game.addFood()
        game.spawnSnake()
        solution=-2
        theSolution=[]
        while(solution!=-1):
            if(solution==0):         
                problem=Problem(game.getFood(),game.getSnake(),game.getTail(),game.getHeight(),game.getWidth())
                theSolution=search(problem)
            
            solution=game.play(theSolution)
            if(solution==0):
                game.update()


