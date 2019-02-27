# Pranav Salunke
import argparse

# import my own program
import gcdLC
import miscTools


def setArgParse():
    if __name__ != "__main__":
        raise UserWarning("setArgParse() should not be called from a script when affine.py is imported. Use methods directly.")

    parser = argparse.ArgumentParser(description='Program to use the Affine Crypto System')

    parser.add_argument("-a", "--alphabet",
                        type=str,
                        default="ABCDEFGHIJKLMNOPQRSTUVWXYZ ",
                        help="The alphabet that is used in the plaintext and encodedtext. Default: \"ABCDEFGHIJKLMNOPQRSTUVWXYZ \" "
                        )
    modeparsers = parser.add_subparsers(title="Mode",
                                        description="Specify a mode for the Affine program. Required",
                                        help='Affine Encode, Decode, or Brute force attack',
                                        dest="mode"
                                        )
    modeparsers.required = True
    # parameters for encoding using Afineaz
    encodeParser = modeparsers.add_parser("encode", aliases=['e'])
    encodeParser.add_argument("key",
                              type=int,
                              nargs=2,
                              help="The key, (a,b), to be used to encode the message. Enter as two integers: a b. ex: 13 25")
    encodeParser.add_argument("plaintext",
                              type=str,
                              help="The plain text message to be encoded"
                              )

    # parameters for decoding using Afine
    decodeParser = modeparsers.add_parser("decode", aliases=['d'])
    decodeParser.add_argument("key",
                              type=int,
                              nargs=2,
                              help="The key, (a,b), to be used to decode the message. Enter as two integers: a b. ex: 13 25"
                              )
    decodeParser.add_argument("encodedtext",
                              type=str,
                              help="The enccoded message to be decoded"
                              )

    # parameters for the bruteforce attack on an encoded string
    bruteforceParser = modeparsers.add_parser("bruteforce", aliases=['b'])
    bruteforceParser.add_argument("encodedtext",
                                  type=str,
                                  help="The enccoded message to be decoded by using an exhaustive brute force attack. You need to know the alphabet used"
                                  )
    args = parser.parse_args()

    return args


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

    inverse = miscTools.modInverse(a, z)
    decoded = ""
    for e in encryptedtext:
        cipherLetterKey = alphabet.find(e)
        d = inverse * (cipherLetterKey - b)
        d = d % z
        decoded += alphabet[d]
    return decoded


def bruteForceCrack(alphabet, encodedString):
    # tries all possible key values
    # prints out the attempted key pair and the corresponding decoded string
    z = len(alphabet)
    for a in range(1, z + 1):  # z+1 because range(a,b) goes from a to b-1
        if(gcdLC.findGCD(a, z) == 1):
            # print(str(a) + " " + str(linearCombination(a, 27)))
            for b in range(1, z + 1):
                d = affineDecode(alphabet, (a, b), encodedString)
                print("%d %d\n%s" % (a, b, d))


args = setArgParse()
print(args)
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.!?,:) "
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ .?!'"


key = (11, 25)  # a,b where b is the length of the alphabet, and a and b must be coprime
# plaintext = "everything is ok"
# encodedString = affineEncode(alphabet, key, plaintext)
# print(encodedString)


# numberEncoding = "15 8 1 17 13 9 17 10 11 1 9 10 22 2 7 17 21 1 24 22 7 12 17 10 1 21 25 24 11 1 2 17 1 17 8 3 22 26 17 3 1 26 19 11 5 1 11 26 22 1 19 8 16 22 21 9 15 11 19 2 7 17 1 23 25 15 7 19 11 19 17 24 1 1 15 1 10 17 24 11 7 17 24 24 1 19 21 15 18 19 8 15 11 19 22 8 1 15 8 3 1 15 1 9 15 11 19 17 8 11 1 9 17 10 11 19 8 15 16 19 11 0 1 1 5 22 26 15 10 3 1 26 1 17 12 17 24"


