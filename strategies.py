import game
### Strategies

### Basic Strategies
def always_cooperate(results, player_index):
    return 'C'

def always_defect(results, player_index):
    return 'D'

### Best Strategy
def tit_for_tat(results, player_index):
    if not results:
        return 'C'
    else:
        last_opponent_strategy = results[-1][1 - player_index]
        return last_opponent_strategy
