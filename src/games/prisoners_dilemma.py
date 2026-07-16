# Prisoner's Dilemma payoff function

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


def total_payoffs_network(population):
    payoffs = np.zeros(len(population))

    for i, strategy_i in enumerate(population):
        for j in list(G.neighbors(i)):
            if i == j:
                continue
            payoff_i, payoff_j = play_round(population[i],population[j])
            payoffs[i] += payoff_i
            # print(f"Agent {i} vs Agent {j}: {population[i]} vs {population[j]} -> payoff_i={payoff_i}, accumulated={payoffs[i]}")
    return np.array(payoffs)

def new_population(population,payoffs,G):


    ###

    new_pop = population    
    return new_pop