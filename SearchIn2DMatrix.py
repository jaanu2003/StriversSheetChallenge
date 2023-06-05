class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        n = len(matrix)
        m = len(matrix[0])
        low  = 0
        high = (n*m) 
        while(low < high):
            mid = (low+(high-1))//2 
            if(matrix[mid//m][mid%m] == target):
                return True
            if(matrix[mid//m][mid % m] < target):
                low = mid + 1
            else:
                high =  mid
        return False
