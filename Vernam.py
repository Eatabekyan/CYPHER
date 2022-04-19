class Vernam :
    Key = ""
    text = ""
    txet = ""
    Alphabeth = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 'I' : 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 'Q' : 16, 'R' : 17, 'S' : 18, 'T' : 19, 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23, 'Y': 24, 'Z' : 25}
    def __init__(self,key):
        self.SetKey(key)
        
        
    def SetKey(self, key):
        self.Key = key
    
    def Encryption(self, text):
        self.text = text
        self.txet = ""
        for i in range(len(text)):
            if text[i]<'A' or text[i]>'Z':
                self.txet += text[i]
            else:
                for j in self.Alphabeth.keys():
                    if self.Alphabeth[j] == (self.Alphabeth[self.Key[i]] + self.Alphabeth[text[i]])%26:
                        self.txet += j
                        break
                

    def Decryption(self, txet):
        self.txet = txet
        self.text = ""
        txt = txet
        for i in range(25):
            v = Vernam(self.Key)
            v.Encryption(txt)
            txt = v.txet
        self.text = txt
            
    

