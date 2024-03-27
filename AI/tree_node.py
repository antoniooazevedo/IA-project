from AI.sokobond_state import Sokobond_State

from collections import deque

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
        visited = set()

        while queue:
            node = queue.popleft()

            if node.state in visited:
                continue

            if (node.state.is_goal()):
                return node

            for state in node.state.child_states():
                    child_node = TreeNode(state)
                    node.add_child(child_node)
                    queue.append(child_node)

            visited.add(node.state)

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
        visited = set()

        while stack:
            (node, depth) = stack.pop()

            if depth > depth_limit:
                continue

            was_added = False
            if node.state not in visited:
                visited.add(node.state)
                was_added = True

            if node.state.is_goal():
                return node

            if depth < depth_limit:  # Only generate child nodes if below depth limit
                for state in node.state.child_states():
                    child_node = TreeNode(state)
                    node.add_child(child_node)
                    stack.append((child_node, depth + 1))

            if was_added:
                visited.remove(node.state)

        return None

    def iterative_deepening_search(initial_state, depth_limit):
        for local_limit in range(depth_limit+1):
            result = Search.depth_limited_search(initial_state, local_limit)
            print(result)
            if result is not None:
                return result
        return None

    def print_solution(node):
        if node == None:
            print("No solution found")
        elif node.parent == None:
            node.state.printState()
        else:
            Search.print_solution(node.parent)
            node.state.printState()
