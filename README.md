# Strategic Game Equilibrium Analyzer

This is a small Python command line tool that analyzes a simple
two-player game using payoff matrices.

The program reads player payoffs from a file and finds:

- Dominant strategies
- Nash equilibrium points


---

## How to Run

```bash
python analyze_game.py prisoners.txt
```

## Example Input
```bash
# Player A payoff
3 0
5 1

# Player B payoff
3 5
0 1
```

## Example Output
```bash
Game Analysis

Dominant Strategy:
Player A: 1
Player B: 1

Nash Equilibrium:
(1, 1)
```


