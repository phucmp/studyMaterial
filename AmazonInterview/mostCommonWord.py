from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph, banned):
        re_paragraph = re.sub("[^A-Za-z ]", "", paragraph)  #Remove punctionations
        counter = Counter([word for word in re_paragraph.lower().split(" ") if word not in banned])  #Create Counter 
        return [word for word, value in counter.items() if value >= max(counter.values())]

if __name__ == "__main__":
    test_cases = [
        ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]),
        ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit", "ball"]),
        ("", ["hit"]),
        ("", ["hit", "hi"]),
        ("", [])
    ]
    solution = Solution()
    for paragraph, banned in test_cases:
        print(solution.mostCommonWord(paragraph, banned))