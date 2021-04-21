ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        h = dict()
        
        for i in ransomNote: h[i] = h.get(i,0) + 1
        
        for i in h:
            if h[i] > magazine.count(i): return False
        
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        
        magazine = list(magazine)
        
        for i in ransomNote:
        
            if i in magazine: magazine.remove(i)
        
            else: return False        
        
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        h = dict()
        
        for i in magazine: h[i] = h.get(i,0) + 1

        for i in ransomNote:
            if i in h and h[i] > 0: h[i] -= 1
            else: return False
        
        return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        
        h1 = dict()
        
        h2 = dict()
        
        for i in ransomNote: h1[i] = h1.get(i,0) + 1
        
        for i in magazine: h2[i] = h2.get(i,0) + 1
      
        for i in h1:
            if i not in h2 or h1[i] > h2[i]: return False
        
        return True

        