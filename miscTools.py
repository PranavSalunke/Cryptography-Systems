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
    # for example: "0 15 21" instead of "APV" when alphabet is "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    if not isinstance(alphabet, str):
        raise TypeError("numbersToLetters - alphabet must be a string. Was %s" % (str(type(alphabet))))
    if not isinstance(numberEncoding, str):
        raise TypeError("numbersToLetters - numberEncoding must be a string. Was %s" % (str(type(numberEncoding))))

    numberEncoding = numberEncoding.strip()  # remove leading or trailing whitespace
    letters = ""
    numberEncodingList = numberEncoding.split(" ")
    for n in numberEncodingList:
        try:
            num = int(n)
            letters += alphabet[num]
        except ValueError as v:
            customMsg = "numbersToLetters - %s, passed in the numberEncoding string, is not a valid interger" % (str(n))
            v.args = (customMsg, *v.args)
            raise v
        except IndexError as i:
            customMsg = "numbersToLetters - %d is not a valid numeric index for alphabet: \"%s\" should be between 0-%d" % (
                num, alphabet, len(alphabet)-1)
            i.args = (customMsg, *i.args)
            raise i

    return letters


def lettersToNumbers(alphabet, message):
    # to turn a message to its number encoding equivalent
    # for example: "APV" instead of "0 15 21" when alphabet is "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    if not isinstance(alphabet, str):
        raise TypeError("lettersToNumbers - alphabet must be a string. Was %s" % (str(type(alphabet))))
    if not isinstance(message, str):
        raise TypeError("lettersToNumbers - message must be a string. Was %s" % (str(type(message))))

    numbers = ""
    for m in message:
        n = alphabet.find(m)
        if n < 0:  # not in alphabet
            raise IndexError("lettersToNumbers - %s is not a valid letter in the alphabet: \"%s\"" % (m, alphabet))
        numbers += str(n) + " "
    return numbers.strip()


if __name__ == "__main__":  # true if run directly via the command line
    raise UserWarning("miscTools.py is not intended to be used via the command line. Please import it into a Python program and use the methods directly.")
