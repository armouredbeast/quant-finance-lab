"""
PILLAR 1 — PROJECT 1
Probability Simulator
Author: Quant Research Laboratory
Description:
A clean educational toolkit for simulating probability experiments:
- Coin tosses
- Dice throws
- Event probabilities
- Conditional probabilities
- Bayes theorem engine
"""
import random
from collections import Counter
import itertools

## 01. Coin simulator
def simulate_coins(n_tosses: int = 1, n_trials: int = 10000):
    """iumulates tossing n_tosses coins per trial"""
    outcomes = []
    for _ in range(n_trials):
        toss = "".join(random.choice(['H','T']) for _ in range(n_tosses))
        outcomes.append(toss)
    return Counter(outcomes), n_trials

## 02. Dice Simulator
def simulate_dice(n_dice: int = 2, n_trials: int = 10000):
    """Simulate rolling n dice. """
    outcomes = []
    for _ in range(n_trials):
        roll = tuple(random.randint(1,6) for _ in range(n_dice))
        outcomes.append(roll)
    return Counter(outcomes), n_trials
def probability_sum_k(k: int, n_trials: int = 20000):
    """Probability that sum of 2 dice equals k."""
    cnt, total = simulate_dice(2, n_trials)
    good = sum(v for (a,b), v in cnt.items() if a+b ==k)
    return good /total
# -----------------------------------------------------------
# 3. GENERAL EVENT PROBABILITY
# -----------------------------------------------------------
def event_probability(outcome_space, event_filter):
    """
    outcome_space: list/iterable of outcomes
    event_filter: function that returns True if outcome ∈ event
    """
    total = len(outcome_space)
    count = sum(1 for x in outcome_space if event_filter(x))
    return count / total


# -----------------------------------------------------------
# 4. CONDITIONAL PROBABILITY
# -----------------------------------------------------------
def conditional_probability(outcome_space, A_filter, B_filter):
    """
    Computes P(A | B) = P(A ∩ B) / P(B)
    """
    A_and_B = sum(1 for x in outcome_space if A_filter(x) and B_filter(x))
    B = sum(1 for x in outcome_space if B_filter(x))

    if B == 0:
        return 0
    return A_and_B / B


# -----------------------------------------------------------
# 5. BAYES THEOREM ENGINE
# -----------------------------------------------------------
def bayes(prior_A, likelihood_B_given_A, likelihood_B_given_notA):
    """
    Bayes formula:
    P(A|B) = P(B|A)P(A) / (P(B|A)P(A) + P(B|A')P(A'))
    """
    numerator = likelihood_B_given_A * prior_A
    denominator = numerator + likelihood_B_given_notA * (1 - prior_A)
    return numerator / denominator


# -----------------------------------------------------------
# 6. OUTCOME SPACE GENERATORS
# -----------------------------------------------------------
def coin_space(n=3):
    """All possible outcomes of n coins."""
    return ["".join(p) for p in itertools.product(["H", "T"], repeat=n)]


def dice_space(n=2):
    """All possible outcomes of n dice."""
    return list(itertools.product(range(1, 7), repeat=n))


# -----------------------------------------------------------
# DEMO
# -----------------------------------------------------------
if __name__ == "__main__":
    print("\n=== COIN SIMULATION (3 coins) ===")
    count, total = simulate_coins(3, 5000)
    print(count)

    print("\n=== DICE: Probability sum=7 ===")
    print(probability_sum_k(7))

    print("\n=== Conditional Probability Example ===")
    Ω = coin_space(3)
    # A = first coin is H
    # B = at least 2 H in total
    PA_given_B = conditional_probability(
        Ω,
        A_filter=lambda x: x[0] == "H",
        B_filter=lambda x: x.count("H") >= 2
    )
    print("P(first coin = H  | at least 2 H) =", PA_given_B)

    print("\n=== Bayes Theorem Example ===")
    print("P(A|B) =", bayes(prior_A=0.3,
                           likelihood_B_given_A=0.8,
                           likelihood_B_given_notA=0.2))