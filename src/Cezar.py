class Cezar:
    text = ""
    txet = ""
    Alphabeth = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Alphabeth_X = []
    alphabeth_x = []
    X = 0
    AUP = 'A'
    ZUP = 'Z'
    ALOW = 'a'
    ZLOW = 'z'
   
    def __init__(self, X):
	    self.SetAlphX(X)

    def SetAlphX(self, X):
        self.X = X
        Alphabeth = self.Alphabeth
        Alphabeth_X = []
        alphabeth_x = list()
        for i in range(len(self.Alphabeth)):
            Alphabeth_X.append(Alphabeth[(i + X) % (len(self.Alphabeth))])
            alphabeth_x.append(self.alphabeth[(i + X) % len(self.alphabeth)])
        self.Alphabeth_X = Alphabeth_X
        self.alphabeth_x = alphabeth_x

    def Encryption(self, text):
        self.text = text
        self.txet = ""
        for i in range(len(text)):
            for j in range(len(self.Alphabeth)):
                if text[i] == self.Alphabeth[j]:
                    self.txet += self.Alphabeth_X[j]
                    break
                if text[i] == self.alphabeth[j]:
                    self.txet += self.alphabeth_x[j]
                    break
            if (text[i] < self.ALOW or text[i] > self.ZLOW) and (text[i] < self.AUP or text[i] > self.ZUP):
                self.txet += text[i]

    def Decryption(self, txet):
        self.txet = txet
        self.text = ""
        for i in range(len(txet)):
            for j in range(len(self.Alphabeth)):
                if txet[i] == self.Alphabeth_X[j]:
                    self.text += self.Alphabeth[j]
                    break
                if txet[i] == self.alphabeth_x[j]:
                    self.text += self.alphabeth[j]
                    break
        if (txet[i] < self.ALOW or txet[i] > self.ZLOW) and (txet[i] < self.AUP or txet[i] > self.ZUP):
            self.text += txet[i]

