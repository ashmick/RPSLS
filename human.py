from player import Player
class Human(Player):
    
    def __init__(self, name):
        super().__init__(name)
        # self.name=name
        # self.gesture= ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        # self.wins=0
        # self.Gesture_chosen=""
    
    def choose_your_guesture(self):
        human_choices=["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        print(f' Your choices are {human_choices}. ')
        input("Choose 0 for Rock, 1 for Paper, 2 for Scissor, 3 for Lizard, 4 for Spock")      
        
        
    pass