class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def bst(self, nums):
        pass

    def nodeDistance(self, nums, node1, node2):
        dist = -1
        if node1 not in nums or node2 not in nums or len(nums) < 2:
            return dist

        
        return dist

if __name__ == "__main__":
    test_cases = [
        [[2,1,3], 1, 3]        
    ]
    solution = Solution()
    for nums, node1, node2 in test_cases:
        print(solution.nodeDistance(nums, node1, node2))