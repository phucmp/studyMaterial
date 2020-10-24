from solution import Solution

class BubbleSort(Solution):
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