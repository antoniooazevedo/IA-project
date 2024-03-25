import pygame as pg
import sys
from MVC.Model.Entities.connection_model import Connection_Model

class Connection_Controller:

    def __init__(self, connection_model: Connection_Model):
        self.connection = connection_model
        
    def move(self, x, y):
        self.connection.x = x
        self.connection.y = y
