from player import Player

class Human(Player):
    
    def __init__(self, name):
        super().__init__(name)
        # self.name=name
        # self.gesture= ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        # self.wins=0
        # self.Gesture_chosen=""
    
    def choose_a_gesture(self,player_one_choice):
        # self.wins=3
           
        # while human_choices in human_options:
        # human_options= ["0", "1","2","3","4"]
        =input("Choose 0 for Rock, 1 for Paper, 2 for Scissor, 3 for Lizard, 4 for Spock")      
        print(f'You chose option {human_choices} which is {self.gestures[int(human_choices)]}')
        if human_choices==0:
            human_choices= "Rock"
        elif human_choices ==1:
            human_choices= "Paper"
        elif human_choices == 2:
            human_choices= "Scissors"
        elif human_choices==3:
            human_choices="Lizard"
        elif human_choices==4:
            human_choices= "Spock"
        else:                     
            print("Please choose another name.")
                
        return human_choices

            
            
            # if self.wins>0:
                # self.wins-=1
        
        # while self.dinosaur.health > 0 and self.robot.health > 0:
        #     self.robot.attack(self.dinosaur)
        #     if self.dinosaur.health>0:
        #         self.dinosaur.attack(self.robot)
            
                
                
            
                    
               
            
        # create while loop
        pass