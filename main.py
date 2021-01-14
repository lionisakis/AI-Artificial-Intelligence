from autoSnake import World
from snake import GameWord
import sys
from searchAlgorithms import depthFirstSearch
from searchAlgorithms import breadthFirstSearch
from searchAlgorithms import uniformCostSearch
from searchAlgorithms import aStarSearch


if len(sys.argv)!=1:
    string=str(sys.argv[1])
    if string=="dfs":
        World(depthFirstSearch)
    elif string=="bfs":
        World(breadthFirstSearch)
    elif string=="uCS":
        World(uniformCostSearch)
    elif string=="aSS":
        World(aStarSearch)
else:
    game = GameWord()
    game.border()
    game.addFood()
    game.spawnSnake()
    game.play()
    game.loop()