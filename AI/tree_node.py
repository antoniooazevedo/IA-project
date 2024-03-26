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

    @staticmethod
    def breadth_first_search(initial_state):
        root = TreeNode(initial_state)
        queue = deque([root])
        visited = set([initial_state])

        while queue:
            node = queue.popleft()

            if (node.state.is_goal()):
                return node

            for state in node.state.child_states():
                if state not in visited:
                    child_node = TreeNode(state)
                    child_node.parent = node
                    queue.append(child_node)
                    visited.add(state)

        return None


    def print_solution(node):
        if node == None:
            print("No solution found")
        elif node.parent == None:
            node.state.printState()
        else:
            TreeNode.print_solution(node.parent)
            node.state.printState()
