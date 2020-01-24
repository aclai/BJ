import person

class Dealer(person.Person):
    def __init__(self, game):
        self.game = game
        self.hand = []
        self.hand_value = []