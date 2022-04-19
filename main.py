import sys

from Cezar import Cezar
from Vigenere import Vigenere
from Vernam import Vernam
from CezarFreq import*

print("your file is :",sys.argv[1])
filepath = sys.argv[1]
i = 1
print("If you want to encrypt enter".upper(), 1)
print("If you want to decrypt enter".upper(), 2)
print("If you want to hack Ceasar enter".upper(), 3)
print("WARNING: Ceasar Hacker ONLY Works For Texts With More Than 2300 Characters")
x = int(input()) 
if x == 1:
    print("For Ceasar Cypher Enter 1")
    print("For Vernam Cypher Enter 2")
    print("For Vigenere Cypher Enter 3")
    y = int(input())
    if y == 1:
        print("Enter Ceasar Key(NUMBER)")
        CNUM = int(input())
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                Cez = Cezar(CNUM)
                Cez.Encryption(line)
                print(Cez.txet)
                line = fp.readline()
    elif y == 2:
        print("Enter Vernam Key")
        VNUM = str(input())
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                Ver = Vernam(VNUM)
                Ver.Encryption(line)
                print(Ver.txet)
                line = fp.readline()
    elif y == 3:
        print("Enter Vigenere Key")
        VNUM = str(input())
        with open(filepath) as fp:
            line = fp.readline()
            Vig = Vigenere(VNUM)
            while line:
                Vig.Encryption(line)
                print(Vig.Txet)
                line = fp.readline()
    else:
        print("DEFAULT (Ceasar Cypher):")
        print("Enter Ceasar Key(NUMBER)")
        CNUM = int(input())
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                Cez = Cezar(CNUM)
                Cez.Encryption(line)
                print(Cez.txet)
                line = fp.readline()
elif x == 2:
    print("For Ceasar Cypher Enter 1")
    print("For Vernam Cypher Enter 2")
    print("For Vigenere Cypher Enter 3")
    y = int(input())
    if y == 1:
        print("Enter Ceasar Key(NUMBER)")
        CNUM = int(input())
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                Cez = Cezar(CNUM)
                Cez.Decryption(line)
                print(Cez.text)
                line = fp.readline()
    elif y == 2:
        print("Enter Vernam Key")
        VNUM = str(input())
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                Ver = Vernam(VNUM)
                Ver.Decryption(line)
                print(Ver.text)
                line = fp.readline()
    elif y == 3:
        print("Enter Vigenere Key")
        VNUM = str(input())
        with open(filepath) as fp:
            line = fp.readline()
            Vig = Vigenere(VNUM)
            while line:
                Vig.Decryption(line)
                print(Vig.Text)
                line = fp.readline()
    else :
        print("DEFAULT (Ceasar Cypher):")
        print("Enter Ceasar Key(NUMBER)")
        CNUM = str(input())
        with open(filepath) as fp:
            line = fp.readline()
            while line:
                Cez = Cezar(CNUM)
                Cez.Decryption(line)
                print(Cez.text)
                line = fp.readline()
elif x == 3:
    Line =""
    with open(filepath) as fp:
            line = fp.readline()
            while line:
                Line += line
                line = fp.readline()
    print(hack(Line))

else:
    Line =""
    with open(filepath) as fp:
            line = fp.readline()
            while line:
                Line += line
                line = fp.readline()
    print(hack(Line))





