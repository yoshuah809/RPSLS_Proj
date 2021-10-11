import random
from player import Player


class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = "Artificial Human"
        self.gesture = None

    def set_gesture(self):
        gesture_selection = random.randint(0,4)
        if gesture_selection == 0:
            self.gesture = self.gesture_list[0]
        if gesture_selection == 1:
            self.gesture = self.gesture_list[1]
        if gesture_selection == 2:
            self.gesture = self.gesture_list[2]
        if gesture_selection == 3:
            self.gesture = self.gesture_list[3]
        if gesture_selection == 4:
            self.gesture = self.gesture_list[4]
