n = 12

class Solution:

    def countPrimes(self, n: int) -> int:
        
        nums = [1,1]+[0]*(n-2)
        
        for i in range(2,int(n**0.5)+1):
            if nums[i] == 0:
                nums[i*i:n:i] = [1] * len(nums[i*i:n:i])
                        
        return nums.count(0)
   
print(Solution().countPrimes(n))