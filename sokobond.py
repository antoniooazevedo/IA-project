import pygame as pg
from MVC.Model.menu_model import Menu_Model
from MVC.View.menu_view import Menu_View
from MVC.Controller.Menus.main_menu_controller import Main_Menu_Controller
from MVC.Model.level_model import Level_Model
from MVC.View.level_view import Level_View
from MVC.Controller.level_controller import Level_Controller
from AI.sokobond_state import Sokobond_State
from AI.tree_node import Search, Heuristic
import utils as utils
import time

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

        #main_menu_model = Menu_Model(["Play", "Choose AI", "Quit"], "SOKOBOND", 50)
        #main_menu_view = Menu_View(self.screen, main_menu_model, 1)
        #main_menu_controller = Main_Menu_Controller(main_menu_model, self.screen)

        self.level_model = Level_Model(self.levelName)
        self.level_controller = Level_Controller(self.level_model) 
        state = Sokobond_State(self.level_model)
        start_time = time.time()
        goal = self.create_AI(state)
        end_time = time.time()

        execution_time = end_time - start_time

        return execution_time
    
        #while (not self.level_model.won):
        #    
        #    self.level_controller.handle_events()
        #    
        #    self.clock.tick(self.fps)
        #    
        #    self.level_controller.check_win()

    def create_AI(self, state):
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

        self.moves = Search.get_solution_moves(goal)     

        return goal   
    

algorithms = ["A* - Manhattan Distance", "A* - Free Electrons"]
levels = ["lvl1.txt", "lvl2.txt", "lvl3.txt", "lvl6.txt", "lvl7.txt", "lvl8.txt"]


for algorithm in algorithms:
    for level in levels:
        game = Game(algorithm, level)
        execution_time = game.run()
        print(f"Algorithm: {algorithm}, Level: {level}, Execution time: {execution_time}")