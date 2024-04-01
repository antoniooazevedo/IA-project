import pygame as pg
from MVC.Model.Entities.atom_model import Atom_Model
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Model.Entities.wall_model import Wall_Model


class Atom_Controller:
    """
    Class that represents the controller of an atom in the MVC pattern.
    """
    def __init__(self, Atom_Model: Atom_Model, matrix):
        """
        Initializes an Atom_Controller object.
        
        Args:
            Atom_Model (Atom_Model): The model of the atom.
            matrix (list): The matrix of the game.
        """
        self.atom = Atom_Model
        self.matrix = matrix

    def direction_check(self, direction):
        """
        Checks if the atom can move in the given direction.
        
        Args:
            direction (str): The direction in which the atom should move. It can be "up", "down", "left" or "right".
            
        Returns:
            object: The object that is in the way of the atom in the given direction.
        """
        x, y = self.atom.get_position()
        if direction == "up":
            return self.matrix[y - 1][x]

        elif direction == "down":
            return self.matrix[y + 1][x]

        elif direction == "left":
            return self.matrix[y][x - 1]

        elif direction == "right":
            return self.matrix[y][x + 1]

    def move(self, direction):
        """
        Updates the position of the atom in the given direction.
        
        Args:
            direction (str): The direction in which the atom should move.
        """
        if direction == "up":
            self.atom.y -= 1
        elif direction == "down":
            self.atom.y += 1
        elif direction == "left":
            self.atom.x -= 1
        elif direction == "right":
            self.atom.x += 1
