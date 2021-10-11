## This is going to be the GameRoom
from player import Player
from human import Human
from AI import AI


class Gameroom():
    def __init__(self):
        self.display_welcome()
        self.display_rules()
        self.select_game_mode()
         # Here the Player One Select the gesture
        self.player_one.gesture = self.player_one.gesture_list[self.display_options()] 
        # From here the machine takes the turn 
        #print(self.player_one.gesture) 

    def display_welcome(self):
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock, or RPSLS for short!')

        input('press the enter key to continue.')

    def display_rules(self):
        print ('I will now explain the rules of RPSLS.')
        print('you will be able to choose a one or two player game')
        print('you will have the ability to choose one of the five gestures.')
        print('If you have the winning gesture, you will be awarded a score point.')
        print('There is a total of five rounds. whoever scores the most points will win the game.')
        print('The winning combinations are as follows')
        print ('rock crushes scissors')
        print('scissors cut paper')
        print('paper covers rock')
        print('rock crushes lizard')
        print('lizard poisons spock')
        print('spock smashes scissors')
        print('scissors decapitates lizard')
        print('lizard eats paper')
        print('paper disproves spock')
        print('spock vaporizes rock')
        input('\n'+'\n'+'Once you have read and understand the rules, please hit the enter key')

    def select_game_mode(self):
        self.selected_option = int(input("Please select 1. for Player Vs Player or 2. For Player Vs Machine (Single Mode: ): ")) 
        if self.selected_option == 1:  #user has selected 2 Players
           self.player_one = Human()
           self.player_two = Human()
           print("You have selected Multiplayer Mode, Choose your gesture below...")
        
        elif self.selected_option == 2:    #user has selected Single mode
            self.player_one = Human()
            self.player_two = AI()
            print("You have selected Single player Mode")
        else:
            print("Plese select a Valid option, Press Enter to continue") 
            input('press the enter key to continue.') 
   

    def display_options(self):
        
        for gesture in range(len(self.player_one.gesture_list)):
            print(f'Please select {gesture} for {self.player_one.gesture_list[gesture]}')

        return_gesture = int(input())    
        return return_gesture  

    def compare_gesture():
        pass
    def pick_gesture():
        pass