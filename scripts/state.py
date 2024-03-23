from scripts.entities import Atom, Wall, Connection
from scripts.player import Player

class SokobondState:
    def __init__(self, matrix, player):
        self.matrix = [row[:] for row in matrix]
        self.player = player
        self.connections = self.get_connections()

    def get_connections(self):
        connections = []
        for row in self.matrix:
            for cell in row:
                if isinstance(cell, Atom):
                    connections.extend(cell.connections)
        return connections

    def __eq__(self, other):
        if isinstance(other, SokobondState):
            return self.matrix == other.matrix and self.player == other.player
        return False
    
    def __hash__(self):
        return hash(str(self.matrix) + str(self.player))
    
    def __str__(self):
        matrix_str = '\n'.join([' '.join([str(cell) for cell in row]) for row in self.matrix])
        player_str = str(self.player)
        connections_str = ', '.join([str(connection) for connection in self.connections])
        return f"Matrix:\n{matrix_str}\nPlayer: {player_str}\nConnections: {connections_str}"
    
    def printState(self):
        print(self.__str__())

    def is_goal_state(self):
        for row in self.matrix:
            for cell in row:
                if isinstance(cell, Atom) and len(cell.connections) != cell.n_connections:
                    return False
        return True
    
    def move_up(self):
        new_matrix = [row[:] for row in self.matrix]
        for y, row in enumerate(new_matrix):
            for x, cell in enumerate(row):
                if isinstance(cell, Atom) and cell == self.player.atom:
                    if y > 0 and cell.check_move([cell]):
                        new_atom = Atom(cell.game, x, y - 1, cell.type)
                        new_atom.connections = cell.connections
                        new_matrix[y][x] = None
                        new_matrix[y - 1][x] = new_atom
                        new_player = Player(new_atom, self.player.game)
                        new_player.make_possible_connections(new_matrix)
                        return SokobondState(new_matrix, new_player)
        return None
    
    def move_down(self):
        new_matrix = [row[:] for row in self.matrix]
        for y, row in enumerate(new_matrix):
            for x, cell in enumerate(row):
                if isinstance(cell, Atom) and cell == self.player.atom:
                    if y < len(new_matrix) - 1 and cell.check_move([cell]):
                        new_atom = Atom(cell.game, x, y + 1, cell.type)
                        new_atom.connections = cell.connections
                        new_matrix[y][x] = None
                        new_matrix[y + 1][x] = new_atom
                        new_player = Player(new_atom, self.player.game)
                        new_player.make_possible_connections(new_matrix)
                        return SokobondState(new_matrix, new_player)
        return None
    
    def move_left(self):
        new_matrix = [row[:] for row in self.matrix]
        for y, row in enumerate(new_matrix):
            for x, cell in enumerate(row):
                if isinstance(cell, Atom) and cell == self.player.atom:
                    if x > 0 and cell.check_move([cell]):
                        new_atom = Atom(cell.game, x - 1, y, cell.type)
                        new_atom.connections = cell.connections
                        new_matrix[y][x] = None
                        new_matrix[y][x - 1] = new_atom
                        new_player = Player(new_atom, self.player.game)
                        new_player.make_possible_connections(new_matrix)
                        return SokobondState(new_matrix, new_player)
        return None
    
    def move_right(self):
        new_matrix = [row[:] for row in self.matrix]
        for y, row in enumerate(new_matrix):
            for x, cell in enumerate(row):
                if isinstance(cell, Atom) and cell == self.player.atom:
                    if x < len(row) - 1 and cell.check_move([cell]):
                        new_atom = Atom(cell.game, x + 1, y, cell.type)
                        new_atom.connections = cell.connections
                        new_matrix[y][x] = None
                        new_matrix[y][x + 1] = new_atom
                        new_player = Player(new_atom, self.player.game)
                        new_player.make_possible_connections(new_matrix)
                        return SokobondState(new_matrix, new_player)
        return None
    
    def children_states(self):
        new_states = []
        if(self.move_up() != None):
            new_states.append(self.move_up())
        if(self.move_down() != None):
            new_states.append(self.move_down())
        if(self.move_left() != None):
            new_states.append(self.move_left())
        if(self.move_right() != None):
            new_states.append(self.move_right())
        return new_states
    
    def goal_state(self):
        for row in self.matrix:
            for cell in row:
                if isinstance(cell, Atom):
                    if len(cell.connections) < cell.n_connections:
                        return False
        return True
    