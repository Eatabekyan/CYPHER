from Cezar import Cezar


class Vigenere:
    AUP = 'A'
    ZUP = 'Z'
    C = 26
    TxtList = []
    KeyList = []
    TxetList = []
    TxetList_ = []
    Key = ""
    Text = ""
    Txet = ""

    def __init__(self, Key):
        self.Key = Key

    def SetKey(self, Key):
        self.Key = Key

    def SetLists(self, Text):
        self.TxtList = []
        self.KeyList = []
        self.TxetList = []
        self.TxetList_ = []
        for i in range(len(Text)):
            if Text[i] >= self.AUP and Text[i] <= self.ZUP:
                self.TxtList.append(Cezar(0).Alphabeth.index(Text[i]))
                self.KeyList.append(Cezar(0).Alphabeth.index(self.Key[i]))
                self.TxetList.append((self.TxtList[i] + self.KeyList[i]) % self.C)
                self.TxetList_.append((self.TxtList[i] - self.KeyList[i]) % self.C)

    '''def Encryption(self, text):
        self.Text = text
        txet =""
        for k in range(len(self.Key)):
            for i in range(len(Cezar(0).Alphabeth)):
                if self.Key[k] == self.AlphMassive[i][0]:
                    for j in range(len(Cezar(0).Alphabeth)):
                        if self.AlphMassive[0][j] == text[k]:
                            txet += self.AlphMassive[i][j]
                            break
                    break
                if self.Key[k] == self.alphMassive[i][0]:
                    for j in range(len(Cezar(0).alphabeth)):
                        if self.alphMassive[0][j] == text[k]:
                            txet += self.alphMassive[i][j]
                            break
                    break
            if not((text[k]>='a' and text[k]<='z') or (text[k]>='A' and text[k]<='Z')):
	            txet += text[k]
        self.Txet = txet'''

    def Encryption(self, text):
        self.Text = text
        self.Txet = ""
        self.SetLists(text)
        for i in self.TxetList:
            self.Txet += Cezar(0).Alphabeth[i]

    def Decryption(self, text):
        self.Text = ""
        self.Txet = text
        self.SetLists(text)
        for i in self.TxetList_:
            self.Text += Cezar(0).Alphabeth[i]

