
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
        self.play_out_gestures()
        
        pass

    def game_greeting(self):
        print( "Welcome to the Rock, Paper, Scissors, Lizard, Spock game!")
        print("Prepare to have fun!")
        
        
    def game_rules(self):
        print("The game is simple")
        pass
        
            
    def choose_an_opponent(self):   
        opponent_options= ["1","2","3"]
        player_choose_opponent=input("How many players? Press 1, 2, or 3 for a surprise. ")   
        if player_choose_opponent in opponent_options:
            print("Great choice! Let's get started")
          
            
        if player_choose_opponent=="1":
            print("You will be playing against the computer! Good luck")
            
            # initialize ai

            self.player_one=Human("Ashley")
            
            self.player_two=Ai("Computer")

            
            # self.player_one.choose_a_gesture()
            
            
        elif player_choose_opponent=="2":
            print("You will be playing a human!!")
            
            # initialize human
            self.player_one=Human("Missy")
            self.player_two=Human("Cheryl")
            # self.player_one.choose_a_gesture() 
        
        elif player_choose_opponent=="3":
            print("Get ready for the battle of the robots")
            
            self.player_one=Ai("Computer 1")
            self.player_two=Ai("Computer 2")
            pass
    
    def play_out_gestures (self):
        self.wins=3
        while self.wins>0:
            self.player_one.choose_a_gesture()
            self.player_two.choose_a_gesture()
            # self.determine_winner(player_one_choice, player_two_choice)
            self.player_wins-=1
            
        
    # def determine_winner(self,player_one_choice, player_two_choice):
    #     if human_choice == 0 and ai_choice == "Scissors" or ai_choice == "Lizard":
    #         print("Player wins.")
    #         player_wins = player_wins.append(1) 
    #     elif human_choice == 1 and ai_choice == "Rock" or ai_choice == "Spock":
    #         print("Player wins.")
    #         playerWins = playerWins.append(1) 
    #     elif human_choice == 2 and ai_choice == "Paper" or ai_choice == "Lizard":
    #         print("Player wins.")
    #         playerWins = playerWins.append(1) 
    #     elif human_choice == 3 and ai_choice == "Spock" or ai_choice == "Paper":
    #         print("Player wins.")
    #         playerWins = playerWins.append(1)
    #     elif human_choice== 4 and ai_choice == "Scissor" or ai_choice == "Rock":
    #         print("Player wins.")
    #         playerWins = playerWins.append(1)
    #     elif human_choice == ai_choice:
    #         print("Tie")
    #         ties = ties.append(1)
    #     else:
    #         pass