import pygame as pg
import sys

from MVC.Model.level_model import Level_Model
from MVC.View.level_view import Level_View
from MVC.Controller.level_controller import Level_Controller
from MVC.Model.menu_model import Menu_Model
from AI.sokobond_state import Sokobond_State
from AI.tree_node import Search, Heuristic


class Level_Menu_Controller:
    def __init__(self, menu_model: Menu_Model, screen, ai_type):
        self.model = menu_model
        self.screen = screen
        self.ai_type = ai_type

        self.playing = False
        self.get_tip = False
        self.solve_level_ai = False
        self.moves = []

    def handle_events(self):

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
        self.level_model = Level_Model(level)
        self.level_view = Level_View(self.level_model, self.screen)
        self.level_controller = Level_Controller(self.level_model)

    def create_AI(self):
        state = Sokobond_State(self.level_model)

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

    def solve_level(self):
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
