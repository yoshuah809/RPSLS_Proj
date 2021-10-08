from player import Player
class human(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = input('Please enter your name')
        print(self.name)
    def set_gesture(self):
        self.gesture= input(int('which gesture would you like to choose?' + '\n' + 'press 1 for rock'+ '\n' + 'press 2 for paper' + '\n' + 'press 3 for scissors' + '\n' + 'press 4 for lizard' + '\n' + 'press 5 for spock'))
        if self.gesture != 1 or self.gesture != 2 or self.gesture != 3 or self.gesture != 4 or self.gesture != 5:
            self.set_gesture
