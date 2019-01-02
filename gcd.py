# Pranav Salunke
from fractions import gcd as fgcd
import argparse


# set up argparse
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


def findGCD(num1, num2, showGcdWork, findingLC=False):
    a = max(num1, num2)
    b = min(num1, num2)
    if not findingLC:
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
    a = max(num1, num2)
    b = min(num1, num2)
    print("Finding Linear Combination(%d,%d):" % (a, b))

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
    vDict["1"] = -1 * (a / b)  # -q_1 using integer division

    while r != 0:
        i = i + 1
        # u_i = u_(i-2) - q_i*u_(i-1)
        # v_i = v_(i-2) - q_i*v_(i-1)
        r = a % b
        temp = a - r
        q_i = temp / b
        a = b
        b = r
        if i >= 2 and r != 0:
            u = uDict[str(i - 2)] - q_i * uDict[str(i - 1)]
            v = vDict[str(i - 2)] - q_i * vDict[str(i - 1)]
            uDict[str(i)] = u
            vDict[str(i)] = v

    a = max(num1, num2)
    b = min(num1, num2)
    return a, b, u, v


# the functions check which is larger and set a and b accordingly

# num1 = 2458437443
# num2 = 903827662

function = args.function
showGcdWork = args.showGcdWork
num1 = args.number1
num2 = args.number2

if function == "gcd" or function == "both":
    gcd = findGCD(num1, num2, showGcdWork)
    print("Result-- GCD: %d" % (gcd))

if function == "lincomb" or function == "both":
    print()
    a, b, u, v = linearCombination(num1, num2)
    gcd = findGCD(num1, num2, showGcdWork=False, findingLC=True)
    print("Result-- Linear Combination: %d = %d*%d + %d*%d" % (gcd, u, a, v, b))
