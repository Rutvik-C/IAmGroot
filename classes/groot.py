import random

from classes.base4 import Base4


class Groot:
    def __init__(self, sequence, wordLen):
        self.wordLen = wordLen
        
        self.charToIdx = {sequence[i]: i for i in range(len(sequence))}
        self.idxToChar = {i: sequence[i] for i in range(len(sequence))}
        
        self.base4 = Base4(wordLen)
        self.chars = [
            ["i", "I", "í", "Î"],
            [" "],
            ["a", "A", "á", "Â"],
            ["m", "M", "ḿ", "Ḿ"],
            [" "],
            ["g", "G", "ģ", "Ğ"],
            ["r", "R", "ŕ", "Ř"],
            ["o", "O", "ó", "Ô"],
            ["o", "O", "ó", "Ô"],
            ["t", "T", "ť", "Ť"],
            [" "]
        ]
        self.nChars = len(self.chars)
        
        self.charCategory = [
            "iamgroot",
            "IAMGROOT",
            "íáḿģŕóóť",
            "ÎÂḾĞŘÔÔŤ"
        ] 

    def _stringToIdx(self, s):
        res = []
        for char in s:
            res.append(self.charToIdx[char])
        return res
        
    def _idxToString(self, indexes):
        res = ""
        for idx in indexes:
            res += self.idxToChar[idx]
        return res
    
    def _getRandomSequence(self, seqLen, src, subSeed):
        seed = int(hash(src)) + subSeed
        random.seed(seed)
        
        # TODO: Mathematically decide value for randint(a, b). Here 2 and 5 hardcoded 
        randomSequence = [random.randint(3, 6) for i in range(seqLen)]
        return randomSequence 
    
    def _iAmGrootEncode(self, src, base4Encoded):
        grootStr = []
        randomSubSeed = 0
        randomSequence = self._getRandomSequence(self.nChars, src, randomSubSeed)
        i = 0
        charIdx = 0
        
        while i < len(base4Encoded):
            if len(self.chars[charIdx]) == 1:  # Special seperators
                grootStr.append(self.chars[charIdx][0])
                
            else:
                j = 0
                while i < len(base4Encoded) and j < randomSequence[charIdx]:
                    char = self.chars[charIdx][int(base4Encoded[i])]
                    grootStr.append(char)
                    
                    i += 1
                    j += 1
                
            charIdx = charIdx + 1
            if charIdx >= self.nChars:
                charIdx = 0
                randomSubSeed += 1
                randomSequence = self._getRandomSequence(self.nChars, src, randomSubSeed)
            
        while charIdx < self.nChars - 1:  # Sentence completion
            char = self.chars[charIdx][0]
            grootStr.append(char)
            charIdx += 1
            
        return "".join(grootStr)
    
    def _iAmGrootDecode(self, grootStr):
        base4Encoded = []
        
        for char in grootStr:
            if char in [" ", "\n"]:
                continue
            
            for i, s in enumerate(self.charCategory):
                if char in s:
                    base4Encoded.append(str(i))
                    break
        
        return "".join(base4Encoded)
        
    def encode(self, s):
        if s == "":
            return ""
        
        indexes = self._stringToIdx(s)
        base4Encoded = self.base4.encode(indexes)
        grootStr = self._iAmGrootEncode(s, base4Encoded)
        
        return grootStr.strip()

    def decode(self, grootStr):
        base4Encoded = self._iAmGrootDecode(grootStr)
        indexes = self.base4.decode(base4Encoded)
        s = self._idxToString(indexes)
        
        return s.strip()
