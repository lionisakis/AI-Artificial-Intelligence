from autoSnake import World,heuristic
from snake import GameWord
import sys
from searchAlgorithms import depthFirstSearch,breadthFirstSearch,uniformCostSearch
from searchAlgorithms import aStarSearch


if len(sys.argv)!=1:
    string=str(sys.argv[1])
    speed=0.1
    if len(sys.argv)!=2:
        speed=int(sys.argv[2])
    if string=="dfs":
        World(depthFirstSearch,speed)
    elif string=="bfs":
        World(breadthFirstSearch,speed)
    elif string=="ucs":
        World(uniformCostSearch,speed)
    elif string=="ass":
        World(aStarSearch,speed,heuristic)
    elif string=="nhc":
        World(aStarSearch,speed,heuristic,True)
        
else:
    game = GameWord(300)
    game.border()
    game.addFood()
    game.spawnSnake()
    game.play()
    game.loop()