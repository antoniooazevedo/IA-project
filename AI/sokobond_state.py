import copy
from MVC.Controller.level_controller import Level_Controller
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Model.Entities.wall_model import Wall_Model


class Sokobond_State:

    def __init__(self, level):
        self.level = level

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.__str__() == other.__str__():
                connections = []
                for m in self.level.molecules:
                    connections.extend(m.get_connections())

                other_connections = []
                for m in other.level.molecules:
                    other_connections.extend(m.get_connections())

                sameConnections = True

                for c in connections:
                    innerTest = False
                    for o in other_connections:
                        innerTest = innerTest or (c == o)

                    sameConnections = sameConnections and innerTest

                return sameConnections
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__str__())

    def __str__(self):
        matrix_str = ""
        x = -1
        y = -1
        for row in self.level.matrix:
            y += 1
            matrix_str += ","
            for cell in row:
                x += 1
                if isinstance(cell, Wall_Model):
                    matrix_str += ",#"
                elif isinstance(cell, Molecule_Model):
                    for a in cell.get_atoms():
                        if (x, y) == a.get_position():
                            matrix_str += "," + a.element
                            break
                else:
                    matrix_str += ", "
            matrix_str += ",\n"
            x = -1
        return matrix_str

    def printState(self):
        print(self.__str__())

    def move_up(self):
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move("up")
        return Sokobond_State(copy_level)

    def move_down(self):
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move("down")
        return Sokobond_State(copy_level)

    def move_left(self):
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move("left")
        return Sokobond_State(copy_level)

    def move_right(self):
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move("right")
        return Sokobond_State(copy_level)

    def child_states(self):
        new_states = []
        if self.move_up():
            new_states.append(("up", self.move_up()))
        if self.move_right():
            new_states.append(("right", self.move_right()))
        if self.move_left():
            new_states.append(("left", self.move_left()))
        if self.move_down():
            new_states.append(("down", self.move_down()))
        return new_states

    def is_goal(self):
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.check_win()
        return controller.model.won
