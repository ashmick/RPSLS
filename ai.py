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
    
    def choose_a_gesture(self):
        self.gesture_chosen= random.choice(self.gestures)
        print(f'{self.name} has picked {self.gesture_chosen}')
        ai_choice=self.gesture_chosen
        
    pass
