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
                              help="The encoded message to be decoded"
                              )

    # parameters for the bruteforce attack on an encoded string
    bruteforceParser = modeparsers.add_parser("bruteforce", aliases=['b'])
    bruteforceParser.add_argument("encodedtext",
                                  type=str,
                                  help="The encoded message to be decoded by using an exhaustive brute force attack. You need to know the alphabet used"
                                  )
    args = parser.parse_args()

    return args


def affineEncode(alphabet, key, plaintext):
    alphalength = len(alphabet)

    encryptedtext = ""

    for c in plaintext:
        letterKey = alphabet.find(c)
        if letterKey < 0:
            raise UserWarning("Letter %s does not exist in the alphabet \"%s\"" % (c, alphabet))
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
        if cipherLetterKey < 0:
            raise UserWarning("Letter %s does not exist in the alphabet \"%s\"" % (e, alphabet))
        d = inverse * (cipherLetterKey - b)
        d = d % z
        decoded += alphabet[d]
    return decoded


def bruteForceCrack(alphabet, encodedString):
    # tries all possible key values
    # prints out the attempted key pair and the corresponding decoded string
    z = len(alphabet)
    s = ""
    for a in range(1, z + 1):  # z+1 because range(a,b) goes from a to b-1
        if(gcdLC.findGCD(a, z) == 1):
            # print(str(a) + " " + str(linearCombination(a, 27)))
            for b in range(1, z + 1):
                d = affineDecode(alphabet, (a, b), encodedString)
                # print("%d %d\n%s" % (a, b, d))
                s += "key: (%d,%d)\n%s" % (a, b, d)
                s += "\n"

    return s


def main():
    args = setArgParse()
    mode = args.mode
    alph = args.alphabet

    def validateKey(key, n):
        a = key[0]
        b = key[1]
        if gcdLC.findGCD(a, n) != 1:
            raise UserWarning(
                "%d is an invalid value for 'a' in the key (a,b). Make sure it is invertable in 'n' where 'n' is the number of characters in your alphabet (%d). That is, gcd(a,n)=1" % (a, len(alph)))
        if b < 0 or b >= n:
            raise UserWarning(
                "%d is an invalided value for 'b' in the key (a,b). Make sure b is in the inclusive range [0-%d] (one less than the number of characters in your alphabet)" % (b, n-1))
        # this check is not actually needed as b can be any integer since it will be modded by n anyway. so n and 0 are the same as far as the math is concerned.
        #   But it makes more sense to keep it restricted between 0 and n-1

    if mode == "encode" or mode == "e":
        key = args.key
        validateKey(key, len(alph))
        text = args.plaintext
        encoded = affineEncode(alph, key, text)

        print("Encoding the string: \"%s\"" % (text))
        print("The encoded string: \"%s\"" % (encoded))
        print("Now you can send this encrypted message to your friend!")
    elif mode == "decode" or mode == "e":
        key = args.key
        validateKey(key, len(alph))
        text = args.encodedtext
        decoded = affineDecode(alph, key, text)
        print("Decoding the string: \"%s\"" % (text))
        print("The decoded string: \"%s\"" % (decoded))
        print("You can now read the secret message!")
    elif mode == "bruteforce" or mode == "b":
        text = args.encodedtext
        s = bruteForceCrack(alph, text)
        print("Attempting to crack the code (this could take a while)...")
        print(s)
        print("Hopefully, the code was cracked! Which one of these is readable?")


if __name__ == "__main__":  # true if run directly via the command line
    main()
