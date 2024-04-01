import pygame as pg

from MVC.Model.level_model import Level_Model
from MVC.Controller.Entities.molecule_controller import Molecule_Controller
from MVC.Model.Entities.molecule_model import Molecule_Model

class Level_Controller:
    """
    Class that represents the controller of a level in the MVC pattern.
    
    It is responsible for handling the events of the level, such as the player's movements.
    It also checks if the player has won the level.
    """

    def __init__(self, level_model: Level_Model):
        """
        Initializes a Level_Controller object.
        Then connects the molecules in the level.
        Finally, it sets the default quit_level flag to False.
        
        Args:
            level_model (Level_Model): The model of the level.
        """
        self.model = level_model
        self.connect_molecules()
        self.quit_level = False

    def check_win(self):
        """
        Checks if the player has won the level.
        To win the level, there must be only one molecule left, and all its atoms must have zero electrons left.
        If there is more than one molecule left, the player has not won the level.
        If a single atom has electrons left, the player has not won the level.
        Else, the player has won the level.
        """

        if self.model.won:
            return

        if len(self.model.molecules) != 1:
            self.model.won = False
            return

        for atom in self.model.molecules[0].get_atoms():
            if atom.get_electrons() != 0:
                self.model.won = False
                return

        self.model.won = True

    def player_move(self, direction):
        """
        Tries to move the player's molecule in the given direction.
        Then connects the molecules in the level.
        
        Args:
            direction (str): The direction in which the player's molecule should move.
        """
        playerMolecule = self.model.get_player_molecule()
        molecule_controller = Molecule_Controller(playerMolecule, self.model.matrix)
        molecule_controller.move(direction)
        self.connect_molecules()

    def handle_events(self):
        """
        Handles the events of the level.
        If the player presses the escape key, the "r" key or the "t" key,the quit_level flag,
        the solve_level_ai flag, or the get_tip flag are set to True, respectively.
        If the player presses the up, down, left, or right key, the player's molecule is moved in the corresponding direction.
        
        Finally, the molecules in the level are connected.
        """
        
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit_level = True
                    return
                elif event.key == pg.K_UP or event.key == pg.K_w:
                    self.player_move("up")
                elif event.key == pg.K_DOWN or event.key == pg.K_s:
                    self.player_move("down")
                elif event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.player_move("left")
                elif event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.player_move("right")
                elif event.key == pg.K_r:
                    self.model.solve_level_ai = True
                elif event.key == pg.K_t:
                    self.model.get_tip = True

        self.connect_molecules()

    def handle_AIevents(self, move):
        """
        Handles the events of the level when the AI is playing.
        The player's molecule is moved in the given direction.
        Then the molecules in the level are connected.
        Finally, it checks if the player has won the level.
        
        Args:
            move (str): The direction in which the player's molecule should move.
        """
        self.player_move(move)
        self.connect_molecules()
        self.check_win()

    def remove_old_molecules(self):
        """
        Recalculates the molecules in the level.
        """
        self.model.molecules = []
        for x in self.model.matrix:
            for elem in x:
                if (
                    isinstance(elem, Molecule_Model)
                    and elem not in self.model.molecules
                ):
                    self.model.molecules.append(elem)

    def connect_molecules(self):
        """
        Connects the molecules in the level.
        """
        for row in self.model.matrix:
            for entity in row:

                if isinstance(entity, Molecule_Model):
                    controller = Molecule_Controller(entity, self.model.matrix)
                    for atom in entity.get_atoms():
                        controller.make_connections(atom)
                        self.remove_old_molecules()
