import pygame as pg
from MVC.Model.menu_model import Menu_Model
from MVC.View.menu_view import Menu_View
from MVC.Controller.Menus.main_menu_controller import Main_Menu_Controller
from MVC.Model.level_model import Level_Model
from MVC.View.level_view import Level_View
from MVC.Controller.level_controller import Level_Controller
from AI.sokobond_state import Sokobond_State
from AI.tree_node import Search, Heuristic, TreeNode
import utils as utils
import time
import pandas as pd
from memory_profiler import memory_usage



# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)


class Game:

    def __init__(self, ai_type, level_name):
        pg.init()

        self.ai_type = ai_type
        self.levelName = level_name

        pg.display.set_caption("Sokobond")
        self.screen = pg.display.set_mode(WINDOW_SIZE)

        self.clock = pg.time.Clock()
        self.fps = 60

    def run(self):
        self.level_model = Level_Model(self.levelName)
        self.level_controller = Level_Controller(self.level_model) 
        state = Sokobond_State(self.level_model)
        start_time = time.time()
        goal = self.create_AI(state)
        end_time = time.time()
        node_count = TreeNode.node_count


        execution_time, goal_depth = end_time - start_time, goal.depth

        data = pd.DataFrame({
            'Algorithm': [self.ai_type],
            'Execution time': [execution_time],
            'Nodes created': [node_count],
            'Depth': [goal_depth]
        })

        return data, execution_time, node_count, goal_depth
    
        #while (not self.level_model.won):
        #    
        #    self.level_controller.handle_events()
        #    
        #    self.clock.tick(self.fps)
        #    
        #    self.level_controller.check_win()

    def create_AI(self, state):
        TreeNode.node_count = 0
        goal = None
        if self.ai_type == "BFS":
            goal = Search.breadth_first_search(state)
        elif self.ai_type == "DFS":
            goal = Search.depth_first_search(state)
        elif self.ai_type == "Depth Limited":
            goal = Search.depth_limited_search(state, 25)
        elif self.ai_type == "Iterative Deepening":
            goal = Search.iterative_deepening_search(state, 24)
        elif self.ai_type == "Greedy - Manhattan Distance":
            goal = Search.greedy_search(state, Heuristic.manhattan_distance)
        elif self.ai_type == "Greedy - Free Electrons":
            goal = Search.greedy_search(state, Heuristic.prioritize_free_electrons)
        elif self.ai_type == "Greedy - Minimize Free Electrons":
            goal = Search.greedy_search(state, Heuristic.minimize_free_electrons)
        elif self.ai_type == "A* - Manhattan Distance":
            goal = Search.a_star_search(state, Heuristic.manhattan_distance)
        elif self.ai_type == "A* - Free Electrons":
            goal = Search.a_star_search(state, Heuristic.prioritize_free_electrons)
        elif self.ai_type == "A* - Minimize Free Electrons":
            goal = Search.a_star_search(state, Heuristic.minimize_free_electrons)

        if goal == None:
            return
        return goal



algorithms = ["BFS", "DFS","Depth Limited", "Iterative Deepening", "Greedy - Manhattan Distance",
               "Greedy - Free Electrons", "Greedy - Minimize Free Electrons", "A* - Manhattan Distance",
               "A* - Free Electrons", "A* - Minimize Free Electrons"]

levels = ["lvl1.txt", "lvl2.txt", "lvl3.txt", "lvl6.txt", "lvl7.txt", "lvl8.txt", "lvl4.txt", "lvl5.txt"]
results = {}

for level in levels:
    for algorithm in algorithms:
        if level not in results:
            results[level] = []
        if (algorithm in ["Iterative Deepening", "Depth Limited"] and level not in ["lvl1.txt", "lvl2.txt"]) or ((algorithm == "DFS" or algorithm == "Greedy - Free Electrons" or algorithm == "Greedy - Minimize Free Electrons") and level == "lvl5.txt"):
            results[level].append(None)
            continue
        game = Game(algorithm, level)
        data, execution_time, node_count, depth = game.run()
        print(f"Algorithm: {algorithm}, Level: {level}, Execution time: {execution_time}, Nodes: {node_count} nodes, Depth: {depth}")
        if level not in results:
            results[level] = []
        results[level].append(data)

# Write the results to an Excel file
file_path = "sokobond_results.xlsx"
with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
    for level, dataframes in results.items():
        pd.concat(dataframes).to_excel(writer, sheet_name=f'level{level}', index=False)