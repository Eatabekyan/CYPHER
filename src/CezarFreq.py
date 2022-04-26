from Cezar import Cezar

PER = 100
deff = 0.09


def hack(text):

    standFreck = []
    standFreck.append(['A', 8.89])
    standFreck.append(['B', 1.58])
    standFreck.append(['C', 3.99])
    standFreck.append(['D', 2.77])
    standFreck.append(['E', 11.38])
    standFreck.append(['F', 0.93])
    standFreck.append(['G', 1.21])
    standFreck.append(['H', 0.69])
    standFreck.append(['I', 11.44])
    standFreck.append(['J', 0.15])
    standFreck.append(['K', 0.01])
    standFreck.append(['L', 3.15])
    standFreck.append(['M', 5.38])
    standFreck.append(['N', 6.28])
    standFreck.append(['O', 5.40])
    standFreck.append(['P', 3.03])
    standFreck.append(['Q', 1.51])
    standFreck.append(['R', 6.67])
    standFreck.append(['S', 7.60])
    standFreck.append(['T', 8.00])
    standFreck.append(['U', 8.46])
    standFreck.append(['V', 0.96])
    standFreck.append(['W', 2.36])
    standFreck.append(['X', 0.96])
    standFreck.append(['Y', 0.60])
    standFreck.append(['Z', 0.01])

    CurrFreck = []
    for i in range(len(standFreck)):
        CurrFreck.append([standFreck[i][0], 0.0])

    for i in range(len(text)):
        for j in range(len(CurrFreck)):
            if text[i] == CurrFreck[j][0]:
                CurrFreck[j][1] += 1.0
                break

    for i in range(len(CurrFreck)):
            CurrFreck[i][1] = (CurrFreck[i][1]/len(text))*PER

    slides = []
    for i in range(len(CurrFreck)):
        for j in range(len(standFreck)):
            if (CurrFreck[i][1] >= (standFreck[j][1] - deff)) and (CurrFreck[i][1] <= (standFreck[j][1] + deff)):
                slides.append(Cezar.Alphabeth.index(CurrFreck[i][0]) - Cezar.Alphabeth.index(standFreck[j][0]))

    slides.sort()
    count = 0
    maxCount = count
    slide = 0

    for i in range(1, len(slides)):
        if slides[i] == slides[i-1]:
            count += 1
        else:
            if count > maxCount:
                maxCount = count
                slide = slides[i]
            count = 0

    Cez = Cezar(slide)
    Cez.Decryption(text)
    return Cez.text

