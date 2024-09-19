# This program demonstrates a generator that uses the Leibniz formula to yield progressively more accurate estimates of pi

def leibniz_pi_approximation():
    approximation = 0  # Initialize approximation to 0.
    sign = 1  # Initialize sign to 1; will alternate between 1 and -1.
    denominator = 1  # Initialize denominator to 1; will increase by 2 with each step.
    
    while True:  # Infinite loop to keep yielding new approximations.
        approximation += sign * (4 / denominator)
        yield approximation  # Yield the current approximation.
        sign *= -1  # Switch the sign.
        denominator += 2  # Increment the denominator.

# Create generator object
pi_generator = leibniz_pi_approximation()

# Print 10 approximations
for _ in range(10):
    print(next(pi_generator))
