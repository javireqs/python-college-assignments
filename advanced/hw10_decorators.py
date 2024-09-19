# Homework 10 - Decorators
# This program decorates print() (by assignment, not the pie) so that each positional argument it receives 
# has a 50% chance of being ignored, and demonstrates this behavior.
# CS 231 - Advanced Python

import random
import builtins

# Original print function
original_print = print

# Decorator function
def print_with_random_ignore(*args, **kwargs):
    # Filtering args with a 50% chance
    filtered_args = [arg for arg in args if random.choice([True, False])]
    original_print(*filtered_args, **kwargs)

# Overriding the built-in print function
builtins.print = print_with_random_ignore

# Demonstration
print("This", "is", "a", "test", "to", "see", "random", "omissions.")