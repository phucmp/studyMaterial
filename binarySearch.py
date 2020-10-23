
class Solution:
    def __init__(self):
        self.exist = False
        self.error = False

    def _isSorted(self, arr):
        return sorted(arr) == arr

    def solve(self, arr, num):
        if self._isSorted(arr) == True:
            start_index = 0
            end_index = len(arr)-1
            
            while start_index <= end_index:
                mid_index = (start_index + end_index) // 2
                if arr[mid_index] == num:
                    self.exist = True
                    return
                elif arr[mid_index] < num:
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

if __name__ == "__main__":
    #Test Cases
    arr = [1,2,3,4,5,6,7,8]
    # arr = []
    # arr = [1]
    # arr = [1,2,4,5]
    # arr = [1,1,1,1,1]
    # arr = [1,2,5,4]
    num = 4
    solution = Solution()
    solution.solve(arr, num)
    solution.output()