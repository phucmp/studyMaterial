def runningSum(self, nums: List[int]) -> List[int]:
    output = []
    currSum = 0
    for i in range(len(nums)):
        newSum = nums[i] + currSum
        output.append(newSum)
        currSum = newSum
    return output