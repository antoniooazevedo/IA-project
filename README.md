# Sokobond

<div style="text-align: justify">

## Introduction
Sokobond is a game created by Alan Hazelden and Lee Shang Lun and "is an elegantly designed puzzle game about chemistry". The game is available on Steam and has been well received by players and critics alike. The game is a puzzle game where the player must move atoms to create molecules. The game is designed to teach players about chemistry and the mechanics of the game are based on real-world chemistry principles.

## Rules
In Sokobond, you control atoms on a grid with a clear objective: navigate them around and bond them with other atoms to create molecules. You have two main actions: moving in any of the four cardinal directions (up, down, left, right), or pushing nearby atoms in those same directions.

To form a molecule, simply move your atom/molecule to a spot adjacent to another atom with available bonding connections. Both atoms will then lose one bonding connection and combine. The game is completed when all atoms are merged into one molecule and all bonding connections are utilized.

## Relevant Links

- [Steam Page](https://store.steampowered.com/app/290260/Sokobond/)  
- [Different implementation in JavaScript](https://github.com/vpelss/Sokobond_JS)  
- AI UC books:

  - Stuart Russell, Peter Norvig; Artificial intelligence. ISBN: 978-0-13-207148-2
  - Richard S. Sutton; Reinforcement learning. ISBN: 978-0-262-03924-6
  - Stuart Russel, Peter Norvig; Artificial Intelligence: A modern Approach.

- [Pygame Documentation](https://www.pygame.org/docs/)

## Problem Formulation

### State Representation
Each state can be represented as the current configuration of atoms on the grid, including their positions and bonding connections.

### Initial State
The initial state is the configuration of the atoms on the grid at the start of the game, their bonding connections and which atom is the player controlling.

### Objective test
Each solution can be considered as a sequence of actions that lead to the final state where all atoms are merged into one molecule and all bonding connections are utilized.

### Operators
#### Move Operator
- **Name**: Move
- **Preconditions**: 
    - The controlled atom/molecule can only move to any of the four cardinal directions (up, down, left, right).
    - The controlled atom/molecule must be ajdacent to an empty cell in the direction of the move or an atom with no available bonding connections and an empty cell adjacent to it in the direction of the move.
- **Effect**:
    - The controlled atom/molecule moves to the new cell.
    - If the move results in the controlled atom/molecule being adjacent to another atom and the bonding limit of both atoms is not exceeded, a bond is formed.
    - If moved to a cell with another atom and there is no possible bonding connection, both the atom/molecule controlled and the atom in the cell will move to the next cell in the direction of the move - pushing the atom in the cell.
- **Cost**: The cost of this operator is 1.

## Algorithms and Heuristics

### Uninformed algorithms
- **Breadth-First Search (BFS)**: This algorithm is used to find the shortest sequence of moves that leads to the formation of the final molecule. BFS explores all the possible moves (states) at the current level before moving on to the next level. In the context of Sokobond, a "level" can be thought of as a move. So, BFS first considers all states that can be reached in one move, then all states that can be reached in two moves, and so on. The algorithm starts with the initial layout of atoms on the grid (the initial state). It then generates all possible layouts that can be reached by moving the controlled atom/molecule in any of the four cardinal directions (up, down, left, right). BFS continues this process, generating new states and adding them to a queue. It always removes and explores states from the front of the queue (i.e., the states that can be reached with the fewest moves). The algorithm stops when it finds a state where all atoms are merged into one molecule and all bonding connections are utilized. The sequence of moves that led to this state is the solution to the game. BFS is guaranteed to find the shortest solution if one exists, but it can be slow and memory-intensive if there are many possible states to explore.

- **Depth-First Search (DFS)**: This algorithm is used to explore the game's state space by going as deep as possible along each branch before backtracking. In the context of Sokobond, a "branch" can be thought of as a sequence of moves. So, DFS first considers one possible sequence of moves to its fullest extent (until it either reaches a solution or can't go any further), then it backtracks and explores the next sequence. The algorithm starts with the initial layout of atoms on the grid (the initial state). It then generates all possible layouts that can be reached by moving the controlled atom/molecule in any of the four cardinal directions (up, down, left, right). DFS continues this process, generating new states and adding them to a stack. It always removes and explores states from the top of the stack. The algorithm stops when it finds a state where all atoms are merged into one molecule and all bonding connections are utilized. The sequence of moves that led to this state is a solution to the game.

- **Iterative deepening search (IDS)**: This algorithm combines the advantages of Breadth-First Search (BFS) and Depth-First Search (DFS). It explores the game's state space by performing a DFS to a certain "depth limit", and it repeats this process with an increased depth limit until the goal state is found. In the context of Sokobond, a "depth" can be thought of as a sequence of moves. So, IDS first considers all states that can be reached in one move, then all states that can be reached in two moves, and so on, just like BFS. However, IDS uses memory more efficiently than BFS, because it only needs to store a single path from the root to the leaf at any one time, just like DFS. The algorithm starts with the initial layout of atoms on the grid (the initial state). It then generates all possible layouts that can be reached by moving the controlled atom/molecule in any of the four cardinal directions (up, down, left, right). IDS continues this process, generating new states and adding them to a stack. It always removes and explores states from the top of the stack (i.e., the states that can be reached with the most recent sequence of moves). The algorithm stops when it finds a state where all atoms are merged into one molecule and all bonding connections are utilized. The sequence of moves that led to this state is a solution to the game.


### Heuristics

- **Manhattan Distance**: The Manhattan distance heuristic calculates the sum of the distances between each atom and its nearest atom with available bonding connections. This heuristic estimates the number of moves required to bond all atoms together based on their relative positions on the grid. It assumes that moving atoms closer to each other will result in fewer moves needed to form bonds. The heuristic function calculates the Manhattan distance for each atom to its nearest atom with available bonding connections and returns the sum of these distances. 

- **Atoms with More Free Electrons**: This heuristic gives priority to bonding atoms that have more free electrons available for bonding. Free electrons are crucial for forming bonds between atoms, and atoms with more free electrons are more likely to bond successfully. The heuristic function calculates the number of free electrons for each atom and prioritizes bonding atoms with higher numbers of free electrons. This approach aims to maximize the efficiency of bonding by focusing on atoms that can contribute more to forming stable molecules.

- **Minimize Remaining Connections**: The minimize remaining connections heuristic prioritizes bonding atoms that have more available bonding connections. The idea behind this heuristic is to minimize the number of remaining connections on each atom, as atoms with fewer remaining connections are closer to forming a complete molecule. The heuristic function sorts atoms based on the number of remaining bonding connections and prioritizes bonding atoms with fewer connections first.

- **Final molecule constitution heuristic**: 

### Heuristic Algorithms

- **A\* Algorithm**: The A* algorithm is a strategic method for finding the shortest path to a goal. It starts by setting up a priority queue and designating the starting node as the current node. The algorithm then enters a cycle, where it checks if the current node is the goal node. If it is, the search concludes, and we have our path. If the current node isn't the goal, the algorithm generates all potential next nodes (children) from the current node. Each child is added to the priority queue with a priority value equal to the total cost f(n) = g(n) + h(n). Here, g(n) is the cost so far, or the number of moves we've already made, and h(n) is the heuristic cost, or an estimate of the number of moves still needed to reach the goal. The heuristic cost is calculated using the Manhattan distance, which is the number of grid cells we'd have to move in straight lines (no diagonals) to reach the nearest unbonded atom. The algorithm then selects the node with the lowest total cost from the priority queue and sets it as the current node. This process is repeated until the path is found.

- **A\* Prunning**: This algorithm is similar to the A* algorithm, but it prunes any child that doesn't lead to the goal node. This pruning step can help to speed up the search by reducing the number of nodes that need to be explored. It's particularly useful when the heuristic is not very accurate, as it can prevent the algorithm from wasting time exploring paths that are unlikely to lead to the goal. The pruning step is performed after generating the children of the current node. For each child, the algorithm checks if the Manhattan distance to the nearest unbonded atom is less than the Manhattan distance of the current node. If it is, the child is pruned, as it's unlikely to lead to the goal. This heuristic is used to compare the performance of the A* algorithm with and without pruning.

- **A\* minimize remaining connections**: The algorithm checks if the current node is the goal node. If it is, the search concludes, and we have our path. If the current node isn't the goal, the algorithm generates all potential next nodes (children) from the current node. Each child is added to the priority queue with a priority value equal to the total cost f(n) = g(n) + h(n). Here, g(n) is the cost so far, or the number of moves we've already made, and h(n) is the heuristic cost, or an estimate of the number of moves still needed to reach the goal. The heuristic cost is calculated by minimizing the remaining connections, which prioritizes bonding atoms that have more available bonding connections. The idea behind this heuristic is to minimize the number of remaining connections on each atom, as atoms with fewer remaining connections are closer to forming a complete molecule.

- **Greedy Search**: In the game, the Greedy Algorithm uses the heuristic that prefers atoms with more free electrons. It starts with atoms on a grid. Each atom's free electrons are counted, and atoms with more free electrons are prioritized. The algorithm generates all possible moves, then picks the one that bonds with the highest priority atom. The move is made, and the game state updates. If this move forms a bond without exceeding the bonding limit, the process continues. The goal is to merge all atoms into one molecule using all bonding connections. If the goal isn't reached, the process repeats.

## Implementation Work Already Carried Out

- **Game Engine**: The game engine is implemented using the Pygame library. The game engine is responsible for rendering the game, handling user input, and updating the game state. The game engine is implemented in the `sokobond.py` file.
- **Game Loop**: The game loop is implemented in the `sokobond.py` file. The game loop is responsible for running the game, controlling the FPS, updating the game state, and rendering the game.
- **Data Structures**: 
  - The `Atom` class is implemented in the `entities.py` file. The `Atom` class represents an atom in the game. It has attributes such as position and bonding connections. The `Atom` class also has methods to update the atom and bond with other atoms.
  - The `Game` class is implemented in the `game.py` file. The `Game` class represents the game state, and contains methods to update the game state and check for game over conditions. It also contains the initial state of the game.
- **Rendering**: The rendering of the game is implemented in the `sokobond.py` file. The game is rendered using the Pygame library. The game window is created, and the game state is rendered to the window. We also have already created the base_sprite for the atoms. 
- **User Input**: The user input is handled in the `sokobond.py` file. The game listens for user input and updates the game state accordingly. The user can control the atom/molecule using the arrow keys.
