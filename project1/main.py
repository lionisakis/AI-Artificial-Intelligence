from autoSnake import World
from snake import GameWord
import sys
from searchAlgorithms import depthFirstSearch,breadthFirstSearch,uniformCostSearch
from searchAlgorithms import aStarSearch


if len(sys.argv)!=1:
    string=str(sys.argv[1])
    speed=5
    if len(sys.argv)!=2:
        speed=float(sys.argv[2])
    if string=="dfs":
        World(depthFirstSearch,speed)
    elif string=="bfs":
        World(breadthFirstSearch,speed)
    elif string=="ucs":
        World(uniformCostSearch,speed)
    elif string=="ass":
        World(aStarSearch,speed)
    elif string=="nhc":
        World(aStarSearch,speed,True,"n")
        
else:
    game = GameWord(300)
    game.border()
    game.addFood()
    game.spawnSnake()
    game.play()
    game.loop()