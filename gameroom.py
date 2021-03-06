## This is going to be the GameRoom
from player import Player
from human import Human
from AI import AI


class Gameroom():
    def __init__(self):

        self.display_welcome()
        self.display_rules()
        self.select_game_mode()
        self.play_round()
         # Here the Player One Select the gesture
        # self.player_one.gesture = self.player_one.gesture_list[self.display_options()] 
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
    
    def play_round(self):
        this_round = 1
        while this_round <= 5:
            

            print(f'You are now starting round {this_round}')
            input('Please press enter to choose your gesture')
            self.player_one.set_gesture()
            self.player_two.set_gesture()
            if self.player_one.gesture == 'Rock':
                if self.player_two.gesture == 'Rock':
                    print('This round is a tie!')
                elif self.player_two.gesture =='Paper':
                    print(f'paper covers rock,{self.player_two.name} wins this round!')
                    self.player_two.score += 1
                elif self.player_two.gesture == 'Scissors':
                    print(f'rock smashes scissors, {self.player_one.name} wins this round')
                    self.player_one.score += 1
                elif self.player_two.gesture == 'Lizard':
                    print (f'rock smashes lizard, {self.player_one.name} wins this round')
                    self.player_one.score += 1
                else:
                    print (f'spock vaporizes rock, {self.player_two.name} wins this round')
                    self.player_two.score += 1



            elif self.player_one.gesture == 'Paper':
                if self.player_two.gesture == 'Paper':
                    print('this round is a tie!')
                elif self.player_two.gesture == 'Rock':
                    print (f'paper covers rock {self.player_one.name} wins this round!')
                    self.player_one.score += 1
                elif self.player_two.gesture == 'Scissors':
                    print(f'scissors cuts paper, {self.player_two.name} wins this round!')
                    self.player_two.score += 1
                elif self.player_two.gesture == 'Lizard':
                    print(f'lizard eats paper, {self.player_two.name} wins this round!')
                    self.player_two.score += 1
                else:
                    print(f'paper disproves spock, {self.player_one.name} wins this round!')
                    self.player_one.score += 1




            elif self.player_one.gesture == 'Scissors':
                if self.player_two.gesture == 'Scissors':
                    print('this round is a tie!')
                elif self.player_two.gesture == 'Rock':
                    print(f'rock smashes scissors {self.player_two.name} wins this round!')
                    self.player_two.score += 1
                elif self.player_two.gesture == 'Paper':
                    print(f'scissors cut paper {self.player_one.name} wins this round!')
                    self.player_one.score += 1
                elif self.player_two.gesture == 'Lizard':
                    print(f'scissors decapitates lizard {self.player_one.name} wins this round')
                    self.player_one.score += 1
                else:
                    print(f'spock smashes scissors, {self.player_two.name} wins this round!')
                    self.player_two.score += 1



            elif self.player_one.gesture == "Lizard":
                if self.player_two.gesture == 'Lizard':
                    print('this round is a tie!')
                elif self.player_two.gesture == 'Rock':
                    print(f'rock smashes lizard {self.player_two.name} wins this round!')
                    self.player_two.score += 1
                elif self.player_two.gesture == 'Paper':
                    print (f'lizard eats paper, {self.player_one.name} wins this round!')
                    self.player_one.score += 1
                elif self.player_two.gesture == 'Scissors':
                    print (f'scissors decapitates lizard, {self.player_two.name} wins this round!')
                    self.player_two.score += 1
                else:
                    print(f'lizard poisons spock, {self.player_one.name} wins this round!')
                    self.player_one.score += 1



            elif self.player_one.gesture == 'Spock':
                if self.player_two.gesture == 'Spock':
                    print('this round is a tie!')
                elif self.player_two.gesture == 'Rock':
                    print(f'spock vaporizes rock, {self.player_one.name} wins this round')
                    self.player_one.score += 1
                elif self.player_two.gesture == 'Paper':
                    print(f'paper disproves spock, {self.player_two.name} wins this round!')
                    self.player_two.score += 1
                elif self.player_two.gesture == 'Scissors':
                    print(f'spock smashes scissors, {self.player_one.name} wins thi round!')
                    self.player_one.score += 1
                else:
                    print(f'lizard poisons spock, {self.player_two.name} wins this round')
                    self.player_two.score += 1

            if self.player_one.score > 2:
                print(f"The Winner is {self.player_one.name}")
                break
            elif self.player_two.score > 2:
                print(f"The Winer is {self.player_two.name}")
                break
            elif this_round == 5 and self.player_one.score == self.player_two.score:
                print("This game is a tie, next score wins!")
                this_round = 4
                
            elif this_round == 5 and self.player_one.score > self.player_two.score:
                print(f'The winner is {self.player_one.name}')
                break
            elif this_round == 5 and self.player_one.score < self.player_two.score:
                print (f'The winner is {self.player_two.name}')
                break

            else:
                print('Stop trying to break my game!')    

            this_round += 1


            