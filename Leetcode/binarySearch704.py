def search(self, nums: List[int], target: int) -> int:
    startIndex = 0
    endIndex = len(nums)-1
    while startIndex <= endIndex:
        midIndex = (startIndex + endIndex) // 2
        if target == nums[midIndex]:
            return midIndex
        elif target > nums[midIndex]:
            startIndex = midIndex + 1
        else:
            endIndex = midIndex - 1
    return -1