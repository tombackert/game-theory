class PrisonersDilemma:
    """Class to simulate a game of Prisoner's Dilemma"""
    def __init__(self, rounds, strategy1, strategy2):
        self.rounds = rounds
        self.strategy1 = strategy1
        self.strategy2 = strategy2
        self.results = []

    def play_round(self, strategy1, strategy2):
        if strategy1 == 'C' and strategy2 == 'C':
            return (3, 3)
        elif strategy1 == 'D' and strategy2 == 'D':
            return (1, 1)
        elif strategy1 == 'D' and strategy2 == 'C':
            return (5, 0)
        elif strategy1 == 'C' and strategy2 == 'D':
            return (0, 5)

    def play_game(self):
        strategy1_score = 0
        strategy2_score = 0
        for _ in range(self.rounds):
            strategy1 = self.strategy1(self.results, 0)
            strategy2 = self.strategy2(self.results, 1)
            score1, score2 = self.play_round(strategy1, strategy2)
            strategy1_score += score1
            strategy2_score += score2
            self.results.append((strategy1, strategy2, score1, score2))
        return strategy1_score, strategy2_score, self.results