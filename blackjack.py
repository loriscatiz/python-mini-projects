class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return(
"""
"""
        )
    

class Deck:

    suits = {'♥️', '♦️', '♣️', '♠️'}

    values = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
    }

    def __init__(self, card_stack: list[Card] = []):
        for i in range(1, 13):
            for suit in self.suits:
                card_stack.append(Card(suit, self.values[i]))

    
deck = Deck()