from player import Player

class Human(Player):
    
    def __init__(self, name):
        super().__init__(name)
        # self.name=name
        # self.gesture= ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        # self.wins=0
        # self.Gesture_chosen=""
    
    def choose_a_gesture(self):
        self.wins=3
           
        while self.wins>0:
            human_options= ["0", "1","2","3","4"]
            human_choices=input("Choose 0 for Rock, 1 for Paper, 2 for Scissor, 3 for Lizard, 4 for Spock")         
            if human_choices in human_options:
                print(f'You chose option {human_choices} which is {self.gestures[int(human_choices)]}')
                self.wins-=1
        
        
                
                
            
                    
               
            
        # create while loop
        pass