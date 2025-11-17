"""
CLT Engine
Author: Quant Research Laboratory

Demonstrates the Central Limit Theorem by:
 - Sampling from several parent distributions
 - Computing sample means for many trials for each sample-size n
 - Plotting histogram of sample-means vs theoretical normal (with same mean & se)
 - Showing standard error scaling (se ~ sigma / sqrt(n))
Outputs: saved PNGs in ./reports/
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# ----------- Utilities -----------
def ensure_reports():
    os.makedirs("reports", exist_ok=True)

def sample_means_from_distribution(draw_fn, n, trials, *args, **kwargs):
    """
    draw_fn: function to produce samples, e.g., np.random.normal
    n: sample size per mean
    trials: number of independent sample-means to compute
    returns: array of length `trials` with sample means
    """
    # Efficient vectorized draw: shape (trials, n)
    draws = draw_fn(size=(trials, n), *args, **kwargs)
    return draws.mean(axis=1)

def plot_hist_with_gaussian(sample_means, true_mean, true_sigma, n, dist_name, save=True):
    """
    sample_means: array of computed sample means
    true_mean: parent distribution mean
    true_sigma: parent distribution standard deviation
    n: sample size used to compute each mean
    """
    se = true_sigma / np.sqrt(n)
    xmin, xmax = sample_means.min(), sample_means.max()
    x = np.linspace(xmin - se*2, xmax + se*2, 500)
    gauss_pdf = norm.pdf(x, loc=true_mean, scale=se)

    plt.figure(figsize=(9,5))
    plt.hist(sample_means, bins=50, density=True, alpha=0.6, label="Empirical sampling distribution")
    plt.plot(x, gauss_pdf, 'r--', lw=2, label=f"Theoretical Normal(mean={true_mean:.3g}, se={se:.3g})")
    plt.title(f"CLT: Sampling distribution of mean — {dist_name} | n={n} | samples={len(sample_means)}")
    plt.xlabel("Sample mean")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(alpha=0.25)
    if save:
        filename = f"reports/clt_{dist_name.replace(' ','_')}_n{n}.png"
        plt.savefig(filename, dpi=200, bbox_inches="tight")
        print("Saved:", filename)
    plt.show()

# ----------- Main experiment -----------
def run_clt_experiment(trials=2000, sample_sizes=(1,2,5,10,30,100), seed=123):
    np.random.seed(seed)
    ensure_reports()

    # Define parent distributions with (draw_fn, mean, std, name, draw_args)
    parents = [
        (np.random.normal, 0.0, 1.0, "Normal(0,1)", {'loc':0.0, 'scale':1.0}),
        (np.random.uniform, 0.5, np.sqrt(1/12), "Uniform(0,1)", {'low':0.0, 'high':1.0}),
        (np.random.exponential, 1.0, 1.0, "Exponential(λ=1)", {'scale':1.0}),  # mean=1, sigma=1
        (lambda size, **kw: np.random.chisquare(df=2, size=size), 2.0, np.sqrt(4.0), "ChiSquare(df=2)", {}),  # skewed
    ]

    summary = []  # store mean & var of sample_means for quick table

    for draw_fn, true_mean, true_sigma, name, draw_kwargs in parents:
        for n in sample_sizes:
            # compute sample means
            sample_means = sample_means_from_distribution(draw_fn, n=n, trials=trials, **draw_kwargs)
            empirical_mean = sample_means.mean()
            empirical_std = sample_means.std(ddof=1)
            summary.append((name, n, empirical_mean, empirical_std, true_mean, true_sigma, true_sigma/np.sqrt(n)))
            print(f"[{name}] n={n:3d}  empirical_mean={empirical_mean:.4f}  empirical_std={empirical_std:.4f}  theoretical_se={true_sigma/np.sqrt(n):.4f}")

            # plot histogram and theoretical gaussian
            plot_hist_with_gaussian(sample_means, true_mean, true_sigma, n, dist_name=name, save=True)

    # print summary table
    print("\nSummary (Name, n, emp_mean, emp_std, true_mean, true_sigma, theoretical_se):")
    for row in summary:
        print(f"{row[0]:20s} n={row[1]:3d}  emp_mean={row[2]:.4f}  emp_std={row[3]:.4f}  true_mean={row[4]:.4f}  sigma={row[5]:.4f}  se={row[6]:.4f}")

if __name__ == "__main__":
    # default run: 2000 trials per n — fast but illustrative
    run_clt_experiment(trials=2000, sample_sizes=(1,2,5,10,30,100))