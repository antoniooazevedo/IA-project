from collections import deque

class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.depth = 0
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

    def breadth_first_search(initial_state, goal_state_func, operators_func):
        root = TreeNode(initial_state)   # create the root node in the search tree
        queue = deque([root])   # initialize the queue to store the nodes
        visited = set()  # initialize the set to store visited states
        
        while queue:
            node = queue.popleft()   # get first element in the queue
            if goal_state_func(node.state):   # check goal state
                return node
            
            visited.add(node.state)  # mark the state as visited
            
            for state in operators_func(node.state):   # go through next states
                if state not in visited:  # if the state has not been visited yet
                    # create tree node with the new state
                    child_node = TreeNode(state)
                    child_node.parent = node
                    queue.append(child_node)  # append to the queue
                
        return None 
