#!/usr/bin/python3
# Estimate the value of the percolation threshold via Monte Carlo simulation
from percolation import Percolation
from random import randint
from math import sqrt
import statistics


class PercolationStats:
    # Perform independent trials on an n-by-n grid
    def __init__(self, n, trials):
        # Perform independent trials on an n-by-n grid
        if n <= 0 or trials <= 0:
            raise Exception('N and trials both need to be larger than 0')
        self.threshold = []
        self.n = n
        self.trials = trials
        for i in range(trials):
            p = Percolation(n)
            while not p.percolates():
                p.open(randint(1, n), randint(1, n))
            self.threshold.append(p.number_open_sites() / (n ** 2))

    def __str__(self):
        # Return the percolation stats
        string = '{}-by-{} grid, {} trials\n'.format(
            self.n, self.n, self.trials)
        string += 'mean: {}\n'.format(self.mean())
        string += 'stddev: {}\n'.format(self.stddev())
        string += '95% confidence interval: [{}, {}]\n'.format(
            self.confidence_lo(), self.confidence_hi())
        return string

    def mean(self):
        # Sample mean of percolation threshold
        return statistics.mean(self.threshold)

    def stddev(self):
        # Sample standard deviation of percolation threshold
        return statistics.stdev(self.threshold)

    def confidence_lo(self):
        # Low endpoint of 95% confidence interval (Z value of 1.96)
        return self.mean() - (1.96 * self.stddev() / sqrt(self.n ** 2))

    def confidence_hi(self):
        # High endpoint of 95% confidence interval (Z value of 1.96)
        return self.mean() + (1.96 * self.stddev() / sqrt(self.n ** 2))

if __name__ == '__main__':
    print(PercolationStats(20, 100))
    print(PercolationStats(5, 1000))
    print(PercolationStats(2, 10000))
