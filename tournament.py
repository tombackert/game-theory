from game import PrisonersDilemma
from strategies import *
import matplotlib.pyplot as plt
import numpy as np

# Define the number of rounds
rounds = 1000

# Define the strategies
strategy_list = [
    always_cooperate,
    always_defect,
    tit_for_tat,
    friedman,
    joss,
    graaskamp,
    random_strategy,
    probability_p_cooperator,
    suspicious_tit_for_tat,
    generous_tit_for_tat,
    gradual_tit_for_tat,
    imperfect_tit_for_tat,
    tit_for_two_tats,
    two_tits_for_tat,
    omega_tit_for_tat,
    grim_trigger,
    backstabber,
    random_backstabber,
    periodic_defector,
    vindictive,
    bullying
]

# Function to get the strategy name
def get_strategy_name(strategy_func):
    return strategy_func.__name__.replace('_', ' ').title()

# Run the tournament
results_summary = []

for i, strategy1 in enumerate(strategy_list):
    for j, strategy2 in enumerate(strategy_list):
        game = PrisonersDilemma(rounds, strategy1, strategy2)
        strategy1_score, strategy2_score, results = game.play_game()

        # Document the results
        strategy1_name = get_strategy_name(strategy1)
        strategy2_name = get_strategy_name(strategy2)
        results_summary.append((strategy1_name, strategy1_score, strategy2_name, strategy2_score))

# Print summary of all matches
print()
print("Summary of all matches:")
print()
print(f"{'Strategy 1':<24} | {'Score':<7} | {'Strategy 2':<24} | {'Score':<7}")
print("-" * 24 + "-|-" + "-" * 7 + "-|-" + "-" * 24 + "-|-" + "-" * 7)
for match in results_summary:
    print(f"{match[0]:<24} | {match[1]:<7} | {match[2]:<24} | {match[3]:<7}")

print("-"*90)


# Get values for each strategy
results_per_strategy = {get_strategy_name(strategy): [] for strategy in strategy_list}

for strategy, value, _, _ in results_summary:
    if strategy in results_per_strategy:
        results_per_strategy[strategy].append(value)

average_score_per_strategy = {strategy: sum(results_per_strategy[strategy]) / len(results_per_strategy[strategy]) for strategy in results_per_strategy}

# Sort the strategies by average score
average_score_per_strategy = dict(sorted(average_score_per_strategy.items(), key=lambda item: item[1], reverse=True))

# Plot the average scores
print("Average scores per strategy:")
print()

print(f"{'Place':<10} | {'Strategy':<40} | {'Average score':<30}")
print("-" * 10 + "-|-" + "-" * 40 + "-|-" + "-" * 34)
for index, strategy in enumerate(average_score_per_strategy, start=1):
    print(f"{index:<10} | {strategy:<40} | {round(average_score_per_strategy[strategy]):<30}")

print()
print()


# Visualization with colored bars
strategies = list(average_score_per_strategy.keys())
scores = list(average_score_per_strategy.values())

colors = plt.cm.viridis(np.linspace(0, 1, len(strategies)))

plt.figure(figsize=(14, 8))
bars = plt.barh(strategies, scores, color=colors)
plt.xlabel('Average Score')
plt.ylabel('Strategy')
plt.title('Average Score per Strategy in Repeated Prisoner\'s Dilemma')
plt.gca().invert_yaxis()  # To display the highest score at the top

# Adding score labels to each bar
for bar, score in zip(bars, scores):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{round(score):}', va='center')

plt.show()