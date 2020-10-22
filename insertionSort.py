class Solution:
    def __init__(self):
        self.sortedArr = []

    def solve(self, arr):
        for i in range(1,len(arr)):
            while (i != 0 and arr[i] < arr[i-1]):
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                i -= 1
        self.sortedArr = arr

    
    def output(self):
        print(self.sortedArr)

if __name__ == "__main__":
    # Test Cases
    arr = [3,2,8,4,1,6,7]
    # arr = [1,1,1,1,1,1]
    # arr = []
    # arr = [1]
    # arr = [0,0,0,0,0]
    # arr = [1,2,3,4,5]
    solution = Solution()
    solution.solve(arr)
    solution.output()