

def decToBin(x):
    return bin(x)[2:]


def binToDec(b):
    return int(b, 2)


def calculateWi(Vi, a, m):
    Wi = []
    for v in Vi:
        Wi.append((v*a) % m)

    return Wi


def decToBinBackwardsList(x, WiLen):  # returns as list backwards to match with Wi
    decNum = str(decToBin(x))

    if len(decNum) < WiLen:  # pad it to be len k (k=WiLen)
        decNumTemp = decNum
        decNum = ""
        for _ in range(WiLen - len(decNumTemp)):
            decNum += "0"
        decNum += decNumTemp

    decNumBackwardList = []
    for i in range(len(decNum)-1, -1, -1):
        decNumBackwardList.append(int(decNum[i]))
    return decNumBackwardList


def letterToNumber(alphabet, letter):
    return alphabet.find(letter)


def numberToLetter(alphabet, number):
    return alphabet[number]


def superIncreasingKnapsackBackwards(V, Vi):
    # finds binary representation of the solution
    # returns flipped so maps to a number
    binaryList = ["0"]*len(Vi)  # len([0,0...0,0]) = len(Vi)
    for i in range(len(Vi)-1, -1, -1):
        if Vi[i] <= V:
            binaryList[i] = "1"
            V -= Vi[i]
    binaryList.reverse()

    return "0b" + "".join(binaryList)


def encode(alphabet, message, Wi):
    encoded = []
    WiLen = len(Wi)
    for l in message:
        sum_ = 0
        n = letterToNumber(alphabet, l)
        binrep = decToBinBackwardsList(n, WiLen)

        for i in range(WiLen):
            if binrep[i] == 1:
                sum_ += Wi[i]

        encoded.append(sum_)

    return encoded


def decode(alphabet, b, m, encodedSeqence, Wi, Vi):
    decodedString = ""
    for e in encodedSeqence:
        V = (e*b) % m
        binaryRep = superIncreasingKnapsackBackwards(V, Vi)

        decodedString += numberToLetter(alphabet, binToDec(binaryRep))
    return decodedString


# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Z/26Z
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .?!'"

# from example
# Vi = [2, 3, 7, 15, 31]
# Wi = [34, 51, 58, 11, 39]
# m = 61
# a = 17
# b = 18

Vi = [3, 5, 10, 20, 41]
a = 17
b = 53
m = 100
Wi = calculateWi(Vi, a, m)
# Vi = [3, 4, 10, 19, 40]
# a = 19
# b = 79
# m = 100
# Wi = calculateWi(Vi, a, m)

# message = "WHY"
message = "I JUST FINISHED MY LAST CRYPTO HW!!"
cipherSequence = encode(alphabet, message, Wi)
print(cipherSequence)
if b is not None:
    plainText = decode(alphabet, b, m, cipherSequence, Wi, Vi)
    print(plainText)

print(decode(alphabet, b, m, [182, 176, 167, 155], Wi, Vi))
