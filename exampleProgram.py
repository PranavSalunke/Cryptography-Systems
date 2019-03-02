# Pranav Salunke
# This is an example program displaying how the Crypto Systems can be used in a different program
# run this in the command line with python 3

# ALL OF THE IMPORTS
#  other libraries
import random
import argparse

#  my programs (make sure they are in the same folder as this file!)
import gcdLC
import miscTools
import affine


def setArgParse():
    parser = argparse.ArgumentParser(description='Example Program showing how to use the Crypto System in your own projects!')

    parser.add_argument("-s", '--system',
                        choices=["miscTools", "freqencyAnalysis", "gcdLC", "affine", "affineMatrix", "knapsack", "rsa", "all", ],
                        default="all",
                        help="Choose which example to run. Default: all")

    return parser.parse_args()


def runExamples():
    args = setArgParse()
    mode = args.system

    if mode == "miscTools" or mode == "all":
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
        print("convert the message  \"%s\" to its letter representation \n in the alphabet: \"%s\"" % (messageNums, alphabet))
        message = miscTools.numbersToLetters(alphabet, messageNums)
        print("The letter representation is: \"%s\"" % (message))

    if mode == "freqencyAnalysis" or mode == "all":

        ##-- freqencyAnalysis.py
        print("\n---EXAMPLE FOR freqencyAnalysis.py---\n")

    if mode == "gcdLC" or mode == "all":
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

    if mode == "affine" or mode == "all":

        ##-- affine.py
        print("\n---EXAMPLE FOR affine.py---\n")
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        text = "THIS IS AN EXAMPLE"
        print("Encoding \"%s\" with the key (5,11) using alphabet \"%s\"" % (text, alph))
        encoded = affine.affineEncode(alph, (5, 11), text)
        print("This is the output: %s" % (encoded))

        print()
        encodedtext = "FJgyWgyWHpWuGHSiwuWLQWXuALXgpnWHWSuyyHnuWrygpnWUJuWtQQgpuWSuUJLXWHQQgpuIuALXuWygpAuWdLrWHwbuHXdWZpLkWUJuWZud"
        specialAlph = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print("Decoding \"%s\"\nwith the key (23,34)\nusing alphabet \"%s\"" % (encodedtext, specialAlph))
        decoded = affine.affineDecode(specialAlph, (23, 34), encodedtext)
        print("This is the plain text message: %s" % (decoded))

        print()
        unknownMessage = "NCNLKFILOCSNLVPCHLEAHHZBA"
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        print("We don't know the key for this message: %s. We do know the alphabet used: %s, Let's bruteforce it!" % (unknownMessage, alph))
        bruteforce = affine.bruteForceCrack(alph, unknownMessage)
        print(bruteforce)
        print("which one was right? (There are a lot of possibilities, thats why it's better to know the key! :P )")

    if mode == "affineMatrix" or mode == "all":
        ##-- affineMatrix.py
        print("\n---EXAMPLE FOR affineMatrix.py---\n")

    if mode == "knapsack" or mode == "all":
        ##-- knapsack.py
        print("\n---EXAMPLE FOR knapsack.py---\n")

    if mode == "rsa" or mode == "all":
        ##-- RSA.py
        print("\n---EXAMPLE FOR RSA.py---\n")


runExamples()
