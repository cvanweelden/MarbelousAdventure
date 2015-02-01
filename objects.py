from assets import sprites

class GameObject(object):
    def __init__(self, coords=(0,0), world=None, sprite=None):
        self.coords = coords
        self.world = world
        if sprite is None and hasattr(self,"default_sprite"):
            self.sprite = self.default_sprite
        else:
            self.sprite = sprite
    
    def setup(self):
        pass

    def update(self):
        pass

class Fence(GameObject):
    default_sprite = sprites["fence_hor"]
    
    def setup(self):
        i,j = self.coords
        fence_left = isinstance(self.world.get((i,j-1)),Fence)
        fence_right = isinstance(self.world.get((i,j+1)),Fence)
        fence_top = isinstance(self.world.get((i-1,j)),Fence)
        fence_bottom = isinstance(self.world.get((i+1,j)),Fence)

        if not (fence_left or fence_right) and (fence_bottom or fence_top):
            self.sprite = sprites["fence_ver"]

class Tree(GameObject):
    default_sprite = sprites["tree_top"]

    def setup(self):
        i,j = self.coords
        if not isinstance(self.world.get((i+1,j)),Tree):
            self.sprite = sprites["tree_trunk"]

class Goat(GameObject):
    default_sprite = sprites["goat"]

    def __init__(self, *args, **kwargs):
        self.following = False
        super(Goat,self).__init__(*args, **kwargs)

    def setup(self):
        #self.follow(self.world.player)
        pass

    def follow(self, obj):
        self.target = obj
        self.target_prev_coords = obj.coords
        self.following = True

    def update(self):
        if self.following:
            if self.target.coords != self.target_prev_coords:
                self.coords = self.target_prev_coords
                self.target_prev_coords = self.target.coords

class Princess(GameObject):
    default_sprite = sprites["princess"]

    def move(self, direction):
        i,j = self.coords
        if direction == 'l':
            target = (i,j-1)
        elif direction == 'r':
            target = (i,j+1)
        elif direction == 'u':
            target = (i-1,j)
        elif direction == 'd':
            target = (i+1,j)
        if self.world.get(target) is None and target[0] >= 0 and target[1] >= 0 and target[0] <= self.world.size[0] and target[1] <= self.world.size[1]:
            self.coords = target
            
    def checkforgoats(self):
    	i,j = self.coords
    	neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        for n in neighbors:
        	obj = self.world.get(n)
        	if obj.__class__ is Goat:
        		obj.follow(self)
    
    def update(self):
    	self.checkforgoats()
    	

    
