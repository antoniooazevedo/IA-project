import pygame as pg
import sys

class Molecule_Model:
    def __init__(self, atoms, connections_list=None, isPlayer=False):
        self.isPlayer = isPlayer
        self.molecule = dict()

        for i, atom in enumerate(atoms):
            if connections_list is not None and i < len(connections_list):
                connections = connections_list[i]
            else:
                connections = []
        self.molecule[atom] = connections

    def get_atom(self):
        return list(self.molecule.keys())[0]
