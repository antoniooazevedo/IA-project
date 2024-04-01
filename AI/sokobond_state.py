import copy
from MVC.Controller.level_controller import Level_Controller
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Model.Entities.wall_model import Wall_Model


class Sokobond_State:

    """
    Class that represents a state of the Sokobond game.
    """

    def __init__(self, level):

        """
        Initializes a Sokobond_State object.

        Args:
            level (Level_Model): The model of the level.
        """

        self.level = level

    def __eq__(self, other):

        """
        Compares two Sokobond_State objects for equality.

        Two Sokobond_State objects are considered equal if they are of the same class, 
        their string representations are equal and they have the same set of connections 
        between their molecules.

        Args:
            other (Sokobond_State): The other Sokobond_State object to compare with.

        Returns:
            bool: True if the two Sokobond_State objects are equal, False otherwise.
        """

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
                        innerTest = innerTest or c == o

                    sameConnections = sameConnections and innerTest
                    if not sameConnections:
                        break

                return sameConnections
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        """
        Compares two Sokobond_State objects for inequality.

        This method uses the __eq__ method to determine if two Sokobond_State objects are equal, 
        and then returns the opposite result.

        Args:
            other (Sokobond_State): The other Sokobond_State object to compare with.

        Returns:
            bool: True if the two Sokobond_State objects are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __hash__(self):
        """
        Returns a hash value for a Sokobond_State object.

        Returns:
            int: The hash value of the Sokobond_State object.
        """
        return hash(self.__str__())

    def __str__(self):

        """
        Returns a string representation of the Sokobond_State object, based
        on the level's matrix.
        """
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
        """
        Prints the string representation of the Sokobond_State object.
        """
        print(self.__str__())

    def move_up(self):
        """
        Generates a new Sokobond_State object by moving the player's molecule up.

        Returns:
            Sokobond_State: The new Sokobond_State object.
        """

        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move("up")

        new_state = Sokobond_State(copy_level)
        
        if self.__eq__(new_state):
            return None 
        
        return new_state

    def move_down(self):
        """
        Generates a new Sokobond_State object by moving the player's molecule down.

        Returns:
            Sokobond_State: The new Sokobond_State object.
        """

        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move("down")
        new_state = Sokobond_State(copy_level)
        
        if self.__eq__(new_state):
            return None 
        
        return new_state

    def move_left(self):
        """
        Generates a new Sokobond_State object by moving the player's molecule left.

        Returns:
            Sokobond_State: The new Sokobond_State object.
        """

        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move("left")
        new_state = Sokobond_State(copy_level)
        
        if self.__eq__(new_state):
            return None 
        
        return new_state

    def move_right(self):
        """
        Generates a new Sokobond_State object by moving the player's molecule right.

        Returns:
            Sokobond_State: The new Sokobond_State object.
        """
        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.player_move("right")
        new_state = Sokobond_State(copy_level)
        
        if self.__eq__(new_state):
            return None 
        
        return new_state

    def child_states(self):
        """
        Generates all possible child states of the current state with the possible operators.

        Returns:
            list: A list of tuples, where each tuple contains the direction of the operator and the new state.
        """
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
        """
        Checks if the current state is a goal state and changes the won attribute of the level model.

        Returns:
            bool: True if the current state is a goal state, False otherwise.
        """

        copy_level = copy.deepcopy(self.level)
        controller = Level_Controller(copy_level)
        controller.check_win()
        return controller.model.won
