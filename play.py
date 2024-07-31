from game import PrisonersDilemma
from strategies import *

### Game parameters
rounds = 10
player1_strategy = always_cooperate
player2_strategy = always_defect

### Play the game
game = PrisonersDilemma(rounds, player1_strategy, player2_strategy)
player1_score, player2_score = game.play_game()
results = game.get_results()

### Return results
print(f'Player 1 Score: {player1_score}')
print(f'Player 2 Score: {player2_score}')
print('Results per round:')
for result in results:
    print(result)