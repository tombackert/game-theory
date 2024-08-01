from game import PrisonersDilemma
from strategies import *

### Game parameters
rounds = 200
strategy1 = random_strategy
strategy2 = joss


### Play the game
game = PrisonersDilemma(rounds, strategy1, strategy2)
strategy1_score, strategy2_score, results = game.play_game()


### Return results to the console in a nice format
print("-" * 72)
print(f"Game:  {strategy1.__name__.upper().replace("_", " ")} vs {strategy2.__name__.upper().replace("_", " ")}")

print()
print()

print("Results per round:" + " " * 23 + "Strategy 1 | Strategy 2")
print("-" * 52 + "|" + "-" * 19)

cumulative_score1 = 0
cumulative_score2 = 0
for i, result in enumerate(results):
    strategy1_res, strategy2_res, score1, score2 = result
    cumulative_score1 += score1
    cumulative_score2 += score2
    print(f"Round {i+1:3}  : ({strategy1_res}, {strategy2_res}, {score1}, {score2})" + " " * 23 + f"{cumulative_score1:3} | {cumulative_score2:1}")

print()

if strategy1_score > strategy2_score:
    print(f"Winner: {strategy1.__name__.upper().replace("_", " ")} !!!")
elif strategy1_score < strategy2_score:
    print(f"Winner: {strategy2.__name__.upper().replace("_", " ")} !!!")
else:
    print("It's a tie!")

print("-" * 72)