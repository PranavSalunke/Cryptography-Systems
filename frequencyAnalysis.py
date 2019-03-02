# Pranav Salunke
# import affine
raise NotImplementedError("freqencyAnalysis has not been completed yet. I am working on it! I will update the repository when it is completed!")


def getFrequencyAnalysis(alphabet, string):
    # returns list of tuples for every letter in alphabet
    # tuple: (N,L) where N is the frequency of letter L in the string
    string = string.upper()
    alphabet = alphabet.upper()
    frequencyDict = {}
    frequencyList = []
    for a in alphabet:
        frequencyDict[str(a)] = 0

    for c in string:
        frequencyDict[str(c)] = frequencyDict[str(c)] + 1

    for letters, freq in frequencyDict.items():
        frequencyList.append((freq, letters))

    frequencyList.sort(reverse=True)
    # print(frequencyList)
    return frequencyList


def joinLetterFreqency(frequencyList):
    # returns list of lists
    # inside list is a list of letters with the same freqency/ groups letters with same freqency
    #   the group of letters is done alphabetically
    # frequencyList is retrieved from getFrequencyAnalysis
    p1 = 0
    p2 = 0
    frequencyListLetters = []
    while(p2 < len(frequencyList) and p1 < len(frequencyList)):
        sublist = []
        n1, l1 = frequencyList[p1]
        n2, l2 = frequencyList[p2]
        while((p2 < len(frequencyList) and p1 < len(frequencyList)) and frequencyList[p1][0] == frequencyList[p2][0]):
            sublist.append(frequencyList[p2][1])
            p2 = p2 + 1

        p1 = p2
        # sublist.sort()
        frequencyListLetters.append(sublist)

    return frequencyListLetters


