from solution import Solution

class InsertionSort(Solution):
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