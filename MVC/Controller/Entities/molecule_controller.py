import pygame as pg
import sys
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Model.Entities.connection_model import Connection_Model
from MVC.Model.Entities.wall_model import Wall_Model
from MVC.Controller.Entities.atom_controller import Atom_Controller
from MVC.Controller.Entities.connection_controller import Connection_Controller

class Molecule_Controller:
    def __init__(self, molecule_Model: Molecule_Model, matrix):
        self.model = molecule_Model
        self.matrix = matrix

    def check_move(self, direction):
        atoms = self.model.get_atoms()
        can_move = True
        other_molecules = []
        
        for atom in atoms: 
            atomController = Atom_Controller(atom, self.matrix)
            obj = atomController.direction_check(direction)
            
            if isinstance(obj, Wall_Model):
                return False

            elif isinstance(obj, Molecule_Model) and obj != self.model:
                controller = Molecule_Controller(obj, self.matrix)
                can_move = can_move and controller.check_move(direction)
                other_molecules.append(controller)

            elif obj == None:
                can_move = can_move and True

        if (can_move):
            for molecule_controller in other_molecules:
                molecule_controller.move(direction)
            
        return can_move
    
    def move(self, direction):
        if (self.check_move(direction)):
            atoms = self.model.get_atoms()

            for atom in atoms:
                atomController = Atom_Controller(atom, self.matrix)
                x, y = atom.get_position()
                if direction == 'up':
                    atomController.move('up')
                    self.matrix[y][x] = None
                    self.matrix[y-1][x] = self.model      
                elif direction == 'down':
                    atomController.move('down')
                    self.matrix[y][x] = None
                    self.matrix[y+1][x] = self.model
                elif direction == 'left':
                    atomController.move('left')
                    self.matrix[y][x] = None
                    self.matrix[y][x-1] = self.model
                elif direction == 'right':
                    atomController.move('right')
                    self.matrix[y][x] = None
                    self.matrix[y][x+1] = self.model

            for connection in self.model.get_connections():
                connectionController = Connection_Controller(connection)
                connectionController.move(direction)
            
            return True
                
        return False
    
    
    def connect(self, my_molecule, my_atom, direction):
        my_x, my_y = my_atom.get_position()
        my_connection = Connection_Model(my_x, my_y, direction)
        my_molecule.molecule[my_atom].append(my_connection)
        my_atom.set_electrons(my_atom.get_electrons() - 1)
    
    def new_connection(self, new_x, new_y, my_molecule, current_atom, direction, opposite_direction):
        adjacent = self.matrix[new_y][new_x].get_molecule()
        atoms = adjacent.get_atoms()
        connection_done = False

        for a in atoms:
            if a.get_position() == (new_x, new_y):
                if a.get_electrons() == 0:
                    continue
                self.connect(my_molecule, current_atom, direction)
                self.connect(adjacent, a, opposite_direction)
                connection_done = True
                break
        if connection_done:    
            for (atom, connections) in adjacent.molecule.items():
                my_molecule.molecule[atom] = connections
            
            for atom in atoms:
                x, y = atom.get_position()
                self.matrix[y][x] = my_molecule

    def make_connections(self, current_atom):
        x,y = current_atom.get_position()
        
        if current_atom.get_electrons() == 0:
            return False

        molecule = self.model.get_molecule()
        
        possible_up = isinstance(self.matrix[y-1][x], Molecule_Model) and self.matrix[y-1][x].get_molecule() != molecule
        possible_down = isinstance(self.matrix[y+1][x], Molecule_Model) and self.matrix[y+1][x].get_molecule() != molecule
        possible_left = isinstance(self.matrix[y][x-1], Molecule_Model) and self.matrix[y][x-1].get_molecule() != molecule
        possible_right = isinstance(self.matrix[y][x+1], Molecule_Model) and self.matrix[y][x+1].get_molecule() != molecule
        
        
        
        if possible_up:
            self.new_connection(x, y-1, molecule, current_atom, "up", "down")
            
        if possible_down:
            self.new_connection(x, y+1, molecule, current_atom, "down", "up")
        
        if possible_left:	
            self.new_connection(x-1, y, molecule, current_atom, "left", "right")
                            
        if possible_right:
            self.new_connection(x+1, y, molecule, current_atom, "right", "left")
                                    
                    
        
            
         
        
        
        


    
        