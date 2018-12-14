# Pranav Salunke
from fractions import gcd as fgcd


def findGCD(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    print("Finding gcd(%d,%d):\n" % (a, b))

    r = None
    gcdanswer = None
    q = None

    while r != 0:
        gcdanswer = r
        r = a % b
        temp = a - r
        q = temp / b
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
# for question 1
num1 = 2458437443
num2 = 903827662

gcd = findGCD(num1, num2)
print("\nGCD: %d" % (gcd))

a, b, u, v = linearCombination(num1, num2)
print("Linear Combination: %d = %d*%d + %d*%d" % (gcd, u, a, v, b))


# extra examples
print("-------------")

# from lecture
num1 = 1001
num2 = 1339

gcd = findGCD(num1, num2)
print("\nGCD: %d" % (gcd))

a, b, u, v = linearCombination(num1, num2)
print("Linear Combination: %d = %d*%d + %d*%d" % (gcd, u, a, v, b))

print("-------------")

num1 = 97564
num2 = 84

gcd = findGCD(num1, num2)
print("\nGCD: %d" % (gcd))

a, b, u, v = linearCombination(num1, num2)
print("Linear Combination: %d = %d*%d + %d*%d" % (gcd, u, a, v, b))

print("-------------")

num1 = 5690
num2 = 12001

gcd = findGCD(num1, num2)
print("\nGCD: %d" % (gcd))

a, b, u, v = linearCombination(num1, num2)
print("Linear Combination: %d = %d*%d + %d*%d" % (gcd, u, a, v, b))


for i in range(1, 32):
    g = fgcd(i, 30)
    print(str(i) + " -- " + str(g))
