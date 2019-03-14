# Pranav Salunke

import numpy as np
import miscTools


def matrixToNumString(matrix):
    s = ""
    for a, b in zip(matrix[0], matrix[1]):
        s += " "
        s += str(a)
        s += " "
        s += str(b)
    s = s.strip()
    return s


def numStringToText(alphabet, numstring):
    s = ""
    numarr = numstring.split()
    for n in numarr:
        s += alphabet[int(n)]
    return s


def textStringToMatrix(alphabet, string):
    top = []
    bottom = []
    for i in range(len(string)):
        n = alphabet.find(string[i])
        if i % 2 == 0:
            top.append(n)
        else:
            bottom.append(n)

    if len(top) > len(bottom):
        n = alphabet.find(" ")
        bottom.append(n)

    return np.array([top, bottom])


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
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.?"
    # from hw question 5.2
    # text = "U?DIPPWKCKIKFBWZERRXTV AXN,FG.SAYCHYVTMIMBG.LHTV KCPEAF?.FSGGZ.YOQMZQL.DWKLHYCHIVT,REEKQMJSLEAFXWWVFMKQQUQEWOQHI .BOG.UN.JGNIZQYESRMOQGNWMTVZHF,OKQYZQBLVNQ.MJSLMKQQUQRXKMJEG.ZH WRM.HYNDV,REE,RGBJR.F?NFHMHGHSFMKTZPDKA?EVJEM W?T MDOYU.FSFYCKWSHKNGEG.LH?NFHMHGHSFOQCCESRM?N,RZBE,.HZZQLIHWWCZ.KHIIJOWIHW..HQQUQUNRMJR.F?TWANUEGSEGTSHFXWZGHDOOQGNVFMKWE,MBFE,.H,XOQWKZBOTRZON.ECJQLWZFXWZQQUQ.GMZCIG.VZKWV.Q.NXVTG.QQUQ.USFMKBOBFEM WYCHIVTJR.FJLVZGNMJSL?Z QIOWCESRMSFSWSEYRWK"
    # from example 5.4
    text = "CU.TG CGNFCG.?BK"
    C = textStringToMatrix(alphabet, text)

    for e1 in range(2):  # test all 16 cases
        for e2 in range(2):
            for e3 in range(2):
                for e4 in range(2):
                    # get matrix A for that case
                    # for text from hw question 5.2
                    # A = np.array([[14 + (15 * e1), 5 + (15 * e2)], [3 + (15 * e3), 11 + (15 * e4)]])
                    # from example 5.4
                    A = np.array([[9 + (15 * e1), 1 + (15 * e2)], [13 + (15 * e3), 4 + (15 * e4)]])

                    # get det A to see if it is invertable in mod 30 (30 is hard coded for now)
                    det = int(round(np.linalg.det(A)))
                    det = det % 30
                    detinv = miscTools.modInverse(det, 30)
                    if detinv is not None:
                        print("%d %d %d %d" % (e1, e2, e3, e4))
                        Achanged = flippityFlopPart(A)
                        Ainv = (detinv * Achanged) % 30  # find A^-1
                        P = (Ainv.dot(C)) % 30  # get matrix for plain text
                        s = matrixToNumString(P)
                        print(numStringToText(alphabet, s))  # convert number matrix to string


# main()
