'''
-1,-1  -1,0  -1,1
       0,0   
1,-1    1,0   1,1
'''
# Calculate the sum based on the given indexes
def calculateSum(arr, row, col):
    return arr[row][col] + arr[row-1][col-1] + arr[row-1][col] + arr[row-1][col+1] + arr[row+1][col-1] + arr[row+1][col] + arr[row+1][col+1]

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxSum = float('-inf')
    for row in range(1,5):
        for col in range(1,5):
            currSum = calculateSum(arr, row, col)
            if currSum > maxSum:
                maxSum = currSum
    return maxSum