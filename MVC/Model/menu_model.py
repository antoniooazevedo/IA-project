import pygame as pg

class Menu_Model:
    def __init__(self, options, bigText, bigFont, optionsFont):
        self.options = options
        self.optionsFont = optionsFont
        self.bigText = bigText
        self.bigFont = bigFont
        self.selected = 0
    
        