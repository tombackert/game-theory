# Repeated Prisoner's Dilemma

Repo for experimenting with the Repeated Prisoner's Dilemma game based on Robert Axelrod work.

#### Strategies implemented:
| Strategy             | Description
|:---------------------|:--------------------------
| Always Cooperate     | Cooperates unconditionally.
| Always Defect        | Defects unconditionally.
| Random               | Chooses probabilistically.
| Tit for Tat          | Cooperates on the first round and imitates its opponent's previous move thereafter.
| Friedmann            | Cooperates until its opponent has defected once, and then defects for the rest of the game.
| Joss                 | Plays like TFT but defects every 10% of the time.
| Graaskamp            | Plays like TFT but defects in the 50th round.

#### References:
- [Veritasium Video](https://youtu.be/mScpHTIi-kM?si=YPWhvPgj4how0AwX)
- [Stanford on Prisoner’s Dilemma](https://plato.stanford.edu/entries/prisoner-dilemma/index.html#return)
- [Stanford Strategies](https://plato.stanford.edu/entries/prisoner-dilemma/strategy-table.html#:~:text=A%20good%20strategy%20for%20the,reduces%20the%20average%20payoff%20of)
