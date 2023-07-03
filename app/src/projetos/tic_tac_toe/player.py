import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
        
    def get_move(self, game):
        pass
        
class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
            
    def move(self, game):
        pass
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        pass    
        