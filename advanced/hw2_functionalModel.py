# Javier Hernandez Requena
# CS 231
# Aaron Brick
# February 20, 2022
# Homework 2 - Functional Model
# This program displays the curvature of a sinusoid on the terminal


from math import sin, radians
from time import sleep
import signal
import sys

def signal_handler(sig, frame):
    """Handle keyboard interruption (Ctrl+C) to exit the loop gracefully."""
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def wave(frequency=1, amplitude=100, speed=0.01):
    """
    Display a wave in the terminal.

    :param frequency: Frequency of the wave.
    :param amplitude: Amplitude of the wave.
    :param speed: Speed at which the wave is displayed.
    """
    while True:
        for a in range(-180, 180):
            angle_in_radians = radians(a * frequency)
            s = round(sin(angle_in_radians) * amplitude) // 2
            offset = s + 50
            print(f"{a} degrees:", end="\t")
            print(" " * offset, end="*\n")
            sleep(speed)

# Parameters: frequency, amplitude, and speed
wave(1, 100, 0.01)
