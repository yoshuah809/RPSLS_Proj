from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.set_name()

    def set_name(self):
        self.name = input('Please enter your name: ')
        print(f'{self.name} has been registered as a player!')
    def set_gesture(self):
        choose_gesture = input(f'which gesture would you like to choose {self.name}' + '\n' + 'press 1 for rock'+ '\n' + 'press 2 for paper' + '\n' + 'press 3 for scissors' + '\n' + 'press 4 for lizard' + '\n' + 'press 5 for spock' + '\n' + ' ')
        gesture_selection = int(choose_gesture)
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
        else:
            print('that is not an option please try again')
            self.set_gesture()
