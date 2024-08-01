import game
import random

"""
List of strategies for the Repeated Prisoner's Dilemma
"""

def always_cooperate(results, player_index):
    return 'C'

def always_defect(results, player_index):
    return 'D'

def tit_for_tat(results, player_index):
    if not results:
        return 'C'
    else:
        opponents_last_move = results[-1][1 - player_index]
        return opponents_last_move

def friedman(results, player_index):
    for result in results:
        if result[1 - player_index] == 'D':
            return 'D'
    return 'C'
    
def random_strategy(results, player_index):
    return random.choice(['C', 'D'])

def joss(results, player_index):
    if not results:
        return 'C'
    else:
        opponents_last_move = results[-1][1 - player_index]
        if random.random() < 0.1:
            return 'D'
        return opponents_last_move
    
def graaskamp(results, player_index):
    round_number = len(results) + 1
    if not results:
        return 'C'
    else:
        opponents_last_move = results[-1][1 - player_index]
        if round_number == 50:
            return 'D'
        return opponents_last_move
    
def probability_p_cooperator(results, player_index):
    p = 0.25
    return 'C' if random.random() < p else 'D'

def suspicious_tit_for_tat(results, player_index):
    if not results:
        return 'D'
    else:
        opponents_last_move = results[-1][1 - player_index]
        return opponents_last_move

def generous_tit_for_tat(results, player_index):
    if not results:
        return 'C'
    else:
        opponents_last_move = results[-1][1 - player_index]
        if opponents_last_move == 'D':
            return 'C' if random.random() < 0.33 else 'D'  # Example generosity parameter
        return 'C'

def gradual_tit_for_tat(results, player_index):
    if not results:
        return 'C'
    defection_count = 0
    for result in results:
        if result[1 - player_index] == 'D':
            defection_count += 1
    if defection_count == 0:
        return 'C'
    elif results[-1][1 - player_index] == 'D':
        return 'D'
    return 'C'

def imperfect_tit_for_tat(results, player_index):
    if not results:
        return 'C'
    opponents_last_move = results[-1][1 - player_index]
    return opponents_last_move if random.random() < 0.9 else 'C'

def tit_for_two_tats(results, player_index):
    if len(results) < 2:
        return 'C'
    if results[-1][1 - player_index] == 'D' and results[-2][1 - player_index] == 'D':
        return 'D'
    return 'C'

def two_tits_for_tat(results, player_index):
    if not results:
        return 'D'
    if results[-1][1 - player_index] == 'D':
        return 'D'
    return 'C'

def omega_tit_for_tat(results, player_index):
    deadlock_threshold = 3
    randomness_threshold = 5
    defection_streak = 0
    cooperation_streak = 0
    for result in results:
        if result[1 - player_index] == 'D':
            defection_streak += 1
            cooperation_streak = 0
        else:
            cooperation_streak += 1
            defection_streak = 0
        if defection_streak >= randomness_threshold:
            return 'D'
        if cooperation_streak >= deadlock_threshold:
            return 'C'
    return 'C'

def grim_trigger(results, player_index):
    for result in results:
        if result[1 - player_index] == 'D':
            return 'D'
    return 'C'

###

def backstabber(results, player_index):
    if len(results) < 5:
        return 'C'
    return 'D'

def random_backstabber(results, player_index):
    if len(results) < random.randint(1, 10):
        return 'C'
    return 'D'

def periodic_defector(results, player_index):
    if len(results) % 3 == 0:
        return 'D'
    return 'C'

def vindictive(results, player_index):
    for result in results:
        if result[1 - player_index] == 'D':
            return 'D'
    return 'C'

def bullying(results, player_index):
    if len(results) < 3:
        return 'D'
    return 'C' if results[-1][1 - player_index] == 'C' else 'D'