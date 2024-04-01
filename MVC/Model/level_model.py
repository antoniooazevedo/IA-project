from MVC.Model.Entities.molecule_model import Molecule_Model as Molecule_Model
from MVC.Controller.Entities.molecule_controller import Molecule_Controller
from MVC.Model.Entities.atom_model import Atom_Model as Atom_Model
from MVC.Model.Entities.wall_model import Wall_Model as Wall_Model
from MVC.Model.Entities.connection_model import Connection_Model as Connection_Model

"""
n_connections represents the number of connections each atom can have. If the atom is uppercase, it is a field atom, and if it is lowercase, it is a player atom.
image_paths represents the path to the image of each atom.
BASE_LVL_PATH is the path to the levels folder.
"""
n_connections = {"H": 1, "O": 2, "N": 3, "C": 4, "h": 1, "o": 2, "n": 3, "c": 4}

image_paths = {
    "H": "assets/images/h-field.png",
    "O": "assets/images/o-field.png",
    "N": "assets/images/n-field.png",
    "C": "assets/images/c-field.png",
    "h": "assets/images/h-player.png",
    "o": "assets/images/o-player.png",
    "n": "assets/images/n-player.png",
    "c": "assets/images/c-player.png",
    "#": "assets/images/wall.png",
}

BASE_LVL_PATH = "assets/levels/"


class Level_Model:
    """
    Class that represents the model of a level in the MVC pattern.
    
    It is responsible for storing the level data, such as the matrix of the level and the molecules.
    
    It also controls if the player has won the level, if the player wants a tip, and if the AI should solve the level.
    """
    
    def __init__(self, level):
        """
        Initializes a Level_Model object.
        
        Args:
            level (str): The name of the level file to load.
        """
        self.won = False
        self.molecules = []
        self.scrape_level(level)

        self.get_tip = False
        self.solve_level_ai = False

    def scrape_level(self, level):
        """
        Scrape the level file and create the level matrix.
        The level file is a text file where each character represents a different component of the level:
        - " " represents an empty space.
        - "#" represents a wall.
        - Uppercase letters represent field atoms.
        - Lowercase letters represent player atoms.
        
        When each component is read, we create the corresponding model and add it to the level matrix.
        
        Args:
            level (str): The name of the level file to load.
        """

        matrix = []

        row = 0
        col = 0

        with open(BASE_LVL_PATH + level, "r") as file:
            lines = file.read().split("\n")
            for line in lines:
                col = 0
                m_line = []
                components = line.split(",")
                for component in components:
                    if component == " ":
                        m_line.append(None)

                    elif component == "#":
                        m_line.append(Wall_Model(col, row, image_paths[component]))

                    elif component.isupper():
                        n = n_connections[component]
                        atom = Atom_Model(
                            col, row, component, n, False, image_paths[component]
                        )
                        molecule = Molecule_Model([atom], [])

                        m_line.append(molecule)
                        self.molecules.append(molecule)

                    elif component.islower():
                        n = n_connections[component]
                        atom = Atom_Model(
                            col, row, component, n, True, image_paths[component]
                        )
                        molecule = Molecule_Model([atom], [], True)
                        m_line.append(molecule)
                        self.molecules.append(molecule)

                    col += 1
                row += 1
                matrix.append(m_line)

        self.matrix = matrix

    def get_player_molecule(self):
        """
        Getter for the player molecule.
        
        Returns:
            Molecule_Model: The player molecule.
        """
        
        for molecule in self.molecules:
            if molecule.isPlayer:
                return molecule
        return None
