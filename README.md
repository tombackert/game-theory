# Repeated Prisoner's Dilemma

Repo for experimenting with the Repeated Prisoner's Dilemma game based on Robert Axelrod work.

## Explaning the (Repeated) Prisoner's Dilemma

The Prisoner’s Dilemma is a classic game theory experiment with significant real-world applications. It involves two parties who must decide independently whether to cooperate or defect, with the following outcomes:

+ If both cooperate, both receive a moderate reward.
+ If one defects while the other cooperates, the defector receives a large reward while the cooperator gets nothing.
+ If both defect, both receive a minimal reward.

In the Repeated Prisoner’s Dilemma, this game is played multiple times, allowing players to adjust their strategies based on previous outcomes. This repetition introduces the possibility of strategies that consider the history of interactions, leading to more complex and nuanced decision-making.

### Real-World Applications

The Repeated Prisoner’s Dilemma models many real-world situations where individuals or groups interact repeatedly over time. Examples include:

+ Business Competition: Companies deciding between competing aggressively or cooperating through practices like price-fixing.
+ International Relations: Countries choosing between peaceful cooperation or hostile actions.
+ Social Behavior: Individuals in communities deciding whether to cooperate with others for mutual benefit or act selfishly.

Understanding the dynamics of the Repeated Prisoner’s Dilemma helps in analyzing and predicting behaviors in these scenarios, as well as in designing systems and policies that promote cooperative behavior.

### Importance of Understanding Strategies

Different strategies in the Repeated Prisoner’s Dilemma can significantly influence the outcomes of interactions. By studying these strategies, we can gain insights into:
  
+ Stability of Cooperation: What conditions foster long-term cooperative behavior?
+ Impact of Defection: How does a single act of defection affect future interactions?
+ Adaptability and Evolution: How do strategies evolve over time in response to the actions of others?

By analyzing the performance and interactions of these strategies, we can better understand the mechanisms that drive cooperative behavior and the factors that can disrupt it.

## Strategies implemented

| Strategy                   | Description
|:---------------------------|:--------------------------
| Always Cooperate           | Cooperates unconditionally.
| Always Defect              | Defects unconditionally.
| Random                     | Chooses probabilistically.
| Tit for Tat                | Cooperates on the first round and imitates its opponent's previous move thereafter.
| Friedmann                  | Cooperates until its opponent has defected once, and then defects for the rest of the game.
| Joss                       | Plays like TFT but defects every 10% of the time.
| Graaskamp                  | Plays like TFT but defects in the 50th round.
| Probability p Cooperator   | Cooperates with a probability p (example p=0.5).
| Suspicious Tit for Tat     | Defects on the first round and imitates its opponent's previous move thereafter.
| Generous Tit for Tat       | Plays like TFT but occasionally forgives defections.
| Gradual Tit for Tat        | Increases cooperation slowly after defections.
| Imperfect Tit for Tat      | Imitates opponent's last move with some probability of error.
| Tit for Two Tats           | Defects only after two consecutive defections by the opponent.
| Two Tits for Tat           | Defects twice after a single defection by the opponent.
| Omega Tit for Tat          | More complex version of TFT with additional rules.
| Grim Trigger               | Cooperates until the opponent defects once, then defects forever.
| Backstabber                | Cooperates for the first few rounds, then defects.
| Random Backstabber         | Cooperates for a random number of rounds, then defects.
| Periodic Defector          | Defects at regular intervals.
| Vindictive                 | Cooperates until the opponent defects once, then defects forever.
| Bullying                   | Defects initially, then cooperates if the opponent never defects.

## Leaderboard

Place      | Strategy                                 | Average score
-----------|------------------------------------------|-----------------------------------
1          | Imperfect Tit For Tat                    | 2529
2          | Generous Tit For Tat                     | 2496
3          | Omega Tit For Tat                        | 2435
4          | Tit For Two Tats                         | 2403
5          | Gradual Tit For Tat                      | 2347
6          | Tit For Tat                              | 2344
7          | Always Cooperate                         | 2332
8          | Grim Trigger                             | 2232
9          | Friedman                                 | 2229
10         | Vindictive                               | 2227
11         | Periodic Defector                        | 2040
12         | Random Strategy                          | 1965
13         | Graaskamp                                | 1959
14         | Two Tits For Tat                         | 1866
15         | Suspicious Tit For Tat                   | 1863
16         | Backstabber                              | 1744
17         | Random Backstabber                       | 1737
18         | Probability P Cooperator                 | 1726
19         | Joss                                     | 1590
20         | Bullying                                 | 1556
21         | Always Defect                            | 1546

![grafic](game-theory/average-score-per-strategy.png)

## References

+ [Veritasium Video](https://youtu.be/mScpHTIi-kM?si=YPWhvPgj4how0AwX)
+ [Stanford on Prisoner’s Dilemma](https://plato.stanford.edu/entries/prisoner-dilemma/index.html#return)
+ [Stanford Strategies](https://plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html#:~:text=A%20good%20strategy%20for%20the,reduces%20the%20average%20payoff%20of)
