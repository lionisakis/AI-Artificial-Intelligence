import tkinter
import random

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
        self.diraction=RIGHT
        self.inGame=True
        self.begin=True
        self.flag=False
        self.tails=[]

    def border(self):
        # make the vertical border
        for i in range(0,self.width):
            theBorder=i,0,i+19,17
            self.w.create_rectangle(theBorder,fill="purple",outline="purple",tag="border")
            theBorder=i,self.height-20,i+19,self.height
            self.w.create_rectangle(theBorder,fill="purple",outline="purple",tag="border")

        #  make the orizontal border
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
        
        # convert the positions
        def directionToVector(action):
            if action==UP:
                return(0,-20)
            elif action==DOWN:
                return(0,+20)
            elif action==RIGHT:
                return(+20,0)
            elif action==LEFT:
                return(-20,0)

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

        def up_keypress(event):
            if(self.diraction!=DOWN):
                self.diraction=UP


        def down_keypress(event):
            if(self.diraction!=UP):
                self.diraction=DOWN


        def right_keypress(event):
            if(self.diraction!=LEFT):
                self.diraction=RIGHT


        def left_keypress(event):
            if(self.diraction!=RIGHT):
                self.diraction=LEFT
        
        self.top.bind("<Left>", left_keypress)
        self.top.bind("<Down>", down_keypress)
        self.top.bind("<Right>", right_keypress)
        self.top.bind("<Up>", up_keypress)
        # if there are moves        
        if self.diraction!=NONE:
            # add the new tail and haed
            x,y=directionToVector(self.diraction)
            moveBody(x,y)

        
    def printScore(self):
        self.scoreText="Score: " + str(self.score)
        self.w.delete("score")
        self.w.create_text(50,10,fill="white",text=self.scoreText,tag="score")
        self.w.tag_raise("score")


    def play(self):
        self.checkCollisions()
        self.printScore()
        
        if self.inGame:
            self.moveSnake()
            self.top.after(150, self.play)
        else:
            self.top.destroy()
        
    def loop(self):
        self.top.mainloop()