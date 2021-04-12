from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count: int = 0
        self.players: list = []

    def add(self, player: Player):
        player_needed = self.find(player.username)
        if player_needed:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if not player:
            raise ValueError("Player cannot be an empty string!")
        player_needed = self.find(player)
        if player_needed:
            self.players.remove(player_needed)
            self.count -= 1

    def find(self, username: str):
        try:
            return [player for player in self.players if player.username == username][0]
        except IndexError:
            pass
