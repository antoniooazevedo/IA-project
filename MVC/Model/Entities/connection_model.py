class Connection_Model:
    """
    Class that represents a connection between two atoms in the game.
    
    It is responsible for storing the position of the connection and the direction of the connection.
    """
    def __init__(self, x, y, direction):
        """
        Initializes a Connection_Model object.
        
        Args:
            x (int): The x position of the connection.
            y (int): The y position of the connection.
            direction (str): The direction of the connection (up, down, left, right).
        """
        self.x = x
        self.y = y
        self.direction = direction

    def __str__(self):
        """
        Returns a string representation of the Connection_Model object.
        
        Returns:
            str: A string representation of the Connection_Model object.
        """
        if self.direction == "up" or self.direction == "down":
            return "|"

        elif self.direction == "left" or self.direction == "right":
            return "-"

    def __eq__(self, other):
        """
        Compares two Connection_Model objects.
        
        Args:
            other (Connection_Model): The other Connection_Model object to compare.
            
        Returns:
            bool: True if the two Connection_Model objects are equal, False otherwise.
        """
        if isinstance(other, self.__class__):
            return (
                self.x == other.x
                and self.y == other.y
                and self.direction == other.direction
            )
        else:
            return False