def createEncodedFreqOrder(encodedString, humanAssist=False):
    # creates string of the letters in encodedString in the order of their freqency where first letter is most frequent
    # if humanAssist is True,
    #   user is prompted in the console to provide an order for letters which have the same freqency
    #   otherwise it will be done in alphabetical order
    # use humanAssist only in console

    # gets the frequency analysis of encodedString
    frequencyList = getFrequencyAnalysis(alphabet, encodedString)
    # groups letters together depending on their frequency
    frequencyListLetters = joinLetterFreqency(frequencyList)

    s = ""
    if humanAssist:
        print("human assist mode on")
    for letters in frequencyListLetters:
        if humanAssist:
            if len(letters) == 1:
                s += letters[0]
            else:
                print("pick order. ex. \"2 0 1 3\" with no quotes")
                for i in range(len(letters)):
                    print("%d: %s" % (i, letters[i]))
                order = ""
                while len(order) != len(letters):
                    orderNumber = input("enter numbers (or e/exit): ")
                    if orderNumber == "exit" or orderNumber == "e":
                        exit()
                    if orderNumber == "":
                        continue
                    orderNumber = orderNumber.split()
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
                        orderNumber = int(orderNumber[0])
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
    # attempts to crack the code using frequency analysis.
    # knownAplhFreq can be found on wikipedia and passed in:
    #   https://en.wikipedia.org/w/index.php?title=Letter_frequency#Relative_frequencies_of_letters_in_the_English_language
    # encodedFreq is what is returned by createEncodedFreqOrder

    # doesnt exactly work
    decodedString = ""
    for letter in encodedString:
        for i in range(len(encodedFreq)):
            # find index of latter in the encodedFreq
            if encodedFreq[i] == letter:
                decodedString += knownAplhFreq[i]
                break
    return decodedString


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
knownFreq = " ETAOINSHRDLCUMWFGYPBVKJXQZ"  # for a-z + space alphabet
# message = "RANK TALL BOY MAN THEM OVER POST NOW OFF INTO SHE BED LONG FAT ROOM RECOMMEND EXISTENCE CURIOSITY PERFECTLY FAVOURITE GET EAT SHE WHY DAUGHTERS NOT MAY TOO NAY BUSY LAST SONG MUST SELL AN NEWSPAPER ASSURANCE DISCOURSE YE CERTAINLY SOON GONE GAME AND WHY MANY CALM HAVE DETRACT YET DELIGHT WRITTEN FARTHER HIS GENERAL IF IN SO BRED AT DARE ROSE LOSE GOOD FEEL AND MAKE TWO REAL MISS USE EASY CELEBRATED DELIGHTFUL AN ESPECIALLY INCREASING INSTRUMENT AM INDULGENCE CONTRASTED SUFFICIENT TO UNPLEASANT IN IN INSENSIBLE FAVOURABLE LATTER REMARK HUNTED ENOUGH VULGAR SAY MAN SITTING HEARTED ON IT WITHOUT ME VILLAGE DID REMOVED ENJOYED EXPLAIN NOR HAM SAW CALLING TALKING SECURING AS INFORMED DECLARED OR MARGARET JOY HORRIBLE MOREOVER MAN FEELINGS OWN SHY REQUEST NORLAND NEITHER MISTAKE FOR YET BETWEEN THE FOR MORNING ASSURED COUNTRY BELIEVE ON EVEN FEET TIME HAVE AN NO AT RELATION SO IN CONFINED SMALLEST CHILDREN UNPACKED DELICATE WHY SIR END BELIEVE UNCIVIL RESPECT ALWAYS GET ADIEUS NATURE DAY COURSE FOR COMMON MY LITTLE GARRET REPAIR TO DESIRE HE ESTEEM YET BED ANY FOR TRAVELLING ASSISTANCE INDULGENCE UNPLEASING NOT THOUGHTS ALL EXERCISE BLESSING INDULGENCE WAY EVERYTHING JOY ALTERATION BOISTEROUS THE ATTACHMENT PARTY WE YEARS TO ORDER ALLOW ASKED OF WE SO OPINION FRIENDS ME MESSAGE AS DELIGHT WHOLE FRONT DO OF PLATE HEARD OH OUGHT HIS DEFECTIVE NOR CONVINCED RESIDENCE OWN CONNECTION HAS PUT IMPOSSIBLE OWN APARTMENTS BOISTEROUS AT JOINTURE LADYSHIP AN INSISTED SO HUMANITY HE FRIENDLY BACHELOR ENTRANCE TO ON BY SPORTSMAN DELIGHTED IMPROVING DASHWOODS GAY INSTANTLY HAPPINESS SIX HAM NOW AMOUNTED ABSOLUTE NOT MISTAKEN WAY PLEASANT WHATEVER AT AN THESE STILL NO DRIED FOLLY STOOD THING RAPID IT ON HOURS HILLS IT SEVEN YEARS IF POLITE HE ACTIVE COUNTY IN SPIRIT AN MRS HAM INTENTION PROMOTION ENGROSSED ASSURANCE DEFECTIVE CONFINED SO GRACEFUL BUILDING OPINIONS WHATEVER TRIFLING IN INSISTED OUT DIFFERED HAM MAN ENDEAVOR EXPENSES AT ON HE TOTAL THEIR HE SONGS RELATED COMPACT EFFECTS IS ON SETTLED DO DO IN LAUGHTER SECURING SMALLEST SENSIBLE NO MR HASTENED AS PERHAPS PROCEED IN IN BRANDON OF LIMITED UNKNOWN GREATLY DISTRUSTS FULFILLED HAPPINESS UNWILLING AS EXPLAINED OF DIFFICULT NO LANDLORD OF PECULIAR LADYSHIP ATTENDED IF CONTEMPT ECSTATIC LOUD WISH MADE ON IS AM AS HARD COURT SO AVOID IN PLATE HENCE OF RECEIVED MR BREEDING CONCERNS PECULIAR SECURING LANDLORD SPOT TO MANY IT FOUR BRED SOON WELL TO OR AM PROMOTION IN NO DEPARTURE ABILITIES WHATEVER LANDLORD YOURSELF AT BY PLEASURE OF CHILDREN BE STARTED HIS HEARTED ANY CIVILLY SO ME BY MARIANNE ADMITTED SPEAKING MEN BRED FINE CALL ASK CEASE ONE MILES TRUTH DAY ABOVE SEVEN SUSPICION SPORTSMEN PROVISION SUFFERING MRS SAW ENGROSSED SOMETHING SNUG SOON HE ON PLAN IN BE DINE SOME VIEW FINE ME GONE THIS NAME AN RANK COMPACT GREATER AND DEMANDS MRS THE PARLORS PARK BE FINE EASY AM SIZE AWAY HIM AND FINE BRED KNEW AT OF HARDLY SISTER FAVOUR AS SOCIETY EXPLAIN COUNTRY RAISING WEATHER OF SENTIMENTS NOR EVERYTHING OFF OUT UNCOMMONLY PARTIALITY BED IN UP SO DISCOVERY MY MIDDLETON EAGERNESS DEJECTION EXPLAINED ESTIMATING EXCELLENCE YE CONTRASTED INSENSIBLE AS OH UP UNSATIABLE ADVANTAGES DECISIVELY AS AT INTERESTED PRESENT SUPPOSE IN ESTEEMS IN DEMESNE COLONEL IT TO END HORRIBLE SHE LANDLORD SCREENED STANHILL REPEATED OFFENDED YOU OPINIONS OFF DISSUADE ASK PACKAGES SCREENED SHE ALTERATION EVERYTHING SYMPATHIZE IMPOSSIBLE HIS GET COMPLIMENT COLLECTED FEW EXTREMITY SUFFERING MET HAD SPORTSMAN UP AM INTENTION ON DEPENDENT QUESTIONS OH ELSEWHERE SEPTEMBER NO BETRAYED PLEASURE POSSIBLE JOINTURE WE IN THROWING AND CAN EVENT RAPID ANY SHALL WOMAN GREEN HOPE THEY DEAR WHO ITS BRED SMILING NOTHING AFFIXED HE CARRIED IT CLOTHES CALLING HE NO ITS SOMETHING DISPOSING DEPARTURE SHE FAVOURITE TOLERABLY ENGROSSED TRUTH SHORT FOLLY COURT WHY SHE THEIR BALLS EXCELLENCE PUT UNAFFECTED REASONABLE MRS INTRODUCED CONVICTION SHE NAY PARTICULAR DELIGHTFUL BUT UNPLEASANT FOR UNCOMMONLY WHO"
message = "THIS IS A SMALL MESSAGE"
# ^ message made using a random generator for texing a large message

# e = affine.affineEncode(alphabet, (16, 27), message)
e = affineEncode(alphabet, (16, 27), message)

encodedorder = createEncodedFreqOrder(e, False)
f = getFrequencyAnalysis(alphabet, e)
lf = joinLetterFreqency(f)
d = replaceUsingFreq(alphabet, knownFreq, encodedorder, e)

print(e)
print(encodedorder)
print(f)
print(lf)
print(d)
