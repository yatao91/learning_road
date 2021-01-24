# -*- coding: utf-8 -*-


# hardware function that computes the nth factorial, e.g. factorial(2)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# hardware main function that uses our factorial function defined above
def main():
    print("I am the factorial helper")
    print("you can call factorial(number) where number is any integer")
    print("for example, calling factorial(5) gives the result:")
    print(factorial(5))


# this runs when the script is called from the command line
if __name__ == '__main__':
    main()
