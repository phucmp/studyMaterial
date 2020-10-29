from collections import Counter
def findSubstrings(inputString, k):
    i = 0
    output = []
    while i+k-1 < len(inputString):
        substring = inputString[i:i+k]
        counter = Counter(substring)
        if len(counter) == k-1:
            output.append(substring)
        i += 1
    return output

if __name__ == "__main__":
    test_cases = [
        ("", 3),
        ("", 0),
        ("awaglk", 0),
        ("awaglk", 10),
        ("awaglk", 4),
        ("democracy", 5),
        ("wawaglknagagwunagkwkwagl", 4)
    ]

    for inputString, num in test_cases:
        print(findSubstrings(inputString, num))