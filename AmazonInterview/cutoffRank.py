from collections import Counter

def cutOffRank(scores, cutoff):
    ranks = []
    rank = 0
    prev = -1
    skip = 1
    for score in sorted(scores, reverse=True):
        if score == prev:
            ranks.append(rank)
            skip += 1
        else:
            rank += skip
            ranks.append(rank)
            skip = 1
        prev = score

    return len([rank for rank in ranks if rank <= cutoff])
        

if __name__ == "__main__":
    test_cases = [
        ([100,50,50,25], 3),
        ([100,50,50,50,25], 3),
        ([100,50,50,25], 5),
        ([100,50,50,25], 1),
        ([100,50,50,25], 0),
        ([], 0),
        ([2,2,3,4,5], 4)
    ]

    for scores, cutoff in test_cases:
        print(cutOffRank(scores, cutoff))