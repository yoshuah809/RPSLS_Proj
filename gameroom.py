## This is going to be the GameRoom
from player import Player
from human import Human
from AI import AI


class Gameroom():
    def __init__(self):
        self.player = Human()
        self.computer = AI()

    def display_welcome():
        print('welcom to Rock, Paper, Scissors, Lizard, Spock, or RPSLS for short!')
        input('press the enter key to continue.')

    def display_rules():
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

    def select_game_mode():
        pass

    def pick_gesture():
        pass

    def display_options():
        pass

    def compare_gesture():
        pass

    def select_game_mode():
        pass