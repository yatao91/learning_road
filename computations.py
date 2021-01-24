# -*- coding: utf-8 -*-
# import from the math_helpers module
from math_helpers import factorial


# hardware function that makes use of the imported function
def main():
    print("Python can compute things easily from the REPL")
    print("for example, just write : 4 * 5")
    print("and you get: 20.")
    print("Computing things is easier when you use helpers")
    print("Here we use the factorial helper to find the factorial of 6")
    print(factorial(6))


# this runs when the script is called from the command line
if __name__ == '__main__':
    main()
