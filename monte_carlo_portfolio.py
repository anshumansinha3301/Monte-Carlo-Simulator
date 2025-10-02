#!/usr/bin/env python3
import random
import statistics
from typing import Dict, List

class MonteCarloPortfolio:
    def __init__(self, initial_investment: float, years: int, mean_return: float, volatility: float, simulations: int = 1000):
        self.initial_investment = initial_investment
        self.years = years
        self.mean_return = mean_return
        self.volatility = volatility
        self.simulations = simulations
        self.results: List[float] = []

    def run_simulation(self):
        self.results = []
        for _ in range(self.simulations):
            value = self.initial_investment
            for _ in range(self.years):
                annual_return = random.gauss(self.mean_return, self.volatility)
                value *= (1 + annual_return)
            self.results.append(value)

    def summary(self) -> Dict[str, float]:
        if not self.results:
            return {}
        return {
            "Mean Final Value": round(statistics.mean(self.results), 2),
            "Median Final Value": round(statistics.median(self.results), 2),
            "Best Case": round(max(self.results), 2),
            "Worst Case": round(min(self.results), 2),
            "5th Percentile": round(sorted(self.results)[int(0.05 * self.simulations)], 2),
            "95th Percentile": round(sorted(self.results)[int(0.95 * self.simulations)], 2),
        }

    def probability_of_loss(self) -> float:
        if not self.results:
            return 0.0
        losses = [r for r in self.results if r < self.initial_investment]
        return round(len(losses) / len(self.results) * 100, 2)

def demo():
    portfolio = MonteCarloPortfolio(
        initial_investment=10000,
        years=20,
        mean_return=0.07,      # 7% average return
        volatility=0.15,       # 15% std dev
        simulations=5000
    )
    portfolio.run_simulation()
    print("Portfolio Simulation Summary:")
    for k, v in portfolio.summary().items():
        print(f"{k}: {v}")
    print("Probability of Loss:", portfolio.probability_of_loss(), "%")

if __name__ == "__main__":
    demo()
