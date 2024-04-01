import pygame as pg

from MVC.Model.menu_model import Menu_Model


class Menu_View:
    """
    Class that represents the view of the Menu in the MVC pattern.
    
    It is responsible for drawing the menu on the screen.
    """

    def __init__(self, screen, menu_model: Menu_Model, n_columns):
        """
        Initializes a Menu_View object.

        Args:
            screen (pygame.Surface): The surface to render the menu on.
            menu_model (Menu_Model): The model object containing the menu data.
            n_columns (int): The number of columns to display in the menu.
        """
        
        self.screen = screen
        self.model = menu_model
        self.n_columns = n_columns

        pg.font.init()
        font_path = "assets/fonts/RhodiumLibre-Regular.ttf"
        self.bigFont = pg.font.Font(font_path, 100)
        self.optionFont = pg.font.Font(font_path, self.model.optionsFontSize)

    def draw_big_text(self):
        """
        Draw the big text at the top of the screen.
        """
        text = self.bigFont.render(self.model.bigText, True, (0, 0, 0))
        text_width = text.get_width()
        self.screen.blit(text, ((800 - text_width) / 2, 10))

    def draw_options(self):
        """
        Draw the options in the menu.
        
        The options are displayed in a grid with n_columns columns.
        Since the dimensions of the screen are fixed, the height of the options
        is calculated based on the number of options and the number of columns.
        
        The selected option is highlighted with a black rectangle.
        """
        
        options_count = len(self.model.options)
        option_height = self.optionFont.get_height()
        total_height = (
            (options_count + self.n_columns - 1) // self.n_columns
        ) * option_height
        start_y = (600 - total_height) // 2 + 100

        for i in range(options_count):
            text = self.optionFont.render(self.model.options[i], True, (0, 0, 0))
            text_width = text.get_width()
            column = i % self.n_columns
            row = i // self.n_columns
            x = (800 // self.n_columns - text_width) // 2 + column * (
                800 // self.n_columns
            )
            y = start_y + row * option_height - 10
            self.screen.blit(text, (x, y))
            if i == self.model.selected:
                pg.draw.rect(
                    self.screen,
                    (0, 0, 0),
                    (x - 10, y - 10, text_width + 20, option_height + 5),
                    3,
                )

    def draw(self):
        """
        Simply draw the menu on the screen, by calling the draw_big_text and draw_options methods after clearing the screen.
        """
        self.screen.fill((255, 255, 255))
        self.draw_big_text()
        self.draw_options()
