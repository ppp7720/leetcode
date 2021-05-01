words = ["gin", "zen", "gig", "msg"]

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
             'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
             'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
             'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
        
        ans = 0
        new_words = []
        for word in words:
            moss = ''
            for c in word:
                moss += m[c]
            if moss not in new_words:
                new_words.append(moss)
                ans += 1
        return ans