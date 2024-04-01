import pygame as pg
from MVC.Model.menu_model import Menu_Model
from MVC.View.menu_view import Menu_View
from MVC.Controller.Menus.main_menu_controller import Main_Menu_Controller
import utils as utils

# Constants
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)


class Game:
    """
    The main class of the game.
    """

    def __init__(self):
        """
        Create a new Game object.
        
        Starts the game by initializing Pygame and creating the window.
        Also initializes the clock and the frames per second.
        """
        pg.init()

        pg.display.set_caption("Sokobond")
        self.screen = pg.display.set_mode(WINDOW_SIZE)

        self.clock = pg.time.Clock()
        self.fps = 60

    def run(self):
        """
        Runs the game.
        
        Creates the main menu and runs a game loop 
        where we handle events on the main menu. Then, if the user is not playing neither on a different menu,
        we draw the main menu and update the display.
        Finally, we tick the clock. 
        """
        main_menu_model = Menu_Model(["Play", "Choose AI", "Quit"], "SOKOBOND", 50)
        main_menu_view = Menu_View(self.screen, main_menu_model, 1)
        main_menu_controller = Main_Menu_Controller(main_menu_model, self.screen)

        while True:
            main_menu_controller.handle_events()

            if (
                (not main_menu_controller.on_level_menu)
                and (not main_menu_controller.level_menu_controller.playing)
                and (not main_menu_controller.on_ai_menu)
            ):
                main_menu_view.draw()
                pg.display.update()

            self.clock.tick(self.fps)


Game().run()
