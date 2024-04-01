import pygame as pg
import sys

from MVC.Model.level_model import Level_Model
from MVC.View.level_view import Level_View
from MVC.Controller.level_controller import Level_Controller
from MVC.Model.menu_model import Menu_Model
from AI.sokobond_state import Sokobond_State
from AI.tree_node import Search, Heuristic


class Level_Menu_Controller:
    """
    Class that represents the controller of the level menu in the MVC pattern.
    """
    def __init__(self, menu_model: Menu_Model, screen, ai_type):
        """
        Initializes a Level_Menu_Controller object.
        It also sets 3 flags: playing, get_tip and solve_level_ai.
        The playing flag is used to check if the player is currently playing a level.
        The get_tip flag is used to check if the player has asked for a tip.
        The solve_level_ai flag is used to check if the player has asked the AI to solve the level.
        Finally, it sets the moves list used to store the moves the AI as an empty list.
        
        Args:
            menu_model (Menu_Model): The model of the level menu.
            screen (pygame.Surface): The screen of the game.
            ai_type (str): The type of AI to be used in the level.
        """
        self.model = menu_model
        self.screen = screen
        self.ai_type = ai_type

        self.playing = False
        self.get_tip = False
        self.solve_level_ai = False
        self.moves = []

    def handle_events(self):
        """
        Handles the events of the level menu.

        If the player is playing a level, it checks if the player has asked for a tip or if the player has asked the AI to solve the level
        and calls the corresponding methods.
        
        If the player is playing a level, and the player has not asked for a tip or to solve the level, it calls the play_level method.
        
        Else, the player can navigate through the level menu using the arrow keys. Since the level menu has 2 columns, the player can navigate
        through the levels using the left and right arrow keys to move between columns, and the up and down arrow keys to move between rows.
        If the player presses the enter key, the selected level is loaded and the player starts playing the level.
        If the player presses the escape key, the player goes back to the main menu.
        
        Returns:
            bool: True if the player is still in the level menu, False otherwise.
        """
        if self.playing:
            if self.solve_level_ai:
                self.level_view.draw_creating_AI()
                pg.display.update()
                self.create_AI()
                self.solve_level_ai = False

                if self.moves == []:
                    self.level_model.won = False
                    return self.end_of_level(False)

                return self.solve_level()

            elif self.get_tip:
                self.level_view.draw_creating_AI()
                pg.display.update()
                self.create_AI()
                self.get_tip = False

                if self.moves == []:
                    self.level_model.won = False
                    return self.end_of_level(False)
                

                move = self.moves.pop(0)
                pg.time.wait(150)
                self.level_controller.handle_AIevents(move)
                pg.time.wait(150)
                self.level_view.draw()
                pg.display.update()
                self.moves = []

            else:
                return self.play_level()

        else:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        self.model.selected = (self.model.selected - 1) % len(
                            self.model.options
                        )
                        return True
                    if event.key == pg.K_RIGHT:
                        self.model.selected = (self.model.selected + 1) % len(
                            self.model.options
                        )
                        return True
                    if event.key == pg.K_UP:
                        self.model.selected = (self.model.selected - 2) % len(
                            self.model.options
                        )
                        return True
                    if event.key == pg.K_DOWN:
                        self.model.selected = (self.model.selected + 2) % len(
                            self.model.options
                        )
                        return True
                    if event.key == pg.K_RETURN:
                        level = "lvl" + str(self.model.selected + 1) + ".txt"
                        self.create_level(level)
                        self.playing = True
                        return True
                    if event.key == pg.K_ESCAPE:
                        return False
        return True

    def create_level(self, level):
        """
        Creates the level model, view, and controller.
        
        Args:
            level (str): The name of the level to be created.
        """
        self.level_model = Level_Model(level)
        self.level_view = Level_View(self.level_model, self.screen)
        self.level_controller = Level_Controller(self.level_model)

    def create_AI(self):
        """
        Creates the AI to solve the level, based on the type of AI selected by the player,
        and stores the moves the AI will make in the moves list.
        """
        
        state = Sokobond_State(self.level_model)

        goal = None

        if self.ai_type == "BFS":
            goal = Search.breadth_first_search(state)
        elif self.ai_type == "DFS":
            goal = Search.depth_first_search(state)
        elif self.ai_type == "Depth Limited":
            goal = Search.depth_limited_search(state, 25)
        elif self.ai_type == "Iterative Deepening":
            goal = Search.iterative_deepening_search(state, 25)
        elif self.ai_type == "Greedy - Manhattan Distance":
            goal = Search.greedy_search(state, Heuristic.manhattan_distance)
        elif self.ai_type == "Greedy - Prioritize Free Electrons":
            goal = Search.greedy_search(state, Heuristic.prioritize_free_electrons)
        elif self.ai_type == "Greedy - Minimize Free Electrons":
            goal = Search.greedy_search(state, Heuristic.minimize_free_electrons)
        elif self.ai_type == "A* - Manhattan Distance":
            goal = Search.a_star_search(state, Heuristic.manhattan_distance)
        elif self.ai_type == "A* - Prioritize Free Electrons":
            goal = Search.a_star_search(state, Heuristic.prioritize_free_electrons)
        elif self.ai_type == "A* - Minimize Free Electrons":
            goal = Search.a_star_search(state, Heuristic.minimize_free_electrons)

        if goal == None:
            return

        self.moves = Search.get_solution_moves(goal)

    def solve_level(self):
        """
        Solves the level using the moves stored in the moves list.
        Once the level is solved, it calls the end_of_level method with the result set to True.
        
        Returns:
            bool: False, to indicate that the player is no longer playing the level.
        """
        while len(self.moves) != 0:
            move = self.moves.pop(0)
            pg.time.wait(150)
            self.level_controller.handle_AIevents(move)
            pg.time.wait(150)
            self.level_view.draw()
            pg.display.update()

        self.level_model.won = True
        return self.end_of_level(True)

    def end_of_level(self, result):
        """
        Draws the end of level screen.
        If the player has won the level, it draws the end of level win screen.
        Else, it draws the end of level lose screen.
        
        If the player presses the enter key, the playing flag is set to False and the player goes back to the level menu.
        
        Args:
            result (bool): True if the player has won the level, False otherwise.
        """

        while self.playing:

            self.level_view.draw()
            if result:
                self.level_view.draw_end_of_level_win()
            else:
                self.level_view.draw_end_of_level_lose()
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.playing = False
                        return False

    def play_level(self):
        """
        Plays the level.
            
        If the player wants to quit the level, it sets the playing flag to False and returns False.
        Then, it handles the events of the level, and checks if the player has asked for a tip or if the player has asked the AI to solve the level, 
        changing the corresponding flags.
            
        Finally, it draws the level and updates the display.
        
        If the player has won the level, it calls the end_of_level method with the result set to True.
        
        Returns:
            bool: True if the player is still playing the level, False otherwise.
        """

        if self.level_controller.quit_level:
            self.playing = False
            return False

        self.level_controller.handle_events()
        if self.level_model.get_tip:
            self.get_tip = True
            self.level_model.get_tip = False

        elif self.level_model.solve_level_ai:
            self.solve_level_ai = True
            self.level_model.solve_level_ai = False

        self.level_view.draw()
        pg.display.update()

        self.level_controller.check_win()

        if self.level_model.won:
            return self.end_of_level(True)

        return True
