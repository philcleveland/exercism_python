import random
from string import ascii_uppercase

class Robot:
    def __init__(self):
        self.name = self.create_name()

    def reset(self):
        self.name = self.create_name()

    def create_name(self):
        random.seed()
        letters = "".join([letter for letter in random.choices(ascii_uppercase, k=2)])        
        digits = "".join([str(digit) for digit in random.choices(range(1,9), k=3)])
        return letters+digits        