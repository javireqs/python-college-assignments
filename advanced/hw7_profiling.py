# Homework 7 - Profiling
# This program indicates how many times out of a thousand the Monte Carlo method is 
# faster than the Leibniz formula at converging to within one thousandth of the true value of pi.
# CS 231 - Advanced Python


import time
import random
import cProfile

# Function to estimate the value of pi using the Monte Carlo method.
# It continues sampling points until the estimation is within the 
# provided epsilon of the true value of pi.
def monte_carlo_pi_convergence(epsilon: float = 0.001) -> int:
    inside_circle = 0  # Count of points inside the unit circle
    total_points = 0   # Total points sampled

    while True:
        # Sample random point in the unit square [0, 1) x [0, 1)
        x, y = random.random(), random.random()

        # Check if the point lies inside the unit circle
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
        
        total_points += 1

        # Estimate the value of pi
        pi_estimate = 4 * inside_circle / total_points

        # Check convergence to the true value of pi within epsilon
        if abs(pi_estimate - 3.141592653589793) < epsilon:
            return total_points

# Function to estimate the value of pi using the Leibniz formula.
# It continues the series expansion until the estimation is within 
# the provided epsilon of the true value of pi.
def leibniz_pi_convergence(epsilon: float = 0.001) -> int:
    pi_estimate = 0

    # Iterate through the terms of the Leibniz series
    for k in range(10**6):
        pi_estimate += (-1) ** k / (2 * k + 1)

        # Check convergence to the true value of pi within epsilon
        if abs(4 * pi_estimate - 3.141592653589793) < epsilon:
            return k

# Function to compare the speed of convergence of Monte Carlo and 
# Leibniz methods. Returns True if Monte Carlo is faster, otherwise False.
def compare_methods() -> bool:
    monte_carlo_time = timeit(monte_carlo_pi_convergence)
    leibniz_time = timeit(leibniz_pi_convergence)
    return monte_carlo_time < leibniz_time

# Helper function to time the execution of a function and return 
# the elapsed time.
def timeit(func) -> float:
    start_time = time.perf_counter()  # Start timer
    func()
    return time.perf_counter() - start_time  # Calculate elapsed time

# Main driver function
def main():
    trials = 1000
    # Count how many times out of the trials Monte Carlo is faster
    monte_carlo_faster_count = sum(1 for _ in range(trials) if compare_methods())

    # Print the results
    print(f"Out of {trials} trials, Monte Carlo was faster {monte_carlo_faster_count} times.")

# If the script is the main entry point, profile the main function.
if __name__ == "__main__":
    cProfile.run('main()')
