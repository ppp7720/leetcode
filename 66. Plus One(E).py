digits = [9,9,9]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        digits.reverse()
        for i in range(len(digits)):
            if digits[i] == 10:
                try:
                    digits[i+1] += 1
                except:
                    digits.append(1)
                digits[i] = 0
        digits.reverse()
        return digits