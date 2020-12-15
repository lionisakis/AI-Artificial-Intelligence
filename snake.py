import tkinter
import random
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
            x1,y1=self.snake
            x=x1-20
            y=y1+20
            # while x%20!=0:
            #     x=random.randint(10,260)
            # y=1
            # while y%20!=0:
            #     y=random.randint(10,220)
            Position=x+1,y+1,x+19,y+19
            self.foodPosition=(x,y)
            self.w.create_rectangle(Position, fill="green", outline = 'green',tag="food")
            self.Food=True

    def spawnSnake(self):
        x,y=self.snake
        self.w.create_rectangle(x,y,x+20,y+20,fill="blue",outline="black",tag="snake")
        self.flag=False

    def checkCollisions(self):
        x,y=self.snake
        if x<=20 or x>=self.width-20 or y<=20 or y>=self.height-20:
            self.inGame=False
            return
        
        x=0
        theSnake=self.w.find_withtag("snake")[0]
        print(self.w.find_withtag("snake"))
        print(self.w.coords(theSnake))
        for i in self.w.find_withtag("snake"):
            if x==0:
                x=1
                continue
            print("x is",x)
            print(i,self.w.coords(i))
            print(i,theSnake)
            if self.w.coords(i)==self.w.coords(theSnake) and i!=theSnake and self.flag:
                self.inGame=False
                return
            x+=2
        print("DONE")
        if self.snake==self.foodPosition:
            x,y=self.foodPosition
            Position=x+1,y+1,x+19,y+19
            self.w.delete("food")
            self.Food=False
            self.addFood()
            self.score+=1
            self.spawnSnake()
            return
        self.flag=True

    def moveSnake(self):
        
        def moveBody(x,y):
            sx,sy=self.snake
            self.w.create_rectangle(sx+x,sy+y,sx+x+20,sy+y+20,fill="blue",outline="black",tag="snake")
            self.snake=(sx+x,sy+y)
            

        def up_keypress(event):
            if(self.diraction!=1):
                self.diraction=0

        def down_keypress(event):
            if(self.diraction!=0):
                self.diraction=1


        def right_keypress(event):
            if(self.diraction!=3):
                self.diraction=2


        def left_keypress(event):
            if(self.diraction!=2):
                self.diraction=3

        def deletePrevious():
            tougther=self.w.find_withtag("snake")
            first=tougther[0]
            self.w.delete(first)
            

        self.top.bind("<Left>", left_keypress)
        self.top.bind("<Down>", down_keypress)
        self.top.bind("<Right>", right_keypress)
        self.top.bind("<Up>", up_keypress)

        deletePrevious()

        if self.diraction==0:
            moveBody(0,-20)
        elif self.diraction==1:
            moveBody(0,+20)
        elif self.diraction==2:
            moveBody(+20,0)
        elif self.diraction==3:
            moveBody(-20,0)

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
            self.top.after(100, self.play)
        else:
            self.top.destroy()
        
    def loop(self):
        self.top.mainloop()
    

game = GameWord()
game.border()
game.addFood()
game.spawnSnake()
game.play()
game.loop()