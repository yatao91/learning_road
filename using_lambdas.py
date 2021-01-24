# -*- coding: utf-8 -*-
# import the lambdas module
import lambdas


# hardware main function in which we compute the double of 7
def main():
    print(lambdas.g(7))


# this executes when the module is invoked as hardware script at the command line
if __name__ == '__main__':
    main()
