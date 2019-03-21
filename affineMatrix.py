# Pranav Salunke

import numpy as np
import miscTools


def affineMatrixEncode(alphabet, P, key):
    A = key[0]
    B = key[1]
    z = len(alphabet)
    C = np.matmul(A, P)+B  # apply affine matrix transformation C = A*P+B
    C = C % z
    numstr = matrixToNumString(C)
    s = numStringToText(alphabet, numstr)
    return s


def affineMatrixDecode(alphabet, C, A, B):
    pass


def matrixToNumString(matrix):
    # converts a matrix into a string of space separated numbers
    s = ""
    for a, b in zip(matrix[0], matrix[1]):
        s += " "
        s += str(a)
        s += " "
        s += str(b)
    s = s.strip()
    return s


def numStringToText(alphabet, numstring):
    # converts string of space separated numbers to its letter representation
    s = ""
    numarr = numstring.split()
    for n in numarr:
        s += alphabet[int(n)]
    return s


def textStringToMatrix(alphabet, string):
    # converts a string to its 2xN matrix representation. (N depends on length of string)
    #   Pads with space if needed to have a rectangular matrix
    #   if there is no space, it pads with the last character in the alphabet
    top = []
    bottom = []
    for i in range(len(string)):
        n = alphabet.find(string[i])
        if i % 2 == 0:
            top.append(n)
        else:
            bottom.append(n)

    if len(top) > len(bottom):
        n = alphabet.find(" ")  # bad with space
        if n == -1:
            n = len(alphabet)-1
        bottom.append(n)

    return np.array([top, bottom])


def buildKey(alphabet, a, b, c, d, e, f):
    # A is a 2x2 matrix  [[a, b],
    #                     [c, d]]
    # B is a 2x1 matrix  [[e],
    #                     [f]]
    z = len(alphabet)
    A = np.array([[a, b], [c, d]])
    B = np.array([[e], [f]])

    if int(round(np.linalg.det(A))) == 0:
        # matrix is singular and is not a valid matrix since A needs to be invertable
        raise UserWarning("%s is an invalid matrix for A. Needs to be invertable" % (str(A)))
    # make sure elements of B are  0 < element < z
    # really could be any number, but it is clearer to restrict it
    if (B > 0).sum() != B.size or (B < z).sum() != B.size:
        raise UserWarning("%s is an invalid matrix for B. Make sure all elements are greater than 0 and less than the length of the alphabet (%d)" % (str(B), z))

    return (A, B)


def flippityFlopPart(matrix):
    # expects matrix to be a numpy array

    # the swaping part for finding the inverse of a 2 matrix
    # if A is a 2x2 matrix  [[a, b],
    #                        [c, d]]
    # the inverse is 1/determinant  * flippedA
    # where flippedA is [[d -b]
    #                    [-c a]]
    # this is what this function returns as an numpy array

    # make sure matrix is a numpy array
    if not isinstance(matrix, np.ndarray):
        # put error here
        pass

    # make sure the inputted matrix is 2x2
    dimensions = matrix.shape  # should be (2,2)
    if not dimensions == (2, 2):
        # put error here
        pass

    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    t = a
    a = d
    d = t

    b = -b
    c = -c
    return np.array([[a, b], [c, d]])


def main():
    e1 = 0
    e2 = 0
    e3 = 0
    e4 = 0
    # alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.?"
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

    text = "TOMORROW"
    P = textStringToMatrix(alphabet, text)
    key = buildKey(alphabet, 23, -1, 4, 12, 3, 19)
    C = affineMatrixEncode(alphabet, P, key)
    print(text)
    print(P)
    print(key[0])
    print(key[1])
    print(C)

    # for e1 in range(2):  # test all 16 cases
    #     for e2 in range(2):
    #         for e3 in range(2):
    #             for e4 in range(2):
    #                 # get matrix A for that case
    #                 # for text from hw question 5.2
    #                 # A = np.array([[14 + (15 * e1), 5 + (15 * e2)], [3 + (15 * e3), 11 + (15 * e4)]])
    #                 # from example 5.4
    #                 A = np.array([[9 + (15 * e1), 1 + (15 * e2)], [13 + (15 * e3), 4 + (15 * e4)]])

    #                 # get det A to see if it is invertable in mod 30 (30 is hard coded for now)
    #                 det = int(round(np.linalg.det(A)))
    #                 det = det % 30
    #                 detinv = miscTools.modInverse(det, 30)
    #                 if detinv is not None:
    #                     print("%d %d %d %d" % (e1, e2, e3, e4))
    #                     Achanged = flippityFlopPart(A)
    #                     Ainv = (detinv * Achanged) % 30  # find A^-1
    #                     P = (Ainv.dot(C)) % 30  # get matrix for plain text
    #                     s = matrixToNumString(P)
    #                     print(numStringToText(alphabet, s))  # convert number matrix to string


main()
