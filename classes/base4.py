class Base4:
    def __init__(self, wordLen):
        self.wordLen = wordLen
        
    def _encodeUtil(self, n):
        res = ""
        while n > 0:
            res = str(n % 4) + res
            n //= 4
            
        padding = self.wordLen - len(res)
        return "0" * padding + res
        
    def _decodeUtil(self, s):
        res = 0
        for char in s:
            res = res * 4 + int(char)
        return res

    def encode(self, nums):
        base4 = ""
        for num in nums:
            base4 += self._encodeUtil(num)
        return base4
        
    def decode(self, b):
        i = 0
        res = []
        while i + self.wordLen <= len(b):
            res.append(self._decodeUtil(b[i: i + 3]))
            i += self.wordLen            
        return res
