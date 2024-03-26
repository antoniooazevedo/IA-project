import copy
from MVC.Model.level_model import Level_Model
from MVC.Controller.level_controller import Level_Controller
from MVC.Controller.Entities.molecule_controller import Molecule_Controller
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Model.Entities.wall_model import Wall_Model


class Sokobond_State:

    def __init__(self, level):
        self.level = level

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__str__() == other.__str__()
        else:
            return False

    def __hash__(self):
        return hash(self.__str__())
    
    def __str__(self):
        matrix_str = ''
        for row in self.level.matrix:
            matrix_str += ','
            for cell in row:
                if isinstance(cell, Wall_Model):
                    matrix_str += ',#'
                elif isinstance(cell, Molecule_Model):
                    if cell.isPlayer:
                        matrix_str += ',P'
                    else: 
                        matrix_str += ',M'
                else:
                    matrix_str += ', '
            matrix_str += ',\n'
        return matrix_str
    
    def printState(self):
        print(self.__str__())

    def move_up(self):
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move('up')
        return Sokobond_State(copy_level)    

    def move_down(self):
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move('down')
        return Sokobond_State(copy_level)
    
    def move_left(self):
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move('left')
        return Sokobond_State(copy_level)
    
    def move_right(self):
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move('right')
        return Sokobond_State(copy_level)
    
        
    def child_states(self):
        new_states = []
        if self.move_up():
            new_states.append(self.move_up())
        if self.move_right():
            new_states.append(self.move_right())
        if self.move_left():
            new_states.append(self.move_left())
        if self.move_down():
            new_states.append(self.move_down())
        return new_states

    def is_goal(self):
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.check_win()
        return controller.model.won

    