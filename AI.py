import random
from player import Player


class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = "Artificial Human"
        self.gesture = None

    def set_gesture(self):
        self.gesture = self.gesture_list[random.randint(0,4)]
        
