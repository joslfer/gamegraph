# GameGraph

> 🚧 Under construction

Evolutionary Game Theory on Networks. 

Simulation of the Prisoner's Dilemma in evolving populations.

The project starts with a fully connected population where each agent plays against every other agent.

Future versions will include networks.

## Current Features

- Prisoner's Dilemma implementation
- Population payoff computation
- Evolution using Replicator Dynamics
- Evolution of cooperation over generations
- Strategy proportion plot

## Project Structure

```text
gamegraph/
├── cuadernos/
│   └── 01_prisoner_dilemma.ipynb
├── images/
│   └── replicatordynamics.png
├── src/
│   └── games/
│       ├── __init__.py
│       └── prisoners_dilemma.py
├── LICENSE
└── README.md
```


## Results 

The simulation converges to an all-defector population, as predicted by the Nash equilibrium of the Prisoner's Dilemma. 


![replicator dynamics](images/replicatordynamics.png)