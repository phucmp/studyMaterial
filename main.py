from binarySearch import BinarySearch
from bubbleSort import BubbleSort
from insertionSort import InsertionSort

if __name__ == "__main__":
    print("\nMain Starting Entry for Algorithms and Data Structure!\n")

    #Initializing
    binary_search = BinarySearch(4)
    bubble_sort = BubbleSort()
    insertion_sort = InsertionSort()
    algorithms = [ binary_search, bubble_sort, insertion_sort ]

    # Test Cases
    arr = [3,2,8,4,1,6,7]
    # arr = [1,1,1,1,1,1]
    # arr = []
    # arr = [1]
    # arr = [0,0,0,0,0]
    # arr = [1,2,3,4,5]

    # Testing Sorting Algorithms
    for alg in algorithms:
        alg.solve(arr)
        alg.output()