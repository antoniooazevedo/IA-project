import pygame as pg
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Model.Entities.connection_model import Connection_Model
from MVC.Model.Entities.wall_model import Wall_Model
from MVC.Controller.Entities.atom_controller import Atom_Controller
from MVC.Controller.Entities.connection_controller import Connection_Controller


class Molecule_Controller:
    """
    Class that represents the controller of a molecule in the MVC pattern.
    
    It is responsible for handling the movements of the molecule, such as the player's movements.
    It also checks if the molecule can move in a given direction.
    """
    
    def __init__(self, molecule_Model: Molecule_Model, matrix):
        """
        Initializes a Molecule_Controller object.
        
        Args:
            molecule_Model (Molecule_Model): The model of the molecule.
            matrix (list): The matrix of the game.
        """
        self.model = molecule_Model
        self.matrix = matrix

    def check_move(self, direction):
        """
        Checks if the molecule can move in the given direction.
        If the molecule can move, it moves the molecule in the given direction.
        It also pushes the molecules that are in the way of the moving molecule.
        
        Args:
            direction (str): The direction in which the molecule should move.
            
        Returns:
            bool: True if the molecule can move in the given direction, False otherwise.
        """
        
        atoms = self.model.get_atoms()
        can_move = True
        pushed_molecules = []

        for atom in atoms:
            atomController = Atom_Controller(atom, self.matrix)
            obj = atomController.direction_check(direction)

            if isinstance(obj, Wall_Model):
                return False

            elif isinstance(obj, Molecule_Model) and obj != self.model:
                controller = Molecule_Controller(obj, self.matrix)
                can_move = can_move and controller.check_move(direction)
                pushed_molecules.append(controller)

            elif obj == None:
                can_move = can_move and True

        if can_move:
            for controller in pushed_molecules:
                controller.move(direction)

        return can_move

    def move(self, direction):
        """        
        If the molecule can move, it moves the molecule in the given direction.
        Then it updates the matrix with the new positions of the atoms and the molecule.
        
        Args:
            direction (str): The direction in which the molecule should move.
        
        Returns:
            bool: True if the molecule can move in the given direction, False otherwise.
        """
        if self.check_move(direction):
            atoms = self.model.get_atoms()
            list_positions = []
            list_new_positions = []

            for atom in atoms:
                atomController = Atom_Controller(atom, self.matrix)

                x, y = atom.get_position()
                list_positions.append((x, y))

                if direction == "up":
                    atomController.move("up")
                elif direction == "down":
                    atomController.move("down")
                elif direction == "left":
                    atomController.move("left")
                elif direction == "right":
                    atomController.move("right")

                x, y = atom.get_position()
                list_new_positions.append((x, y))

            for x, y in list_positions:
                self.matrix[y][x] = None

            for x, y in list_new_positions:
                self.matrix[y][x] = self.model

            for connection in self.model.get_connections():
                connectionController = Connection_Controller(connection)
                connectionController.move(direction)

            return True

        return False

    def connect(self, my_molecule, my_atom, direction):
        """
        Adds a connection to the molecule and removes an electron from the atom.
        
        Args:
            my_molecule (Molecule_Model): The molecule that will receive the connection.
            my_atom (Atom_Model): The atom that will lose an electron.
            direction (str): The direction of the connection.
        """
        my_x, my_y = my_atom.get_position()
        my_connection = Connection_Model(my_x, my_y, direction)
        my_molecule.molecule[my_atom].append(my_connection)
        my_atom.set_electrons(my_atom.get_electrons() - 1)

    def new_connection(
        self, new_x, new_y, my_molecule, current_atom, direction, opposite_direction
    ):
        """
        Connects two molecules.
        
        Args:
            new_x (int): The x-coordinate of the opposite molecule.
            new_y (int): The y-coordinate of the opposite molecule.
            my_molecule (Molecule_Model): The molecule that will receive the connection and the atoms of the opposite molecule.
            current_atom (Atom_Model): The atom that will lose an electron.
            direction (str): The direction of the connection.
            opposite_direction (str): The opposite direction of the connection.
        """
        adjacent = self.matrix[new_y][new_x].get_molecule()
        atoms = adjacent.get_atoms()
        connection_done = False

        for a in atoms:
            if a.get_position() == (new_x, new_y):
                if a.get_electrons() <= 0 or current_atom.get_electrons() <= 0:
                    continue
                self.connect(my_molecule, current_atom, direction)
                self.connect(adjacent, a, opposite_direction)
                connection_done = True
                break

        if connection_done:

            if my_molecule.isPlayer or adjacent.isPlayer:
                my_molecule.isPlayer = True
                adjacent.isPlayer = True

            for atom, connections in adjacent.molecule.items():
                my_molecule.molecule[atom] = connections

            for atom in atoms:
                x, y = atom.get_position()
                self.matrix[y][x] = my_molecule

    def make_connections(self, current_atom):
        """
        Checks if the molecule can connect to another molecule.
        If it can, it connects the molecules.
        
        Args:
            current_atom (Atom_Model): The atom that will try to connect to another molecule.
        """
        x, y = current_atom.get_position()

        if current_atom.get_electrons() == 0:
            return

        molecule = self.model.get_molecule()

        possible_up = (
            isinstance(self.matrix[y - 1][x], Molecule_Model)
            and self.matrix[y - 1][x].get_molecule() != molecule
        )
        possible_down = (
            isinstance(self.matrix[y + 1][x], Molecule_Model)
            and self.matrix[y + 1][x].get_molecule() != molecule
        )
        possible_left = (
            isinstance(self.matrix[y][x - 1], Molecule_Model)
            and self.matrix[y][x - 1].get_molecule() != molecule
        )
        possible_right = (
            isinstance(self.matrix[y][x + 1], Molecule_Model)
            and self.matrix[y][x + 1].get_molecule() != molecule
        )

        if possible_up:
            self.new_connection(x, y - 1, molecule, current_atom, "up", "down")

        if possible_down:
            self.new_connection(x, y + 1, molecule, current_atom, "down", "up")

        if possible_left:
            self.new_connection(x - 1, y, molecule, current_atom, "left", "right")

        if possible_right:
            self.new_connection(x + 1, y, molecule, current_atom, "right", "left")
