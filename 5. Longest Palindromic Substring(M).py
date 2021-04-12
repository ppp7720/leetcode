import itertools
s = "plyvmcthyommabcqtmqklpfkopccabybkneifgjdqhexoezlykccgpfidcqizmotounzpslphlpwghbubwthhpivqvwmvuirfhfnkjzpxyccwnuqodbdmsxybztgzvtonheaxcrpukdpgapfczulexugxghuzuvwqvgckpsgjqyzywlxtzmkqmzgavdmchnyaqzidzjfbizxgikjbsmhyikjvgveeifntxpmpgaoqbzwxyfsnexidvxdxxzzzykphrzprlzoyqqlbxbbgmyzplgqnzphbbdxitexvvjzhtpgkfpfazqiqeyczhkkooykaotkqwuuehbgfyznwjqutbltsamcmzyhzrdvvdrzhyzmcmastlbtuqjwnzyfgbheuuwqktoakyookkhzcyeqiqzafpfkgpthzjvvxetixdbbhpznqglpzymgbbxblqqyozlrpzrhpkyzzzxxdxvdixensfyxwzbqoagpmpxtnfieevgvjkiyhmsbjkigxzibfjzdizqaynhcmdvagzmqkmztxlwyzyqjgspkcgvqwvuzuhgxguxeluzcfpagpdkuprcxaehnotvzgtzbyxsmdbdoqunwccyxpzjknfhfriuvmwvqviphhtwbubhgwplhplspznuotomziqcdifpgcckylzeoxehqdjgfienkbybaccpokfplkqmtqcbammoyhtcmvylp"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for j in range(len(s)+1,0,-1):
            for i in range(len(s)-j+1):
                if s[i:i+j] == s[i:i+j][::-1]:
                    return s[i:i+j]

a = Solution()
print(a.longestPalindrome(s))

P     I    N
A   L S  I G
Y A   H R
P     I