
from human import Human
from ai import Ai
from player import Player

class Game:
    
    def __init__(self) -> None:
        
        self.player_one=None
        self.player_two=None
        pass
    
    def run_game(self):
        self.game_greeting()
        self.game_rules()
        self.choose_an_opponent()
        self.player_one.choose_a_gesture()
        
        pass

    def game_greeting(self):
        print( "Welcome to the Rock, Paper, Scissors, Lizard, Spock game!")
        print("Prepare to have fun!")
        
        
    def game_rules(self):
        print("The game is simple")
        pass
        
            
    def choose_an_opponent(self):   
        opponent_options= ["1","2"]
        player_choose_opponent=input("Press 1 for multiplayer or 2 to play against the computer?")   
        if player_choose_opponent in opponent_options:
            print("Great choice! Let's get started")
          
            
        if player_choose_opponent=="1":
            print("You will be playing against the computer! Good luck")
            
            # initialize ai
            self.player_one=Ai("Ashley")
            # self.player_one.choose_a_gesture()
            
            
        elif player_choose_opponent=="2":
            print("You will be playing a human!!")
            
            # initialize human
            self.player_one=Human("Missy")
            # self.player_one.choose_a_gesture() 

    
    


        pass
    