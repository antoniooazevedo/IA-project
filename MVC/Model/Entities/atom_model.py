class Atom_Model:

    def __init__(self, x, y, element, electrons, isPlayer=False, image_path=""):
        self.x = x
        self.y = y
        self.element = element
        self.electrons = electrons
        self.isPlayer = isPlayer
        self.image_path = image_path

    def __str__(self):
        return self.element

    def get_position(self):
        return self.x, self.y

    def get_atom(self):
        return self

    def get_electrons(self):
        return self.electrons

    def set_electrons(self, electrons):
        self.electrons = electrons
