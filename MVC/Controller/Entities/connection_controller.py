from MVC.Model.Entities.connection_model import Connection_Model

class Connection_Controller:
    """
    Class that represents the controller of a connection in the MVC pattern.    
    """
    def __init__(self, connection_model: Connection_Model):
        """
        Initializes a Connection_Controller object.
        
        Args:
            connection_model (Connection_Model): The model of the connection.
        """
        self.connection = connection_model

    def move(self, directon):
        """
        Updates the position of the connection in the given direction.
        
        Args:
            directon (str): The direction in which the connection should move.
        """
        if directon == "up":
            self.connection.y -= 1

        elif directon == "down":
            self.connection.y += 1

        elif directon == "right":
            self.connection.x += 1

        elif directon == "left":
            self.connection.x -= 1
