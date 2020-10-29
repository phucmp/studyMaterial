class Solution:
    def numIslands(self, grid):
        count = 0
        if not grid:
            return count
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self._dfs(grid, i, j)
                    print(grid)
                    count += 1
        return count

    def _dfs(self, grid, i, j):
        if i<0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "#" # Mark it as visited in place
        self._dfs(grid, i-1, j)
        self._dfs(grid, i+1, j)
        self._dfs(grid, i, j-1)
        self._dfs(grid, i, j+1)

if __name__ == "__main__":
    test_cases = [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ],
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
    ]

    solution = Solution()
    for grid in test_cases:
        print(solution.numIslands(grid))