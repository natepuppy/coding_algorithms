# Implement a turn-based battle simulator between two teams of monsters.

# Each team starts with a queue of monsters. A monster has a name, hp, and 
# power. During each round, the front monster from each team attacks the 
# other. Team A's monster attacks first, reducing Team B's monster's HP 
# by its power. Even if this attack reduces Team B's monster's HP to 0 
# or below, it still gets one final dying strike and attacks back before 
# being removed. After both attacks, any monster with HP ≤ 0 is eliminated 
# and removed from the front of its team's queue. The battle continues until 
# one or both teams have no monsters remaining. Return the winner 
# ("Team A", "Team B", or "Draw") along with a log of the battle.


from collections import deque

class Game:
    def __init__(self, team_a, team_b):
        self.team_a = deque(team_a)
        self.team_b = deque(team_b)
        self.logs = []

    def play(self):
        self.logs.append("Match Started: Team A vs Team B")

        while self.team_a and self.team_b:
            a = self.team_a[0]
            b = self.team_b[0]

            self.logs.append(f"Round: {a['name']} vs {b['name']}")

            # Team A attacks
            b["hp"] -= a["power"]
            a_killed = b["hp"] <= 0
            self.logs.append(
                f"{a['name']} attacks {b['name']} for {a['power']} damage. {b['name']} HP: {b['hp']}"
            )

            # Team B always gets a counterattack
            a["hp"] -= b["power"]
            b_killed = a["hp"] <= 0

            action = "uses a dying strike on" if a_killed else "attacks"
            self.logs.append(
                f"{b['name']} {action} {a['name']} for {b['power']} damage. {a['name']} HP: {a['hp']}"
            )

            if a_killed:
                self.team_b.popleft()
                self.logs.append(f"{b['name']} has been eliminated")

            if b_killed:
                self.team_a.popleft()
                self.logs.append(f"{a['name']} has been eliminated")

        winner = self.winner()
        self.logs.append("Draw!" if winner == "Draw" else f"{winner} wins!")

        return {"winner": winner, "logs": self.logs}

    def winner(self):
        if self.team_a and self.team_b:
            return None
        if not self.team_a and not self.team_b:
            return "Draw"
        return "Team A" if self.team_a else "Team B"

if __name__ == "__main__":
    a_monsters = [
        {
            'name': "Nathan",
            'hp': 20,
            'power': 10
        }
    ]

    b_monsters = [
        {
            'name': "Nathan",
            'hp': 20,
            'power': 10
        }
    ]

    print(Game(a_monsters, b_monsters).play())