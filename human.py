from player import Player
class human(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name= input('please enter your name')
        print(self.name)