# Homework 8 - CPython
# This program is a universal launcher that expects its command line arguments to consist of the absolute path 
# to an executable program in any language, followed by any number of arguments for that program (e.g., /bin/ls -l). 
# The wrapper should transparently runs that program and exits with its exit value.
# CS 231 - Advanced Python

import sys
import subprocess

def run_program(executable, *args):
    """
    Run a program with given arguments and return its exit value.
    
    :param executable: Path to the executable program.
    :param args: Arguments for the program.
    :return: Exit value of the program.
    """
    try:
        # Run the program with arguments and capture the output and error streams.
        result = subprocess.run([executable, *args], capture_output=True, text=True)
        
        # Print the output of the program to stdout and stderr respectively.
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)
        
        # Return the exit value of the program.
        return result.returncode

    except FileNotFoundError:
        sys.stderr.write(f"'{executable}' not found\n")
        return 1
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1

if __name__ == "__main__":
    # Check if at least the path to the executable is provided.
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: launcher.py <path_to_executable> [args...]\n")
        sys.exit(1)

    # Split the command line arguments into the executable path and its arguments.
    executable = sys.argv[1]
    args = sys.argv[2:]
    
    # Run the program and capture its exit value.
    exit_value = run_program(executable, *args)
    sys.exit(exit_value)
