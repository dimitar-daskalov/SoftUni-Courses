from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count: int = 0
        self.cards: list = []

    def add(self, card: Card):
        card_needed = self.find(card.name)
        if card_needed:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if not card:
            raise ValueError("Card cannot be an empty string!")
        card_needed = self.find(card)
        if card_needed:
            self.cards.remove(card_needed)
            self.count -= 1

    def find(self, name: str):
        try:
            return [card for card in self.cards if card.name == name][0]
        except IndexError:
            pass
