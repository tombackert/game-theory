class PrisonersDilemma:
    """Class to simulate a game of Prisoner's Dilemma"""
    def __init__(self, rounds, player1_strategy, player2_strategy):
        self.rounds = rounds
        self.strategy1 = player1_strategy
        self.strategy2 = player2_strategy
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
        player1_score = 0
        player2_score = 0
        for _ in range(self.rounds):
            strategy1 = self.strategy1()
            strategy2 = self.strategy2()
            score1, score2 = self.play_round(strategy1, strategy2)
            player1_score += score1
            player2_score += score2
            self.results.append((strategy1, strategy2, score1, score2))
        return player1_score, player2_score

    def get_results(self):
        return self.results