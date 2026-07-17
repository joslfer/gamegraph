# Prisoner's Dilemma payoff function

import numpy as np 
import networkx as nx
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

T = 5  # Temptation: payoff for defecting while the other cooperates
R = 3  # Reward: payoff when both cooperate
P = 1  # Punishment: payoff when both defect
S = 0  # Sucker: payoff for cooperating while the other defects

payoffs = {
    (True, True): (R, R),
    (True, False): (S, T),
    (False, True): (T, S),
    (False, False): (P, P),
}


def play_round(cooperates_a, cooperates_b):
    return payoffs[(cooperates_a, cooperates_b)]


def total_payoffs_network(population,G):
    payoffs = np.zeros(len(population))

    for i, strategy_i in enumerate(population):
        for j in list(G.neighbors(i)):
            #if i == j:
                #continue
            payoff_i, payoff_j = play_round(population[i],population[j])
            payoffs[i] += payoff_i
            # print(f"Agent {i} vs Agent {j}: {population[i]} vs {population[j]} -> payoff_i={payoff_i}, accumulated={payoffs[i]}")
    return np.array(payoffs)

def new_population(population,payoffs,G):
    new_pop = np.zeros(len(population)).astype(bool)
    for i, strategy_i in enumerate(population):
        paycompare = payoffs[i]
        new_pop[i] = strategy_i
        for neighbour in list(G.neighbors(i)):
            if payoffs[neighbour] > paycompare:
                new_pop[i] = population[neighbour] 
                paycompare = payoffs[neighbour]
    return new_pop


def animate_network(history, G, pos, filename = "../images/network_evo.gif"):
    fig, ax = plt.subplots( dpi = 200)
    fig.subplots_adjust(top=0.92)
    fig.tight_layout()

    def update(frame):
        ax.clear()
        ax.set_title(f"Generation {frame} | Cooperation: {np.mean(history[frame]):.2%}",y=0.98)
        node_colors = ["green" if strategy == True else "red" for strategy in history[frame]]
        nx.draw(G,pos=pos,node_color=node_colors,node_size = 30, ax=ax)
        ax.set_axis_off()
        return
    ani = FuncAnimation(fig,update,frames=len(history))
    ani.save(filename, writer="pillow", fps = 5)
    plt.close(fig)
    return ani

