from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players_list = []

    def assign_player(self, player):
        if player in self.players_list:
            return f"Player {player.name} is already in the guild."
        elif player not in self.players_list and not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        player.guild = self.name
        self.players_list.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name not in [player.name for player in self.players_list]:
            return f"Player {player_name} is not in the guild."
        current_player = [p for p in self.players_list if p.name == player_name][0]
        self.players_list.remove(current_player)
        current_player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.players_list:
            result += p.player_info()

        return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
