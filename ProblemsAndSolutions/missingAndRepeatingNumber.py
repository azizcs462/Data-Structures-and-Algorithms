# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

 

# Example 1:

# Input: grid = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
# Example 2:

# Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
# Output: [9,5]
# Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].



class Solution:
    def findRepeatingAndMissingNumbers(self,nums):
        rows = len(nums)
        columns = len(nums[0])

        sumn = (rows*rows*(rows*rows+1))/2
        squareSum = sumn*(2*rows*rows+1)/3
        

        numsSum = 0
        numsSquareSum = 0

        for i in range(rows):
            for j in range(columns):
                numsSum += nums[i][j]
                numsSquareSum += nums[i][j]**2


        #x-y
        sumdiff = sumn - numsSum

        #x2-y2
        squarediff = squareSum - numsSquareSum

        #x+y 
        missingRepeatingSum =    squarediff/ sumdiff

        missingNumber = (missingRepeatingSum+sumdiff)/2

        repeatingNumber= missingNumber - sumdiff

        return [int(repeatingNumber),int(missingNumber)]








grid = [[9,1,7],[8,9,2],[3,4,6]]        

obj = Solution()
print(obj.findRepeatingAndMissingNumbers(grid))




