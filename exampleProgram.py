# Pranav Salunke
# This is an example program displaying how the Crypto Systems can be used in a different program
# run this in the command line with python 3

# ALL OF THE IMPORTS
#  other libraries
import random

#  my programs (make sure they are in the same folder as this file!)
import gcdLC
import miscTools

##-- miscTools.py
print("\n---EXAMPLE FOR miscTools.py---\n")

print("Finding modular inverse of 242 mod 428 using brute force")
mi = miscTools.bruteForceModInverse(243, 428)
print("The modular inverse of 243 mod 428 is %d" % (mi))

print("Same thing with the non brute force modular inverse")
mi = miscTools.modInverse(243, 428)
print("The modular inverse of 243 mod 428 is %d" % (mi))

print()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?,:) "
message = "HEY HOW ARE YOU?! :)"

print("convert the message  \"%s\" to its numerical representation \n in the alphabet: \"%s\"" % (message, alphabet))
messageNums = miscTools.lettersToNumbers(alphabet, message)
print("The numerical representation is: \"%s\"" % (messageNums))

print()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?,:) "
messageNums = "8 32 0 12 32 22 4 11 11 29 32 19 7 0 13 10 18 32 5 14 17 32 0 18 10 8 13 6 27 32 30 3"
print("convert the message  \"%s\" to its letter representation \n in the alphabet: \"%s\"" % (message, alphabet))
message = miscTools.numbersToLetters(alphabet, messageNums)
print("The letter representation is: \"%s\"" % (message))

##-- freqencyAnalysis.py
print("\n---EXAMPLE FOR freqencyAnalysis.py---\n")

##-- gcdLC.py
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

##-- affine.py
print("\n---EXAMPLE FOR affine.py---\n")

##-- affineMatrix.py
print("\n---EXAMPLE FOR affineMatrix.py---\n")

##-- knapsack.py
print("\n---EXAMPLE FOR knapsack.py---\n")

##-- RSA.py
print("\n---EXAMPLE FOR RAS.py---\n")
