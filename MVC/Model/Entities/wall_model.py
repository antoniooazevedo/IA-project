class Wall_Model:
    def __init__(self, x, y, image_path=""):
        self.x = x
        self.y = y
        self.image_path = image_path

    def __str__(self):
        return f"Wall_Model({self.x}, {self.y})"
