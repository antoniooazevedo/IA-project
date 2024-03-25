import pygame as pg
import sys
from MVC.Model.Entities.connection_model import ConnectionModel

class ConnectionController:

    def __init__(self, connection_model: ConnectionModel):
        self.connection = connection_model
        
    def move(self, x, y):
        self.connection.x = x
        self.connection.y = y
