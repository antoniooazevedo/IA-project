from AI.sokobond_state import Sokobond_State

from collections import deque


class TreeNode:
    """
    Class that represents a node in a tree for search algorithms.
    """

    def __init__(self, state, move=None, parent=None):
        """
        Initializes a TreeNode object.

        Args:
            state (Sokobond_State): The state of the Sokobond game.
            move (str): The move that led to this state.
            parent (TreeNode): The parent node of this node.
        """
        self.state = state
        self.move = move
        self.parent = parent
        self.children = []
        self.depth = 0

    def add_child(self, child_node, move):
        """
        Adds a child node to this node.

        Args:
            child_node (TreeNode): The child node to be added.
            move (str): The move that leads to the child node.
        """
        self.children.append(child_node)
        child_node.parent = self
        child_node.move = move


class Search:
    """
    Class that contains various search algorithms.
    """

    def breadth_first_search(initial_state):
        """
        Performs a breadth-first search on the initial state.

        Args:
            initial_state (Sokobond_State): The initial state of the Sokobond game.

        Returns:
            TreeNode: The node containing the goal state, if found. None otherwise.
        """
        root = TreeNode(initial_state)
        queue = deque([root])
        visited = set()

        while queue:
            node = queue.popleft()

            if node.state.is_goal():
                return node

            if node.state in visited:
                continue

            for move, state in node.state.child_states():
                child_node = TreeNode(state)
                node.add_child(child_node, move)
                queue.append(child_node)
            
            visited.add(node.state)

        return None

    def depth_first_search(initial_state):
        """
        Performs a depth-first search on the initial state.

        Args:
            initial_state (Sokobond_State): The initial state of the Sokobond game.

        Returns:
            TreeNode: The node containing the goal state, if found. None otherwise.
        """
        root = TreeNode(initial_state)
        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()

            if node.state in visited:
                continue

            if node.state.is_goal():
                return node

            for move, state in node.state.child_states():
                child_node = TreeNode(state)
                node.add_child(child_node, move)
                stack.append(child_node)

            visited.add(node.state)

        return None

    def depth_limited_search(initial_state, depth_limit):
        """
        Performs a depth-limited search on the initial state.

        Args:
            initial_state (Sokobond_State): The initial state of the Sokobond game.
            depth_limit (int): The maximum depth to search.

        Returns:
            TreeNode: The node containing the goal state, if found. None otherwise.
        """

        root = TreeNode(initial_state)
        root.depth = 0
        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()

            if node.state.is_goal():
                return node

            test_depth = 0
            if node.depth != 0:
                test_depth = node.parent.depth + 1 

            isVisitedWithLowerDepth = False
            for d in range(0, test_depth):
                if (node.state, d) in visited:
                    isVisitedWithLowerDepth = True
                    break
                
            if isVisitedWithLowerDepth:
                continue

            node.depth = test_depth

            visited.add((node.state, node.depth))

            if node.depth == depth_limit:
                continue

            for move, state in node.state.child_states():
                child_node = TreeNode(state)
                child_node.depth = node.depth + 1
                node.add_child(child_node, move)
                stack.append(child_node)

        return None

    def iterative_deepening_search(initial_state, depth_limit):
        """
        Performs an iterative deepening search on the initial state.

        Args:
            initial_state (Sokobond_State): The initial state of the Sokobond game.
            depth_limit (int): The maximum depth to search.
        
        Returns:
            TreeNode: The node containing the goal state, if found. None otherwise.
        """
        
        for local_limit in range(depth_limit + 1):
            result = Search.depth_limited_search(initial_state, local_limit)
            if result is not None:
                return result
        return None

    def greedy_search(initial_state, heuristic):
        """
        Performs a greedy search on the initial state, by
        prioritizing the states with the highest heuristic value.

        Args:
            initial_state (Sokobond_State): The initial state of the Sokobond game.
            heuristic (function): The heuristic function to evaluate the states.

        Returns:
            TreeNode: The node containing the goal state, if found. None otherwise.
        """

        root = TreeNode(initial_state)
        root.depth = 0
        queue = deque([(root, heuristic(root.state))])
        visited = set()

        while queue:
            (node, _) = queue.popleft()

            if node.state.is_goal():
                return node

            if node.state in visited:
                continue

            for move, state in node.state.child_states():
                local_cost = heuristic(state)
                child_node = TreeNode(state)
                child_node.depth = node.depth + 1
                node.add_child(child_node, move)
                queue.append((child_node, local_cost))

            queue = deque(sorted(queue, key=lambda x: x[1], reverse=True))

            visited.add(node.state)

        return None

    def a_star_search(initial_state, heuristic):
        """
        Performs an A* search on the initial state, by
        prioritizing the states with the highest heuristic value and lowest depth.

        Args:
            initial_state (Sokobond_State): The initial state of the Sokobond game.
            heuristic (function): The heuristic function to evaluate the states.

        Returns:
            TreeNode: The node containing the goal state, if found. None otherwise.
        """
        root = TreeNode(initial_state)
        root.depth = 0
        queue = deque([(root, heuristic(root.state))])
        visited = set()

        while queue:
            queue = deque(sorted(queue, key=lambda x: x[1], reverse=True))
            (node, val) = queue.popleft()

            if node.state.is_goal():
                return node

            if node.state in visited:
                continue

            for move, state in node.state.child_states():
                child_node = TreeNode(state)
                child_node.depth = node.depth + 1
                node.add_child(child_node, move)
                local_value = heuristic(state) - child_node.depth
                queue.append((child_node, local_value))

            queue = deque(sorted(queue, key=lambda x: x[1], reverse=True))

            visited.add(node.state)

        return None

    def print_solution(node):
        """
        Prints the states that lead to the goal state.

        Args:
            node (TreeNode): The node containing the goal state.
        """
        if node == None:
            print("No solution found")
        elif node.parent == None:
            node.state.printState()
        else:
            Search.print_solution(node.parent)
            node.state.printState()

    def get_solution_moves(node):
        """
        Returns the moves that lead to the goal state.

        Args:
            node (TreeNode): The node containing the goal state.

        Returns:
            list: A list of moves that lead to the goal state.
        """
        moves = []
        while node.parent != None:
            moves.append(node.move)
            node = node.parent
        moves.reverse()
        return moves