# bruteForceCrack(alphabet, asLetters)
# message = "I JUST FINISHED MY LAST CRYPTO HW!!"
# message = "I JUST FINISHED MY LAST CRYPTO HW"
message = "RANK TALL BOY MAN THEM OVER POST NOW OFF INTO SHE BED LONG FAT ROOM RECOMMEND EXISTENCE CURIOSITY PERFECTLY FAVOURITE GET EAT SHE WHY DAUGHTERS NOT MAY TOO NAY BUSY LAST SONG MUST SELL AN NEWSPAPER ASSURANCE DISCOURSE YE CERTAINLY SOON GONE GAME AND WHY MANY CALM HAVE DETRACT YET DELIGHT WRITTEN FARTHER HIS GENERAL IF IN SO BRED AT DARE ROSE LOSE GOOD FEEL AND MAKE TWO REAL MISS USE EASY CELEBRATED DELIGHTFUL AN ESPECIALLY INCREASING INSTRUMENT AM INDULGENCE CONTRASTED SUFFICIENT TO UNPLEASANT IN IN INSENSIBLE FAVOURABLE LATTER REMARK HUNTED ENOUGH VULGAR SAY MAN SITTING HEARTED ON IT WITHOUT ME VILLAGE DID REMOVED ENJOYED EXPLAIN NOR HAM SAW CALLING TALKING SECURING AS INFORMED DECLARED OR MARGARET JOY HORRIBLE MOREOVER MAN FEELINGS OWN SHY REQUEST NORLAND NEITHER MISTAKE FOR YET BETWEEN THE FOR MORNING ASSURED COUNTRY BELIEVE ON EVEN FEET TIME HAVE AN NO AT RELATION SO IN CONFINED SMALLEST CHILDREN UNPACKED DELICATE WHY SIR END BELIEVE UNCIVIL RESPECT ALWAYS GET ADIEUS NATURE DAY COURSE FOR COMMON MY LITTLE GARRET REPAIR TO DESIRE HE ESTEEM YET BED ANY FOR TRAVELLING ASSISTANCE INDULGENCE UNPLEASING NOT THOUGHTS ALL EXERCISE BLESSING INDULGENCE WAY EVERYTHING JOY ALTERATION BOISTEROUS THE ATTACHMENT PARTY WE YEARS TO ORDER ALLOW ASKED OF WE SO OPINION FRIENDS ME MESSAGE AS DELIGHT WHOLE FRONT DO OF PLATE HEARD OH OUGHT HIS DEFECTIVE NOR CONVINCED RESIDENCE OWN CONNECTION HAS PUT IMPOSSIBLE OWN APARTMENTS BOISTEROUS AT JOINTURE LADYSHIP AN INSISTED SO HUMANITY HE FRIENDLY BACHELOR ENTRANCE TO ON BY SPORTSMAN DELIGHTED IMPROVING DASHWOODS GAY INSTANTLY HAPPINESS SIX HAM NOW AMOUNTED ABSOLUTE NOT MISTAKEN WAY PLEASANT WHATEVER AT AN THESE STILL NO DRIED FOLLY STOOD THING RAPID IT ON HOURS HILLS IT SEVEN YEARS IF POLITE HE ACTIVE COUNTY IN SPIRIT AN MRS HAM INTENTION PROMOTION ENGROSSED ASSURANCE DEFECTIVE CONFINED SO GRACEFUL BUILDING OPINIONS WHATEVER TRIFLING IN INSISTED OUT DIFFERED HAM MAN ENDEAVOR EXPENSES AT ON HE TOTAL THEIR HE SONGS RELATED COMPACT EFFECTS IS ON SETTLED DO DO IN LAUGHTER SECURING SMALLEST SENSIBLE NO MR HASTENED AS PERHAPS PROCEED IN IN BRANDON OF LIMITED UNKNOWN GREATLY DISTRUSTS FULFILLED HAPPINESS UNWILLING AS EXPLAINED OF DIFFICULT NO LANDLORD OF PECULIAR LADYSHIP ATTENDED IF CONTEMPT ECSTATIC LOUD WISH MADE ON IS AM AS HARD COURT SO AVOID IN PLATE HENCE OF RECEIVED MR BREEDING CONCERNS PECULIAR SECURING LANDLORD SPOT TO MANY IT FOUR BRED SOON WELL TO OR AM PROMOTION IN NO DEPARTURE ABILITIES WHATEVER LANDLORD YOURSELF AT BY PLEASURE OF CHILDREN BE STARTED HIS HEARTED ANY CIVILLY SO ME BY MARIANNE ADMITTED SPEAKING MEN BRED FINE CALL ASK CEASE ONE MILES TRUTH DAY ABOVE SEVEN SUSPICION SPORTSMEN PROVISION SUFFERING MRS SAW ENGROSSED SOMETHING SNUG SOON HE ON PLAN IN BE DINE SOME VIEW FINE ME GONE THIS NAME AN RANK COMPACT GREATER AND DEMANDS MRS THE PARLORS PARK BE FINE EASY AM SIZE AWAY HIM AND FINE BRED KNEW AT OF HARDLY SISTER FAVOUR AS SOCIETY EXPLAIN COUNTRY RAISING WEATHER OF SENTIMENTS NOR EVERYTHING OFF OUT UNCOMMONLY PARTIALITY BED IN UP SO DISCOVERY MY MIDDLETON EAGERNESS DEJECTION EXPLAINED ESTIMATING EXCELLENCE YE CONTRASTED INSENSIBLE AS OH UP UNSATIABLE ADVANTAGES DECISIVELY AS AT INTERESTED PRESENT SUPPOSE IN ESTEEMS IN DEMESNE COLONEL IT TO END HORRIBLE SHE LANDLORD SCREENED STANHILL REPEATED OFFENDED YOU OPINIONS OFF DISSUADE ASK PACKAGES SCREENED SHE ALTERATION EVERYTHING SYMPATHIZE IMPOSSIBLE HIS GET COMPLIMENT COLLECTED FEW EXTREMITY SUFFERING MET HAD SPORTSMAN UP AM INTENTION ON DEPENDENT QUESTIONS OH ELSEWHERE SEPTEMBER NO BETRAYED PLEASURE POSSIBLE JOINTURE WE IN THROWING AND CAN EVENT RAPID ANY SHALL WOMAN GREEN HOPE THEY DEAR WHO ITS BRED SMILING NOTHING AFFIXED HE CARRIED IT CLOTHES CALLING HE NO ITS SOMETHING DISPOSING DEPARTURE SHE FAVOURITE TOLERABLY ENGROSSED TRUTH SHORT FOLLY COURT WHY SHE THEIR BALLS EXCELLENCE PUT UNAFFECTED REASONABLE MRS INTRODUCED CONVICTION SHE NAY PARTICULAR DELIGHTFUL BUT UNPLEASANT FOR UNCOMMONLY WHO"
e = affineEncode(alphabet, (16, len(alphabet)), message)
# print(e)
# d = affineDecode(alphabet, (16, 31), e)
# print(d)
# print(affineDecode(alphabet, (26, 28), "BUVCFIWOUJTZ!H"))
# print(affineDecode(alphabet, (16, 4), "WYVLOOXPPLIYGLKPMXO"))
