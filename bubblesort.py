class Solution:
    def __init__(self):
        self.sortedArr = []

    def solve(self, arr):
        if len(arr) != 0:        
            isSorted = False
            indexes = len(arr)-1
            while (isSorted != True):
                isSorted = True
                for i in range(indexes):
                    if arr[i] > arr[i+1]:
                        temp = arr[i]
                        arr[i] = arr[i+1]
                        arr[i+1] = temp      
                        # arr[i] = arr[i] ^ arr[i+1] 
                        # arr[i+1] = arr[i] ^ arr[i+1] 
                        # arr[i] = arr[i] ^ arr[i+1]
                        isSorted = False
                indexes -= 1
            self.sortedArr = arr

    def output(self):
        print(self.sortedArr)


if __name__ == "__main__":
    # Test Cases
    arr = [3,8,2,4,1,6,7]
    # arr = [1,1,1,1,1,1]
    # arr = []
    # arr = [1]
    # arr = [0,0,0,0,0]
    # arr = [1,2,3,4,5]
    solution = Solution()
    solution.solve(arr)
    solution.output()
