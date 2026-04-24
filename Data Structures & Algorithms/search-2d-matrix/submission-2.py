class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        while i < len(matrix):
            low = matrix[i][0]
            high = matrix[i][len(matrix[i]) - 1]
            if target >= low and target <= high:
                k = 0
                j = len(matrix[i]) - 1
                while k <= j:
                    middle = (k + j) // 2
                    print(matrix[i][middle], k , j)
                    if target > matrix[i][middle]:
                        k = middle + 1
                    elif target < matrix[i][middle]:
                        j = middle - 1
                    else:
                        return True
            i += 1
        return False