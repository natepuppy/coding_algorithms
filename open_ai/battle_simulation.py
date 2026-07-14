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
    def __init__(self, a_monsters, b_monsters):
        self.a_monsters = deque(a_monsters)
        self.b_monsters = deque(b_monsters)
        self.remaining_a = len(a_monsters)
        self.remaining_b = len(b_monsters)
        self.logs = []

    def play(self):
        self.logs.append("Match Started: Team A vs Team B")

        while self.winner() is None:
            a_monster = self.a_monsters[0]
            b_monster = self.b_monsters[0]

            self.logs.append(f"Round: {a_monster['name']} vs {b_monster['name']}")

            a_is_killing_strike = self.attack(a_monster, b_monster)
            if a_is_killing_strike:
                self.remaining_b -= 1
                self.b_monsters.popleft()
            
            self.logs.append(f"{a_monster['name']} attacks {b_monster['name']} for {a_monster['power']} damage. {b_monster['name']} HP: {b_monster['hp']}")

            b_is_killing_strike = self.attack(b_monster, a_monster)
            if b_is_killing_strike:
                self.remaining_a -= 1
                self.a_monsters.popleft()

            # Change: Checked if Team B was killed this turn to inject the [dying strike] text
            action_text = "executes a [dying strike] counterattack!" if a_is_killing_strike else "attacks"
            self.logs.append(f"{b_monster['name']} {action_text} {a_monster['name']} for {b_monster['power']} damage. {a_monster['name']} HP: {a_monster['hp']}")

            if a_is_killing_strike:
                self.logs.append(f"{b_monster['name']} has been eliminated")

            if b_is_killing_strike:
                self.logs.append(f"{a_monster['name']} has been eliminated")

        winner = self.winner()

        if winner == "Draw":
            self.logs.append("Draw!")
        else:
            self.logs.append(f"{winner} wins the Match!")

        return {
            "winner": winner,
            "logs": self.logs
        }
    
    def attack(self, attacker, defender):
        defender['hp'] -= attacker['power']
        if defender['hp'] <= 0:
            return True
        return False

    def winner(self):
        if self.remaining_a > 0 and self.remaining_b > 0:
            return None
        elif self.remaining_a <= 0 and self.remaining_b <= 0:
            return "Draw"
        elif self.remaining_b <= 0:
            return "Team A"
        elif self.remaining_a <= 0:
            return "Team B"

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