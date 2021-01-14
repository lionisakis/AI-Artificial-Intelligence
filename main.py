from autoSnake import World,heuristic
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
    elif string=="ucs":
        World(uniformCostSearch)
    elif string=="ass":
        World(aStarSearch,heuristic)
else:
    print(1)
    game = GameWord()
    game.border()
    game.addFood()
    game.spawnSnake()
    game.play()
    game.loop()