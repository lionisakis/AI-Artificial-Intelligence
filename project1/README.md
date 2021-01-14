Author: Lionis Emmanouil Georgios (Akis)

### Summery of the program:
  This project creates a snake game. That game can be played either by the user or by the computer. The computer solves this problem by using Search Algorithms (BFS,DFS,UCS,A*). Those solutions cannot be perfect as the snake can trap itself. Language: Python
 
### How to compile the programm:
  The execution of the programm is easy. You just have to write `python main.py {searchAlgorithm} {speed}` or `python3 main.py {searchAlgorithm} {speed}`
  It depends on how you run a python script. The project is writen in ** Pytho3.9 ** version. The args that have been passed are the following:
  
  searchAlgorithm:
  
- *dfs* (Depth First Search)
- *bfs* (Breath Fisrt Search)
- *ucs* (Uniform Cost Search)
- *ass* (A Star Search, A*)
- *___*    (With no argument then the user plays the game. **NOTE: the speed argument has to be missing to work**
    
   speed:
   
- *number* (So the game goes according to that speed)
- *___* (If the argument is missing then it is set to 0.1) 
  
### Description of the main :
  The main takes the arguments and chooses if the game runs with the search algorithms or not.
  
### Search Algorithms:
  The search Algorithms run as following:
  
  There is a class World, which is being called by the main, that controls the game. At first, it create the panel with the boundaries. Then, it spawns the food and the snake. After, it calls the class Problem which converst the game to a state problem, which is being used in the search algorithms. Then, it calls the search algorithms. It gives the solution to the game and runs it.

  The class Problem has 3 functions: 
    getStartingState, which returns the startingState, 
    getSuccessors, which returns the states that are legal, 
    isGoal, that returns if that state is the final position that we want.
  
  The class GameWord has many functions. The important functions are the checkCollisions, which checks if that move is deadly and if it is, then it ends the game. There is also moveBody, which moves the snake. The snake first spawns the new head and tails and then it destroys the previous head and last tail. If the food is recently eaten, then it waits for one move and then it is spawned. It is spawned at the position of the food and it is added when the snake leaves that position.

### User Control
  The class GameWord is the same as the one in the search algotihms, with the exception that the moves are given from the user and not from the computer.
