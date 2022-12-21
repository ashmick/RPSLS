from player import Player
import random

class Ai(Player):

    def __init__(self,name):    
        super().__init__(name)
        # self.name=name
        # self.gesture= ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        # self.wins=0
        # self.Gesture_chosen=""
        pass
    
    def choose_a_guesture(self):
        self.choose_your_guesture= random.choice(self.gesture)
        print(f'{self.name} has picked {self.Gesture_chosen}')
    pass
