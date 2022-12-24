
class Player:
    
    def __init__(self, name) -> None:
        self.name=name
        self.gestures= ["Rock", "Paper", "Scissor", "Lizard", "Spock"]
        self.wins=0
        self.gestures_chosen=""
        pass
    
    
    
    def choose_a_gesture(self):
        for gesture in self.gestures:
            player_picked=input(f'What do you choose? {gesture} Press 0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock')
        print(f'You picked {player_picked}')
        pass