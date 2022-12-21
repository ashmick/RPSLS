from ai import Ai
class Player:
    
    def __init__(self, name) -> None:
        self.name=name
        self.gesture= ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        self.wins=0
        self.Gesture_chosen=""
        pass
    
    def game_greeting(self):
        print( "Welcome to the Rock, Paper, Scissors, Lizard, Spock game!")
        print("Prepare to have fun!")
        player_name=input("What is your name?")
        choice=print(f'{player_name} would you like to play against a Human or an AI?')
        if choice == "AI":
            print("Great, let's get this game started! Best of 3 wins!")
            
            pass
            
    def choose_an_opponent(self):      
        pass
    
        
    
    def choose_your_guesture(self):
        
        print(self.gesture)
        
        print("Which one do you want to choose")
        pass