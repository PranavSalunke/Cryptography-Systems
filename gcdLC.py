# Pranav Salunke
from fractions import gcd as fgcd
import argparse


# set up argparse
def setArgParse():
    parser = argparse.ArgumentParser(description='Program to find the GCD and/or linear combination of two integers using the euclidean algorithm')

    parser.add_argument("-f", '--function',
                        choices=["gcd", "lincomb", "both"],
                        default="both",
                        help="If you want the GCD of the two integers or the linear combination or both. Choices: \"gcd\", \"lincomb\" \"both\" (default) ")
    parser.add_argument('-showGcdWork',
                        action='store_true',
                        help="Include this flag to show the work in finding the GCD."
                        )
    parser.add_argument("number1",
                        type=int,
                        help="The first number")
    parser.add_argument("number2",
                        type=int,
                        help="The second number")

    args = parser.parse_args()

    return args


def findGCD(num1, num2, showGcdWork=False):
    if not isinstance(num1, int):
        raise TypeError("findGCD - num1 must be an integer. Was %s" % (str(type(num1))))
    if not isinstance(num2, int):
        raise TypeError("findGCD - num2 must be an integer. Was %s" % (str(type(num2))))
    if not isinstance(showGcdWork, bool):
        raise TypeError("findGCD - showGcdWork must be a boolean. Was %s" % (str(type(showGcdWork))))

    a = max(num1, num2)
    b = min(num1, num2)
    print("Finding gcd(%d,%d):" % (a, b))

    r = a % b  # check if it is 0 (if a is multiple of b)
    q = None
    gcdanswer = b  # if a is multiple of b, b (the smaller number) will the the gcd
    # if not, it will be set to the right value in the loop

    while r != 0:
        gcdanswer = r
        r = a % b
        temp = a - r
        q = temp / b
        if(showGcdWork):
            print("%d = %d * %d + %d" % (a, q, b, r))

        a = b
        b = r

    return gcdanswer


def linearCombination(num1, num2):
    if not isinstance(num1, int):
        raise TypeError("linearCombination - num1 must be an integer. Was %s" % (str(type(num1))))
    if not isinstance(num2, int):
        raise TypeError("linearCombination - num2 must be an integer. Was %s" % (str(type(num2))))

    a = max(num1, num2)
    origA = a
    b = min(num1, num2)
    origB = b
    print("Finding LinearCombination(%d,%d):" % (a, b))

    r = None
    q_i = None
    u = None
    v = None
    uDict = {}  # to keep track of u_i. Key is i value is u_i
    vDict = {}

    # initial values
    i = 0
    uDict["0"] = 0
    uDict["1"] = 1
    vDict["0"] = 1
    vDict["1"] = -1 * (a // b)  # -q_1 using integer division

    while r != 0:
        i = i + 1
        # u_i = u_(i-2) - q_i*u_(i-1)
        # v_i = v_(i-2) - q_i*v_(i-1)
        r = a % b
        temp = a - r
        q_i = temp / b
        a = b
        if r != 0:  # last b value is the gcd
            b = r
        if i >= 2 and r != 0:
            u = uDict[str(i - 2)] - q_i * uDict[str(i - 1)]
            v = vDict[str(i - 2)] - q_i * vDict[str(i - 1)]
            uDict[str(i)] = u
            vDict[str(i)] = v

    u = int(uDict[str(i-1)])  # not entirely sure why i-1, but I think we don't count the one where r = 0
    v = int(vDict[str(i-1)])
    return b, origA, origB, u, v,


def main():
    if __name__ != "__main__":
        raise UserWarning("main() should not be called from a script when gcdLC.py is imported. Use findGCD and linearCombination directly.")

    args = setArgParse()
    function = args.function
    showGcdWork = args.showGcdWork
    num1 = args.number1
    num2 = args.number2
    # the findGCD and linearCombination check which argument is larger and set a and b accordingly
    if function == "gcd" or function == "both":
        gcd = findGCD(num1, num2, showGcdWork)
        print("  Result-- GCD: %d" % (gcd))

    if function == "lincomb" or function == "both":
        if function == "both":
            print()
        gcd, a, b, u, v = linearCombination(num1, num2)
        print("  Result-- Linear Combination: %d = %d*%d + %d*%d" % (gcd, u, a, v, b))


if __name__ == "__main__":  # true if run directly via the command line
    main()
