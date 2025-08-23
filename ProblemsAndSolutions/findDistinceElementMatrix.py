
# Given a N x N matrix M. Write a program to find count of all the distinct elements common to all rows of the matrix. Print count of such elements.


class Solution:
    def distinctElement(self,Matrix):
        result = 0
        numberDict = {}
        rows = len(Matrix)

        for i in range(rows):
            numberSet = set(Matrix[i])

            for num in numberSet:
                if num in numberDict:
                    numberDict[num] = numberDict[num]+1
                else:
                    numberDict[num] = 1

        for item in numberDict:
            if numberDict[item] ==rows:
                result = result+1

        return result        




        return Matrix
    

Matrix = [[2, 1, 4, 3],
     [1, 2, 3, 2],
     [3, 6, 2, 3],
     [5, 2, 5, 3]]
obj = Solution()

print(obj.distinctElement(Matrix))
