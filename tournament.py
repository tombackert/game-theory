from game import PrisonersDilemma
import strategies as strat
import matplotlib.pyplot as plt

# Define the number of rounds
rounds = 200

# Define the strategies
strategy_list = [
    strat.always_cooperate,
    strat.always_defect,
    strat.tit_for_tat,
    strat.friedman,
    strat.joss,
    strat.graaskamp,
    strat.random_strategy
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
print("#"*90)
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

print(f"{'Place':<10} | {'Strategy':<20} | {'Average score':<20}")
print("-" * 10 + "-|-" + "-" * 20 + "-|-" + "-" * 20)
for index, strategy in enumerate(average_score_per_strategy, start=1):
    print(f"{index:<10} | {strategy:<20} | {round(average_score_per_strategy[strategy]):<20}")

print()
print("#"*90)