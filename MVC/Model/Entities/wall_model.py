class Wall_Model:
    """
    Class that represents a wall in the game.
    
    It is responsible for storing the position of the wall and the image path.
    """
    
    def __init__(self, x, y, image_path=""):
        """
        Initializes a Wall_Model object.
        
        Args:
            x (int): The x position of the wall.
            y (int): The y position of the wall.
            image_path (str): The path to the image of the wall.
        """
        self.x = x
        self.y = y
        self.image_path = image_path

    def __str__(self):
        """
        Returns a string representation of the Wall_Model object.
    
        Returns:
            str: A string representation of the Wall_Model object.    
        """
        return f"Wall_Model({self.x}, {self.y})"
