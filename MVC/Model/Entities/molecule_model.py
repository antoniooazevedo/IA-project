class Molecule_Model:
    """
    Class that represents a molecule in the game.
    
    It is responsible for storing the atoms and their connections.
    It also has a flag to check if the molecule is the player's.
    """
    def __init__(self, atoms, connections_list=None, isPlayer=False):
        """
        Initializes a Molecule_Model object.
        
        Args:
            atoms (list): A list of atoms in the molecule.
            connections_list (list): A list of lists of connections between atoms.
            isPlayer (bool): A flag to check if the molecule is the player's.
        """
        self.isPlayer = isPlayer
        self.molecule = dict()

        for i, atom in enumerate(atoms):
            if connections_list is not None and i < len(connections_list):
                connections = connections_list[i]
            else:
                connections = []
        self.molecule[atom] = connections

    def get_molecule(self):
        """
        Returns the object.
        
        Returns:
            Molecule_Model: The object.
        """
        return self

    def get_atoms(self):
        """
        Returns the atoms in the molecule.
        
        Returns:
            list: The atoms in the molecule.
        """
        return list(self.molecule.keys())

    def get_connections(self):
        """
        Returns the connections between atoms in the molecule.
        
        Returns:
            list: The connections between atoms in the molecule.
        """
        ret = []
        for _, v in self.molecule.items():
            ret.extend(v)

        return ret

    def __str__(self):
        """
        Returns a string representation of the Molecule_Model object.
        
        Returns:
            str: A string representation of the Molecule_Model object.
        """
        return str(self.molecule)
