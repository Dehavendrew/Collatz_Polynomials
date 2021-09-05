import numpy as np

m = 3
n = 2

def generateReport(polyList, colorList):
    with open("equations.html",'w') as ofile:
        ofile.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Collatz Equations</title>\n")
        ofile.write("<script src=\"https://polyfill.io/v3/polyfill.min.js?features=es6\"></script>\n")
        ofile.write("<script type=\"text/javascript\" id=\"MathJax-script\" async src=\"https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js\"></script>\n")
        ofile.write("</head>\n")
        ofile.write("<body style=\"margin: 5px; font-size: 40px;\">\n")


        for poly in polyList:
            eqn = "<p style=\"background-color: {}\">\\(".format(colorList[poly])
            first = True
            for frac in polyList[poly]:
                if(frac[0,0] == -1 and frac[0,1] == -1):
                    continue
                else:
                    if not first:
                        eqn = eqn + " - "
                    first = False

                    if(frac[1,0] != -1 or frac[1,1] != -1):
                        eqn = eqn + "\\frac{"

                    if frac[0,0] == 0:
                        eqn = eqn + "1"
                    elif frac[0,0] > 0:
                        eqn = eqn + str(n) + "^{" + str(int(frac[0,0])) + "}"

                    if frac[0,1] == 0:
                        eqn = eqn + "1"
                    elif frac[0,1] > 0:
                        eqn = eqn + str(m) + "^{" + str(int(frac[0,1])) + "}"

                    if(frac[1,0] != -1 or frac[1,1] != -1):
                        eqn = eqn + "}{"

                    if frac[1,0] == 0:
                        eqn = eqn + "1"
                    elif frac[1,0] > 0:
                        eqn = eqn + str(n) + "^{" + str(int(frac[1,0])) + "}"

                    if frac[1,1] == 0:
                        eqn = eqn + "1"
                    elif frac[1,1] > 0:
                        eqn = eqn + str(m) + "^{" + str(int(frac[1,1])) + "}"

                    if(frac[1,0] != -1 or frac[1,1] != -1):
                        eqn = eqn + "}"

            eqn = eqn + " = {}\\)</p>\n".format(poly)
            ofile.write(eqn)

        ofile.write("\n</body>\n</html>")

def collatzSeq(x):
    seq = ""
    while x != 1:
        if x % 2 == 0:
            x = x // n
            seq = seq + "e"
        else:
            x = m * x + 1
            seq = seq + "o"
    return seq

def computePolynomial(seq, val):

    print(seq)
    poly = []
    frac = np.ones((2,2)) * - 1

    first = True
    leadingE = True
    leading2 = 0
    pow2 = True
    demon = 0

    for step in seq:
        if step == "o":
            pow2 = False
            leadingE = False
            demon = demon + 1

            if not first:
                poly.append(frac)

            for i in range(len(poly)):
                if poly[i][0,1] == -1:
                    poly[i][0,1] = 0
                poly[i][0,1] = poly[i][0,1] + 1

            #if not(frac[0,0] == -1 and frac[0,1] == -1):


            frac = np.ones((2,2)) * - 1
            frac[0,0] = 0

        if step == "e":
            if leadingE:
                leading2 = leading2 + 1
                continue
            if(frac[1,0] == -1):
                frac[1,0] = 0
            frac[1,0] = frac[1,0] + 1
            for i in range(len(poly)):
                poly[i][1,0] = poly[i][1,0] + 1

        first = False

    #if not(frac[0,0] == -1 and frac[0,1] == -1):
    poly.append(frac)
    #print(poly)

    if not pow2:
        for frac in poly:
            frac[0,0] = frac[0,0] + leading2
            frac[1,0] = frac[1,0] + leading2
    else:
        poly = []
        frac = np.ones((2,2)) * -1
        frac[1,0] = leading2
        poly.append(frac)

    max2pow = -1
    max3pow = -1
    for frac in poly:
        if frac[1,0] > max2pow:
            max2pow = frac[1,0]
        if frac[1,1] > max3pow:
            max3pow = frac[1,1]

    #print(max2pow, max3pow)

    for frac in poly:
        if frac[1,0] < max2pow:
            diff = max2pow - frac[1,0]
            frac[0,0] = frac[0,0] + diff
        if frac[1,1] < max3pow:
            diff = max3pow - frac[1,1]
            frac[0,1] = frac[0,1] + diff

        frac[1,0] = -1
        frac[1,1] = -1

    #print(poly)

    frac = np.ones((2,2))
    frac[0,0] = max2pow
    frac[1,0] = -1
    frac[0,1] = max3pow
    frac[1,1] = -1
    poly.append(frac)

    #print(poly)


    # total = 0
    # for i in range(len(poly)):
    #     frac = poly[i]
    #     if i == len(poly) - 1:
    #         if frac[0,0] != -1 and frac[0,1] == -1:
    #             total = total -  2**frac[0,0]
    #         elif frac[0,0] == -1 and frac[0,1] != -1:
    #             total = total -  3**frac[0,1]
    #         elif frac[0,0] != -1 and frac[0,1] != -1:
    #             total = total -  2**frac[0,0] * 3**frac[0,1]
    #     else:
    #         if frac[0,0] != -1 and frac[0,1] == -1:
    #             total = total +  2**frac[0,0]
    #         elif frac[0,0] == -1 and frac[0,1] != -1:
    #             total = total +  3**frac[0,1]
    #         elif frac[0,0] != -1 and frac[0,1] != -1:
    #             total = total +  2**frac[0,0] * 3**frac[0,1]
    #
    # total = (total * -1) / val
    # demon = int(total ** (1/3))

    #print(demon)


    if pow2:
        demon = -1

    for frac in poly:
        if frac[0,1] == -1:
            frac[1,1] = demon
        else:
            frac[1,1] = demon - frac[0,1]
            frac[0,1] = -1

    poly.reverse()

    return(poly)

def checkPoly(polyList):
    colorList = {}
    for poly in polyList:
        total = 0
        first = True
        for frac in polyList[poly]:
            prod = 1
            if frac[0,0] == -1 and frac[0,1] == -1:
                continue
            if frac[0,0] != -1:
                prod = prod * (n ** frac[0,0])
            if frac[0,1] != -1:
                prod = prod * (m ** frac[0,1])
            if frac[1,0] != -1:
                prod = prod / (n ** frac[1,0])
            if frac[1,1] != -1:
                prod = prod / (m ** frac[1,1])

            if first:
                total = prod
            else:
                total = total - prod

            first = False

        if round(total) == int(poly):
            print("correct {}".format(poly))
            colorList[poly] = "#90EE90"
        else:
            print("incorrect {}".format(poly))
            colorList[poly] = "#F08080"

    return colorList

polyList = {}

for i in range(2,101):
    x = collatzSeq(i)
    polyList[str(i)] = computePolynomial(x, i)

correctList = checkPoly(polyList)

generateReport(polyList, correctList)
