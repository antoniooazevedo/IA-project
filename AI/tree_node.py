from AI.sokobond_state import Sokobond_State

from collections import deque
import heapq

class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        self.depth = 0
    
    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

class Search:

    def breadth_first_search(initial_state):
        root = TreeNode(initial_state)
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if (node.state.is_goal()):
                return node

            for state in node.state.child_states():
                    child_node = TreeNode(state)
                    node.add_child(child_node)
                    queue.append(child_node)

        return None

    def depth_first_search(initial_state):
        root = TreeNode(initial_state)
        stack = [root]
        visited = set()

        while stack:
            node = stack.pop()

            if node.state in visited:
                continue

            if (node.state.is_goal()):
                return node


            for state in node.state.child_states():
                child_node = TreeNode(state)
                node.add_child(child_node)
                stack.append(child_node)

            visited.add(node.state)

        return None

    def depth_limited_search(initial_state, depth_limit):
        root = TreeNode(initial_state)
        stack = [(root, 0)]
        count = 0

        while stack:
            (node, depth) = stack.pop()
            count += 1

            if (node.state.is_goal()):
                print("Nodes visited: ", count)
                return node

            if depth == depth_limit:
                continue
            
            for state in node.state.child_states():
                child_node = TreeNode(state)
                node.add_child(child_node)
                stack.append((child_node, depth + 1))

        print("Nodes visited: ", count)
        return None

    def iterative_deepening_search(initial_state, depth_limit):
        for local_limit in range(depth_limit+1):
            print("Searching depth limit: ", local_limit)
            result = Search.depth_limited_search(initial_state, local_limit)
            if result is not None:
                return result
            print("No solution found at depth limit")
        return None

    def greedy_search(initial_state, cost_function):
        root = TreeNode(initial_state)
        queue = deque([(root, cost_function(root.state))])
        visited = set()

        while queue:
            (node, cost) = queue.popleft()

            if node.state in visited:
                continue

            if (node.state.is_goal()):
                return node

            for state in node.state.child_states():
                local_cost = cost_function(state)
                child_node = TreeNode(state)
                node.add_child(child_node)
                queue.append((child_node, local_cost))

            visited.add(node.state)
            queue = deque(sorted(queue, key=lambda x: x[1]))

        return None
    
    def a_star_search(initial_state, heuristic, cost_function):
        root = TreeNode(initial_state)
        queue = deque([root])
        visited = set()

        while queue:
            queue = deque(sorted(queue, key=lambda x: heuristic(x.state) + cost_function(x.state)))
            (node,_) = queue.popleft()

            if node.state in visited:
                continue

            if (node.state.is_goal()):
                return node

            for state in node.state.child_states():
                child_node = TreeNode(state)
                node.add_child(child_node)
                queue.append(child_node)

        return None

    def print_solution(node):
        if node == None:
            print("No solution found")
        elif node.parent == None:
            node.state.printState()
        else:
            Search.print_solution(node.parent)
            node.state.printState()


class Heuristic:
    def prioritize_free_electrons(state):
        n_molecules = len(state.level.molecules)
        n_electrons = 0
        for m in state.level.molecules:
            for a,c in m.molecule.items():
                n_electrons = n_electrons + a.electrons

        return n_electrons * n_molecules #quanto menor, melhor (por causa do sort)
    
    
