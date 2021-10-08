from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = self.set_name()

    def set_name(self):
        self.name = input('Please enter your name')
        print(self.name)
    def set_gesture(self):
<<<<<<< Updated upstream
        gesture_selection = input(int('which gesture would you like to choose?' + '\n' + 'press 1 for rock'+ '\n' + 'press 2 for paper' + '\n' + 'press 3 for scissors' + '\n' + 'press 4 for lizard' + '\n' + 'press 5 for spock'))
        if gesture_selection != 1 or self.gesture != 2 or self.gesture != 3 or self.gesture != 4 or self.gesture != 5:
            self.set_gesture(self)
        if gesture_selection == 1:
            self.gesture = self.gesture_list[0]
        if gesture_selection == 2:
            self.gesture = self.gesture_list[1]
        if gesture_selection == 3:
            self.gesture = self.gesture_list[2]
        if gesture_selection == 4:
            self.gesture = self.gesture_list[3]
        if gesture_selection == 5:
            self.gesture = self.gesture_list[4]
=======
        self.gesture= input(int('which gesture would you like to choose?' + '\n' + 'press 1 for rock'+ '\n' + 'press 2 for paper' + '\n' + 'press 3 for scissors' + '\n' + 'press 4 for lizard' + '\n' + 'press 5 for spock'))
        if self.gesture != 1 or self.gesture != 2 or self.gesture != 3 or self.gesture != 4 or self.gesture != 5:
            self.set_gesture
>>>>>>> Stashed changes
