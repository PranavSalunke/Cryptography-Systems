from fractions import gcd


def bruteForceInverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def findInverse(a, m):
    # does not work yet, only got it to get the gcd.
    # not sure how to do rest of the extended Euclid algo. yet
    # using brute force above for now
    multInv = 0
    oldM = m
    oldA = a
    m = max(oldA, oldM)
    a = min(oldA, oldM)

    q = m // a
    r = m % a
    gcdval = a
    while r != 0:
        gcdval = r
        m = a
        a = r
        r = m % a
        q = m // a


def affineEncode(alphabet, key, plaintext):
    alphalength = len(alphabet)

    plaintextCAP = plaintext.upper()
    encryptedtext = ""

    for c in plaintextCAP:
        letterKey = alphabet.find(c)
        encodedNumber = (((letterKey) * key[0]) + key[1]) % alphalength
        encodedLetter = alphabet[encodedNumber]
        encryptedtext += encodedLetter

    return encryptedtext


def affineDecode(alphabet, key, encryptedtext):
    a, b = key
    z = len(alphabet)

    inverse = bruteForceInverse(a, z)
    decoded = ""
    for e in encryptedtext:
        cipherLetterKey = alphabet.find(e)
        d = inverse * (cipherLetterKey - b)
        d = d % z
        decoded += alphabet[d]
    return decoded


def numbersToLetters(alphabet, numberEncoding):
    letters = ""
    numberEncodingList = numberEncoding.split(" ")
    for n in numberEncodingList:
        letters += alphabet[int(n)]

    return letters


def frequencyAnalysis(alphabet, string, humanAssist=False):
    string = string.upper()
    alphabet = alphabet.upper()
    frequencyDict = {}
    frequencyList = []
    frequencyListLetters = []
    for a in alphabet:
        frequencyDict[str(a)] = 0

    for c in string:
        frequencyDict[str(c)] = frequencyDict[str(c)] + 1

    for letters, freq in frequencyDict.items():
        frequencyList.append((freq, letters))

    frequencyList.sort(reverse=True)

    p1 = 0
    p2 = 0
    while(p2 < len(frequencyList) and p1 < len(frequencyList)):
        sublist = []
        n1, l1 = frequencyList[p1]
        n2, l2 = frequencyList[p2]
        while((p2 < len(frequencyList) and p1 < len(frequencyList)) and frequencyList[p1][0] == frequencyList[p2][0]):

            sublist.append(frequencyList[p2][1])

            p2 = p2 + 1

        p1 = p2
        frequencyListLetters.append(sublist)

    s = ""
    if humanAssist:
        print("human assist mode on")
    for letters in frequencyListLetters:
        if humanAssist:
            if len(letters) == 1:
                s += letters[0]
            else:
                print("pick order")
                for i in range(len(letters)):
                    print("%d: %s" % (i, letters[i]))
                order = ""
                while len(order) != len(letters):
                    orderNumber = input("enter numbers: ")
                    if orderNumber == "exit":
                        exit()
                    if orderNumber == "":
                        continue

                    if len(orderNumber) > 1:
                        for o in orderNumber:
                            o = int(o)
                            if o >= 0 and o < len(letters):
                                if letters[o] not in order:
                                    order += letters[o]
                        for i in range(len(letters)):
                            if letters[i] not in order:
                                print("%d: %s" % (i, letters[i]))
                    else:
                        orderNumber = int(orderNumber)
                        if orderNumber >= 0 and orderNumber < len(letters):
                            if letters[orderNumber] not in order:
                                order += letters[orderNumber]

                        for i in range(len(letters)):
                            if letters[i] not in order:
                                print("%d: %s" % (i, letters[i]))
                s += order
                print("order picked: %s; order so far: %s" % (order, s))
        else:
            if len(letters) == 1:
                s += letters[0]
            else:
                for l in letters:
                    s += l

    return s


def replaceUsingFreq(alphabet, knownAplhFreq, encodedFreq, encodedString):
    # doesnt exactly work
    decodedString = ""
    for letter in encodedString:
        for i in range(len(encodedFreq)):
            # find index of latter in the encodedFreq
            if encodedFreq[i] == letter:
                decodedString += knownAplhFreq[i]
                break
    return decodedString


def bruteForceCrack(alphabet, encodedString):
    z = len(alphabet)
    for a in range(1, z + 1):  # z+1 because range(a,b) goes from a to b-1
        if(gcd(a, z) == 1):
            # print(str(a) + " " + str(linearCombination(a, 27)))
            for b in range(1, z + 1):
                d = affineDecode(alphabet, (a, b), encodedString)
                print("%d %d\n%s" % (a, b, d))


# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?,:) "
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .?!'"


key = (11, 25)  # a,b
# plaintext = "everything is ok"
# encodedString = affineEncode(alphabet, key, plaintext)
# print(encodedString)


# numberEncoding = "15 8 1 17 13 9 17 10 11 1 9 10 22 2 7 17 21 1 24 22 7 12 17 10 1 21 25 24 11 1 2 17 1 17 8 3 22 26 17 3 1 26 19 11 5 1 11 26 22 1 19 8 16 22 21 9 15 11 19 2 7 17 1 23 25 15 7 19 11 19 17 24 1 1 15 1 10 17 24 11 7 17 24 24 1 19 21 15 18 19 8 15 11 19 22 8 1 15 8 3 1 15 1 9 15 11 19 17 8 11 1 9 17 10 11 19 8 15 16 19 11 0 1 1 5 22 26 15 10 3 1 26 1 17 12 17 24"
# # from most freqent to least frequent
# knownFreq = " ETAOINSHRDLCUMWFGYPBVKJXQZ"
# asLetters = numbersToLetters(alphabet, numberEncoding)
# print(affineDecode(alphabet, (14, 15), asLetters))
# frequency = frequencyAnalysis(alphabet, asLetters, False)

# bruteForceCrack(alphabet, asLetters)
message = "I JUST FINISHED MY LAST CRYPTO HW!!"
e = affineEncode(alphabet, (16, 31), message)
print(e)
d = affineDecode(alphabet, (16, 31), e)
print(d)
print(affineDecode(alphabet, (26, 28), "BUVCFIWOUJTZ!H"))
# print(affineDecode(alphabet, (16, 4), "WYVLOOXPPLIYGLKPMXO"))

# findInverse(23, 30)
# print(bruteForceInverse(1341, 134234))
