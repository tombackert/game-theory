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