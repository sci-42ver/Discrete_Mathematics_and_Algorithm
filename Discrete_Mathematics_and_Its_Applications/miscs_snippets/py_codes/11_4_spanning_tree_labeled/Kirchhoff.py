# https://www.geeksforgeeks.org/problems/total-number-of-spanning-trees-in-a-graph/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab

from typing import List

class Solution:
    def countSpanningTrees(self, graph: List[List[int]], n: int, Use_adj:bool,m: int=0) -> int:
        # Create the adjacency matrix
        adj_matrix = [[0] * n for _ in range(n)]
        if Use_adj:
          adj_matrix=graph
        else:
          for edge in graph:
              u, v = edge
              adj_matrix[u][v] = 1
              adj_matrix[v][u] = 1

        # Calculate the Laplacian matrix
        laplacian_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    laplacian_matrix[i][j] = sum(adj_matrix[i])
                else:
                    laplacian_matrix[i][j] = -adj_matrix[i][j]

        # Calculate the determinant of (n-1) x (n-1) submatrix
        determinant = self.calculateDeterminant(laplacian_matrix, n - 1)

        # Return the determinant as the total number of spanning trees
        return int(determinant)

    def calculateDeterminant(self, matrix: List[List[int]], size: int) -> int:
        if size == 1:
            return matrix[0][0]
        
        determinant = 0
        sign = 1

        for i in range(size):
            # Get the (i, 0) element as a pivot
            pivot = matrix[i][0]

            # Exclude the current row and column
            submatrix = [row[1:] for row in (matrix[:i] + matrix[i + 1:])]

            # Update the determinant using recursion
            determinant += sign * pivot * self.calculateDeterminant(submatrix, size - 1)

            # Change the sign for the next iteration
            sign *= -1

        return determinant

# https://stackoverflow.com/a/18248618/21294350
K=lambda n:[[0 if j == i else 1 for j in range(n)] for i in range(n)]
solution=Solution()
n=3
print(solution.countSpanningTrees(K(n),n,True))
n=4
print(solution.countSpanningTrees(K(n),n,True))

K_mn=lambda m,n:[[0 if (i<m and j<m) or (i>=m and j>=m) else 1 for j in range(m+n)] for i in range(m+n)]
m=2
n=2
print(solution.countSpanningTrees(K_mn(m,n),m+n,True))

C_n=lambda n:[[1 if (abs(j-i)==1 or abs(j-i)==n-1) else 0 for j in range(n)] for i in range(n)]
n=5
print(solution.countSpanningTrees(C_n(n),n,True))