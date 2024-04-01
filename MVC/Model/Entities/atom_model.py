class Atom_Model:
    """
    Class that represents an atom in the game.
    
    It is responsible for storing the position of the atom, the element of the atom, the number of remaining electrons in the atom,
    a flag to check if the atom is the player's, and the path to the image of the atom.
    """

    def __init__(self, x, y, element, electrons, isPlayer=False, image_path=""):
        """
        Initializes an Atom_Model object.
        
        Args:
            x (int): The x position of the atom.
            y (int): The y position of the atom.
            element (str): The element of the atom.
            electrons (int): The number of remaining electrons in the atom.
            isPlayer (bool): A flag to check if the atom is the player's.
            image_path (str): The path to the image of the atom.
        """
        self.x = x
        self.y = y
        self.element = element
        self.electrons = electrons
        self.isPlayer = isPlayer
        self.image_path = image_path

    def __str__(self):
        """
        Returns a string representation of the Atom_Model object.
        
        Returns:
            str: A string representation of the Atom_Model object.
        """
        return self.element

    def get_position(self):
        """
        Getter of the position of the atom.
        
        Returns:
            tuple: The position of the atom.
        """
        return self.x, self.y

    def get_atom(self):
        """
        Getter of the object.
        
        Returns:
            Atom_Model: The object.
        """
        return self

    def get_electrons(self):
        """
        Getter of the number of remaining electrons in the atom.
        
        Returns:
            int: The number of remaining electrons in the atom.
        """
        return self.electrons

    def set_electrons(self, electrons):
        """
        Setter of the number of remaining electrons in the atom.
        
        Args:
            electrons (int): The number of remaining electrons in the atom.
        """
        self.electrons = electrons
