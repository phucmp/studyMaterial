def cutOffRank(scores, cutoff):
    pass

if __name__ == "__main__":
    test_cases = [
        ([100,50,50,25], 3),
        ([2,2,3,4,5], 4)
    ]

    for scores, cutoff in test_cases:
        print(cutOffRank(scores, cutoff))