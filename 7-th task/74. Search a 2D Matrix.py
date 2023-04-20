https://leetcode.com/problems/search-a-2d-matrix/submissions/937123256/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search_line(matrix, target, left, right):
            if left > right:
                return False
            
            mid = left + (right - left) // 2

            if matrix[mid] == target:
                return True
            
            if matrix[mid] > target:
                return search_line(matrix, target, left, mid - 1)
            else:
                return search_line(matrix, target, mid + 1, right)
        
        def search_matrix(matrix, target, line):
            if target <= matrix[line][-1]:
                return matrix[line]
            elif line + 1 < len(matrix):
                return search_matrix(matrix, target, line + 1)
    
        matrix_line = search_matrix(matrix, target, 0)

        if not matrix_line:
            return False
        
        return search_line(matrix_line, target, 0, len(matrix_line) - 1)