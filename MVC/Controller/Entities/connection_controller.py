import pygame as pg
import sys
from MVC.Model.Entities.connection_model import Connection_Model

class Connection_Controller:

    def __init__(self, connection_model: Connection_Model):
        self.connection = connection_model
        
    def move(self, directon):
        if directon == "up":
            self.connection.y -= 1  

        elif directon == "down":
            self.connection.y += 1
            
        elif directon == "right":
            self.connection.x += 1
            
        elif directon == "left":
            self.connection.x -= 1
    