# Pranav Salunke
# This is an example program displaying how the Crypto Systems can be used in a different program
# run this in the command line with python 3

# ALL OF THE IMPORTS
#  other libraries
import random

#  my programs (make sure they are in the same folder as this file!)
import gcdLC

# gcdLC.py
print("\n---EXAMPLE FOR gcdLC.py---\n")

print("Finding GCD of 134 and 102")
gcd1 = gcdLC.findGCD(134, 102)
print("The GCD of 134 and 102 is %d" % (gcd1))
gcd, a, b, u, v = gcdLC.linearCombination(134, 102)
print("The Linear Combination of 134 and 102 is: %d = %d*%d + %d*%d" % (gcd, u, a, v, b))

# now for some randomness
print()
n1 = random.randint(1, 1000)
n2 = random.randint(1, 1000)

print("Finding GCD of %d and %d" % (n1, n2))
gcd2 = gcdLC.findGCD(n1, n2)
print("The GCD of %d and %d is %d" % (n1, n2, gcd2))
gcd, a, b, u, v = gcdLC.linearCombination(n1, n2)
print("The Linear Combination of %d and %d is: %d = %d*%d + %d*%d" % (n1, n2, gcd, u, a, v, b))

print()
print("Finding GCD of %d and %d and showing work" % (n1, n2))
gcd3 = gcdLC.findGCD(n1, n2, True)
print("GCD: %d" % (gcd3))

# affine.py
print("\n---EXAMPLE FOR affine.py---\n")

# affineMatrix.py
print("\n---EXAMPLE FOR affineMatrix.py---\n")

# knapsack.py
print("\n---EXAMPLE FOR knapsack.py---\n")

# RSA.py
print("\n---EXAMPLE FOR RAS.py---\n")
