class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0, 0 swap with 0, 3, then 0, 0 swap with 3,3, then 0, 0 swap with 3, 0
        # 0,1 swap with 1, 3 - 0
        # 1, 1 swap with 1, 2; 1, 1 -> 2,2; 1,1 -> 2,1

        # i, j
        # i, j -> j, (row - i) ; i, j -> (row - i), (col - j); i, j -> col - j, i
        # iterate through first quadrant

        d = len(matrix) - 1
        # 3 -> d = 2; (d + 1)//2 = 1
        # 4 -> d = 3; (d + 1)//2 = 2
        # 5 -> d = 4; (d + 1)//2 = 2
        for i in range((d + 1) // 2): 
            for j in range(d // 2 + 1):
                print(i, j)
                #i, j -> j, (row - i)
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][d - i]
                matrix[j][d - i] = tmp
                #i, j -> (row - i), (col - j)
                tmp = matrix[i][j]
                matrix[i][j] = matrix[d - i][d - j]
                matrix[d - i][d - j] = tmp
                #i, j -> col - j, i
                tmp = matrix[i][j]
                matrix[i][j] = matrix[d - j][i]
                matrix[d - j][i] = tmp
        


