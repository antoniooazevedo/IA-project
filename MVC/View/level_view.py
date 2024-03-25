import pygame as pg
import sys

import scripts.utils as utils
from MVC.Model.level_model import Level_Model
from MVC.Model.Entities.atom_model import Atom_Model
from MVC.Model.Entities.molecule_model import Molecule_Model
from MVC.Model.Entities.wall_model import Wall_Model


class Level_View:
    def __init__(self, level_model: Level_Model, screen):
        self.model = level_model
        self.screen = screen
        self.assets = self.load_assets()
        
    def load_assets(self):
        assets = {}
        for molecule in self.model.molecules:
            for atom in molecule.molecule.keys():
                if atom.image_path not in assets:
                    image = pg.image.load(atom.image_path)
                    scaled_image = pg.transform.scale(image, (60, 60))
                    assets[atom.image_path] = scaled_image
                
                electron_image_path = self.get_electron_image_path(atom)
                if electron_image_path not in assets:
                    electron_image = pg.image.load(electron_image_path).convert()
                    electron_image.set_colorkey((255, 255, 255))
                    scaled_electron_image = pg.transform.scale(electron_image, (60, 60))
                    assets[electron_image_path] = scaled_electron_image

        for row in self.model.matrix:
            for entity in row:
                if isinstance(entity, Wall_Model) and entity.image_path not in assets:
                    image = pg.image.load(entity.image_path)
                    scaled_image = pg.transform.scale(image, (60, 60))
                    assets[entity.image_path] = scaled_image
        return assets

    def draw(self):
        self.screen.fill((255, 255, 255))
        for row in self.model.matrix:
            for entity in row:
                if entity is not None:
                    self.draw_entity(entity)

    def get_electron_image_path(self, atom):
        return f"assets/images/{atom.electrons}-con.png"

    def draw_entity(self, entity):
        if isinstance(entity, Molecule_Model):
            for atom in entity.molecule.keys():
                image = self.assets[atom.image_path]
                pos_x = atom.x * 60 + 130
                pos_y = atom.y * 60
                self.screen.blit(image, (pos_x, pos_y))

                electron_image_path = self.get_electron_image_path(atom)
                electron_image = self.assets[electron_image_path]
                self.screen.blit(electron_image, (pos_x, pos_y))
        elif isinstance(entity, Wall_Model):
            image = self.assets[entity.image_path]
            self.screen.blit(image, (entity.x * 60 + 130, entity.y * 60))