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

| Strategy             | Description
|:---------------------|:--------------------------
| Always Cooperate     | Cooperates unconditionally.
| Always Defect        | Defects unconditionally.
| Random               | Chooses probabilistically.
| Tit for Tat          | Cooperates on the first round and imitates its opponent's previous move thereafter.
| Friedmann            | Cooperates until its opponent has defected once, and then defects for the rest of the game.
| Joss                 | Plays like TFT but defects every 10% of the time.
| Graaskamp            | Plays like TFT but defects in the 50th round.

## References

+ [Veritasium Video](https://youtu.be/mScpHTIi-kM?si=YPWhvPgj4how0AwX)
+ [Stanford on Prisoner’s Dilemma](https://plato.stanford.edu/entries/prisoner-dilemma/index.html#return)
+ [Stanford Strategies](https://plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html#:~:text=A%20good%20strategy%20for%20the,reduces%20the%20average%20payoff%20of)
