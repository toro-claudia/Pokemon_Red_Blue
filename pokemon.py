from moves import Move


class Pokemon:
    def __init__(self, name, poke_type, level=5, moves=None):
        self.name = name
        self.poke_type = poke_type
        self.level = level
        self.health = level * 10
        
        if moves: # if user provided moves
            self.moves = moves
        else:
            self.moves = []
    
    def info(self):
        return f"{self.name} ({self.poke_type} type) - Level {self.level}, HP: {self.health}"

    # H
    def take_damage(self, amount): 
        self.health -= amount
        if self.health < 0:
            self.health = 0
    
    def attack(self, other, move):
        print(f"{self.name} uses {move.name} on {other.name}!")
        other.take_damage(move.damage)
