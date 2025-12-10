import numpy as np


def markov_chain(P, state0, steps=20):
    state = state0
    history = [state]

    for _ in range(steps):
        state = np.random.choice(len(P), p=P[state])
        history.append(state)

    print("State Path:", history)
    return history


if __name__ == "__main__":
    P = np.array([
        [0.7, 0.3],
        [0.4, 0.6]
    ])
    markov_chain(P, 0)