from solution import Solution

class BinarySearch(Solution):
    def __init__(self, num):
        self.exist = False
        self.error = False
        self.num = num

    def _isSorted(self, arr):
        return sorted(arr) == arr

    def solve(self, arr):
        if self._isSorted(arr) == True:
            start_index = 0
            end_index = len(arr)-1
            
            while start_index <= end_index:
                mid_index = (start_index + end_index) // 2
                if arr[mid_index] == self.num:
                    self.exist = True
                    return
                elif arr[mid_index] < self.num:
                    start_index = mid_index + 1
                else:
                    end_index = mid_index -1
        else:
            self.error = True

    def output(self):
        if self.error == True:
            print("List is not sorted.")   
        else:
            print(self.exist)