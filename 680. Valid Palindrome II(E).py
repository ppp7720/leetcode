s = "abcdeedcbaz"



# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         res = []

#         def go(i,j,a):
#             while i < j:
#                 if s[i] == s[j]:
#                     i += 1
#                     j -= 1
#                 elif a == 1:
#                     go(i+1,j,a-1)
#                     go(i,j-1,a-1)
#                     break
#                 else: break
#             res.append(i>=j)

#         go(0,len(s)-1,1)
        
#         return True in res

    # def validPalindrome2(self, s: str) -> bool:
    #     _s = s[::-1]
    #     if _s == s: return True
        
    #     for i in range(len(s)//2):
    #         if s[i] != _s[i]:
    #             a = s[:i]+s[i+1:]
    #             b = _s[:i]+_s[i+1:]
    #             return a == a[::-1] or b == b[::-1]
            
    #     return True    

