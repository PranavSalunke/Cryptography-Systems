# Pranav Salunke
import gcdLC


def bruteForceModInverse(a, m):
    if not isinstance(a, int):
        raise TypeError("bruteForceModInverse - a must be an integer. Was %s" % (str(type(a))))
    if not isinstance(m, int):
        raise TypeError("bruteForceModInverse - m must be an integer. Was %s" % (str(type(m))))

    if gcdLC.findGCD(a, m) != 1:
        return None

    if m == 1:
        return 0
        # we know gcd = 1 and the linear combination is gcd = a*u + m*v
        # so with m=1 we have 1 = a*0 + 1*1

    for i in range(0, m):
        if (a * i) % m == 1:
            return i
    return None


def modInverse(a, m):

    # remember linearCombination swaps a and m if a is smaller than m
    # in linearCombination a > m even if not inputted that way
    # so keep track of what linearCombination returns as a and m

    if not isinstance(a, int):
        raise TypeError("modInverse - a must be an integer. Was %s" % (str(type(a))))
    if not isinstance(m, int):
        raise TypeError("modInverse - m must be an integer. Was %s" % (str(type(m))))

    gcd, returnedA, returnedM, u, v = gcdLC.linearCombination(a, m)

    if gcd != 1:
        return None

    if returnedA == a:
        return u % m
    else:
        return v % m


def numbersToLetters(alphabet, numberEncoding):
    # for when encoded string is given as numbers instead of letters
    # for example: "0 15 21" instad of "APV" when alphabet is "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    if not isinstance(alphabet, str):
        raise TypeError("numbersToLetters - alphabet must be a string. Was %s" % (str(type(alphabet))))
    if not isinstance(numberEncoding, str):
        raise TypeError("numbersToLetters - numberEncoding must be an integer. Was %s" % (str(type(numberEncoding))))

    letters = ""
    numberEncodingList = numberEncoding.split(" ")
    for n in numberEncodingList:
        letters += alphabet[int(n)]

    return letters


if __name__ == "__main__":  # true if run directly via the command line
    raise UserWarning("miscTools.py is not intended to be used via the command line. Please import it into a Python program and use the methods directly.")
