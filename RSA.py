# Pranav Salunke


def letterToNumber(alphabet, letter):
    n = alphabet.find(letter)
    if n == -1:
        print("'%s' IS NOT IN THE ALPHABET '%s'. CAN NOT ENCRYPT" % (str(letter), alphabet))
        exit()
    else:
        return n


def numberToLetter(alphabet, number):
    # print("letter as a number: %d" % (number))
    return alphabet[number]


def blockToLetters(alphabet, letters, blockValue, l):
    # print("blockToLetters came in: letters: %s; blockValue: %s; l: %s" % (str(letters), str(blockValue), str(l)))
    alphabetLen = len(alphabet)
    newBlockValue = None
    p = pow(alphabetLen, l)
    q = blockValue // pow(alphabetLen, l)
    # print("1) blockValue %d; l %d; pow %d; q: %d; newBlockValue: %s" %
    #       (blockValue, l, p, q, str(newBlockValue)))
    letter = numberToLetter(alphabet, q)
    letters.append(letter)

    if l > 0:
        newBlockValue = blockValue % pow(alphabetLen, l)
        blockToLetters(alphabet, letters, newBlockValue, l-1)

    # print("2) blockValue %d; l %d; pow %d; q: %d; newBlockValue: %s" %
    #       (blockValue, l, pow(alphabetLen, l), q, str(newBlockValue)))

    if l == 0:
        return letters


def encode(alphabet, message, key):  # key is dict {"n": _, "e":_,"d":_}
    padWithSpace = " " in alphabet
    alphabetLen = len(alphabet)
    encodedMessage = ""
    # split message into blocks with k letters
    c = 0
    messageBlocks = []
    s = ""
    for i in range(len(message)):
        s += message[i]

        if len(s) == k:
            messageBlocks.append(s)
            s = ""

    if len(s) > 0:
        for i in range(len(s), k):  # padding until k block
            if padWithSpace:
                s += " "  # padding until k block
            else:
                # for aplphabet with out space use last letter
                s += alphabet[-1]
        messageBlocks.append(s)  # for remaining letters that are not k block

    # print(messageBlocks)

    # encode each block
    for block in messageBlocks:
        sumA = 0
        encodedBlock = ""
        for i in range(len(block)):
            letter = block[i]
            power = k-1-i  # alphabetLen^power
            letterNumber = letterToNumber(alphabet, letter)
            sumA += letterNumber*(pow(alphabetLen, power))
        sumA = sumA % key["n"]

        encodedA = pow(sumA, key["e"], key["n"])  # sumA^e mod n
        # print("ENCODE || A: %d; EA: %d" % (sumA, encodedA))

        # change encoded block back to aphabet
        # break encodedA into _*alphabetLen^l-1 + _*alphabetLen^l-2...._*alphabetLen^0
        encodedLetters = []
        blockToLetters(alphabet, encodedLetters, encodedA, l-1)  # start at l-1
        # print("letters = " + str("".join(encodedLetters)))
        encodedBlock = "".join(encodedLetters)
        encodedMessage += encodedBlock

    # encodedMessage += "placeholder"
    return encodedMessage


def decode(alphabet, encodedMessage, key):
    if key.get("d") is None:
        return "no decode exponent given"

    alphabetLen = len(alphabet)
    decodedMessage = ""
    # split message into blocks with k letters
    c = 0
    messageBlocks = []
    s = ""
    for i in range(len(encodedMessage)):
        s += encodedMessage[i]

        if len(s) == l:
            messageBlocks.append(s)
            s = ""

    # print(messageBlocks)

    # decode each block
    for block in messageBlocks:
        # print(block)
        sumA = 0
        decodedBlock = ""
        for i in range(len(block)):
            letter = block[i]
            power = l-1-i  # alphabetLen^power
            letterNumber = letterToNumber(alphabet, letter)
            sumA += letterNumber*(pow(alphabetLen, power))
        sumA = sumA % key["n"]

        decodedA = pow(sumA, key["d"], key["n"])  # sumA^d mod n
        # print("A: %d; EA: %d" % (sumA, decodedA))

        # change encoded block back to aphabet
        # break decodedA into _*alphabetLen^l-1 + _*alphabetLen^l-2...._*alphabetLen^0
        decodedLetters = []
        blockToLetters(alphabet, decodedLetters, decodedA, k-1)  # start at l-1
        decodedBlock = "".join(decodedLetters)
        decodedMessage += decodedBlock

    # encodedMessage += "placeholder"
    return decodedMessage


# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Z/26Z
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "  # Z/27Z
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .?!"  # Z/30Z

k = 3  # plain text message units consisting of blocks of k letters
l = 4  # cipher text message units consisting of blocks of l letters.

# encode key: (n, e)
# n = pq
# ex ∈ {1, . . . , φ(nX)}

# key in form: key = {"n": n, "e": encryptnumber, "d": decodekey}

message = "HERE IS MY MESSAGE"
# key = {"n": 46927, "e": 39423, "d": 26767}  # from 7.3 example
key = {"n": 671107, "e": 323849, "d": None}  # mine
encoded = encode(alphabet, message, key)
print(">>" + encoded + "<<")
decoded = decode(alphabet, encoded, key)
print(">>" + decoded + "<<")


# decoded = decode(alphabet, message, key)
# print(">>" + decoded + "<<")
