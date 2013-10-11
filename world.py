from assets import sprites
from objects import *

char2class = {"F": Fence,
        "G": Goat,
        "P": Princess,
        "T": Tree}

class World(object):
    """Object containing all information about the game world.
    """

    def __init__(self, size=(0,0), background=None):
        self.size = size
        self.background = background
        self.objects = []

    def setup(self):
        for obj in self.objects:
            obj.setup()

    def update(self):
        for obj in self.objects:
            obj.update()

    def load_level(self, level_file):
        self.player = None
        with open(level_file,'r') as f:
            for i,line in enumerate(f.readlines()):
                for j,char in enumerate(line.strip()):
                    if char != ".":
                        obj = char2class[char]((i,j),self)
                        self.objects.append(obj)
                        if char == "P":
                            self.player = obj
        self.size = (i,j)
        return self.player

    def get(self, coords):
        for obj in self.objects:
            if obj.coords == coords: return obj
        return None


