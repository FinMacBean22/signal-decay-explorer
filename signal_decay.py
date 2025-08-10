Simple Signal Decay Example

This script shows how a trading signal might weaken over time.
It uses a basic exponential decay formula to simulate the signal dropping
step by step and prints out the results in a neat table.

Author: [Your Name]
Date: 2025
"""

import math

def generate_signal(initial=1.0, decay=0.15, steps=20):
    """
    Create a list of signal strengths, starting at `initial`
    and dropping by the decay rate every step.
    """
    signals = []
    for t in range(steps):
        # signal = initial * e^(-decay * t)
        value = initial * math.exp(-decay * t)
        signals.append(value)
    return signals

def print_signals(signals):
    """
    Print the time step and signal strength side by side
    """
    print("Step | Signal")
    print("--------------")
    for i, val in enumerate(signals):
        print(f"{i:4} | {val:.4f}")

def average_signal(signals):
    """
    Returns the average of all signal values
    """
    return sum(signals) / len(signals) if signals else 0

def main():
    print("Signal Decay Demo\n")

    start = 1.0
    decay_rate = 0.15
    steps = 20

    print(f"Starting signal: {start}")
    print(f"Decay rate per step: {decay_rate}")
    print(f"Total steps: {steps}\n")

    sigs = generate_signal(start, decay_rate, steps)
    print_signals(sigs)

    avg = average_signal(sigs)
    print(f"\nAverage signal over {steps} steps: {avg:.4f}")

if __name__ == "__main__":
    main()
