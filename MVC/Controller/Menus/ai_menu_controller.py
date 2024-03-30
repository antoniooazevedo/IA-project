import pygame as pg
import sys

from MVC.Model.menu_model import Menu_Model


class AI_Menu_Controller:
    def __init__(self, menu_model: Menu_Model):
        self.model = menu_model
        self.ai = "A* - Manhattan Distance"

    def handle_events(self):
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
                    self.model.selected = (self.model.selected - 1) % len(
                        self.model.options
                    )
                    return True
                if event.key == pg.K_DOWN:
                    self.model.selected = (self.model.selected + 1) % len(
                        self.model.options
                    )
                    return True
                if event.key == pg.K_RETURN:
                    self.select_ia()
                    return False
                if event.key == pg.K_ESCAPE:
                    return False
        return True

    def select_ia(self):
        if self.model.selected == 0:
            self.ai = "BFS"
        elif self.model.selected == 1:
            self.ai = "DFS"
        elif self.model.selected == 2:
            self.ai = "Depth Limited"
        elif self.model.selected == 3:
            self.ai = "Iterative Deepening"
        elif self.model.selected == 4:
            self.ai = "Greedy - Manhattan Distance"
        elif self.model.selected == 5:
            self.ai = "Greedy - Free Electrons"
        elif self.model.selected == 6:
            self.ai = "Greedy - Minimize Free Electrons"
        elif self.model.selected == 7:
            self.ai = "A* - Manhattan Distance"
        elif self.model.selected == 8:
            self.ai = "A* - Free Electrons"
        elif self.model.selected == 9:
            self.ai = "A* - Mini"
        elif self.model.selected == 10:
            return
