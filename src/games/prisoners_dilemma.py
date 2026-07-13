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