class Heuristic:
    """
    Class that contains various heuristic functions.
    """
    def prioritize_free_electrons(state):
        """
        This heuristic prioritizes bonding by connecting the player molecule to atoms with more free electrons.

        Args:
            state (Sokobond_State): The state of the Sokobond game.

        Returns:
            int: The heuristic value.
        """
        value = 0

        if state.is_goal():
            return 1000

        player = state.level.get_player_molecule()

        for a in player.get_atoms():
            value += a.get_electrons()

        if value == 0:
            return -1000

        return value

    def manhattan_distance(state):
        """
        This heuristic prioritizes states where the controlled molecule is nearer to a potential bonding atom. 

        Args:
            state (Sokobond_State): The state of the Sokobond game.

        Returns:
            int: The heuristic value.
        """
        value = 30

        if state.is_goal():
            return 1000

        molecules = state.level.molecules
        player = state.level.get_player_molecule()
        electrons = 0

        for p in player.get_atoms():
            electrons += p.get_electrons()

        if electrons == 0:
            return -1000

        atoms = []

        for m in molecules:
            atoms.extend(m.get_atoms())

        min_distance = 1000
        for a in atoms:
            for p in player.get_atoms():
                min_distance = min(
                    min_distance,
                    abs(a.get_position()[0] - p.get_position()[0])
                    + abs(a.get_position()[1] - p.get_position()[1]),
                )

        value -= min_distance

        return value

    def minimize_free_electrons(state):
        """
        This heuristic evaluates the number of free electrons and favors states with fewer free electrons.         
        
        Args:
            state (Sokobond_State): The state of the Sokobond game.

        Returns:
            int: The heuristic value.
        """
        value = 10

        if state.is_goal():
            return 1000

        player = state.level.get_player_molecule()

        for a in player.get_atoms():
            value -= a.get_electrons()

        if value == 10:
            return -1000

        return value
