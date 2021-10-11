from player import Player

class Human(Player):
    def __init__(self):
        self.name = self.set_name()
        super().__init__()

    def set_name(self):
        self.name = input('Please enter your name: ')
        print(self.name)
    def set_gesture(self):
        choose_gesture = input('which gesture would you like to choose?' + '\n' + 'press 1 for rock'+ '\n' + 'press 2 for paper' + '\n' + 'press 3 for scissors' + '\n' + 'press 4 for lizard' + '\n' + 'press 5 for spock' + '\n' + ' ')
        gesture_selection = int(choose_gesture)
        # for gesture in range(len(self.player_one.gesture_list)):
        #     print(f'Please select {gesture} for {self.player_one.gesture_list[gesture]}')
        if gesture_selection == 1:
            self.gesture = self.gesture_list[0]
        elif gesture_selection == 2:
            self.gesture = self.gesture_list[1]
        elif gesture_selection == 3:
            self.gesture = self.gesture_list[2]
        elif gesture_selection == 4:
            self.gesture = self.gesture_list[3]
        elif gesture_selection == 5:
            self.gesture = self.gesture_list[4]
        # self.gesture= input(int('which gesture would you like to choose?' + '\n' + 'press 1 for rock'+ '\n' + 'press 2 for paper' + '\n' + 'press 3 for scissors' + '\n' + 'press 4 for lizard' + '\n' + 'press 5 for spock'))
        else:
            self.set_gesture 
