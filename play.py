from game import PrisonersDilemma
from strategies import *

### Game parameters
rounds = 20
strategy1 = always_cooperate
strategy2 = always_defect

### Play the game
game = PrisonersDilemma(rounds, strategy1, strategy2)
strategy1_score, strategy2_score = game.play_game()
results = game.get_results()

### Return results
print("-" * 70)
print(f"Game:  {strategy1.__name__.upper().replace("_", " ")} vs {strategy2.__name__.upper().replace("_", " ")}")

print()
print()

print("Results per round:" + " " * 21 + "Strategy 1 | Strategy 2")
print("-" * 50 + "|" + "-" * 19)

cumulative_score1 = 0
cumulative_score2 = 0
for i, result in enumerate(results):
    strategy1_res, strategy2_res, score1, score2 = result
    cumulative_score1 += score1
    cumulative_score2 += score2
    print(f"Round {i+1:2}  : ({strategy1_res}, {strategy2_res}, {score1}, {score2})" + " " * 23 + f"{cumulative_score1:2} | {cumulative_score2:1}")

print()

if strategy1_score > strategy2_score:
    print(f"Winner: Player 1 with {strategy1.__name__.upper().replace("_", " ")} !!!")
elif strategy1_score < strategy2_score:
    print(f"Winner: Player 2 with {strategy2.__name__.upper().replace("_", " ")} !!!")
else:
    print("It's a tie!")

print("-" * 70)