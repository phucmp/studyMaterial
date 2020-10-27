"""
Given a list of reviews, a list of keywords and an integer k. Find the most popular k keywords in order of most to least frequently mentioned.

The comparison of strings is case-insensitive.
Multiple occurances of a keyword in a review should be considred as a single mention.
If keywords are mentioned an equal number of times in reviews, sort alphabetically.

Example 1:

Input:
k = 2
keywords = ["anacell", "cetracular", "betacellular"]
reviews = [
  "Anacell provides the best services in the city",
  "betacellular has awesome services",
  "Best services provided by anacell, everyone should use anacell",
]

Output:
["anacell", "betacellular"]

Explanation:
"anacell" is occuring in 2 different reviews and "betacellular" is only occuring in 1 review.
Example 2:

Input:
k = 2
keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
reviews = [
  "I love anacell Best services; Best services provided by anacell",
  "betacellular has great services",
  "deltacellular provides much better services than betacellular",
  "cetracular is worse than anacell",
  "Betacellular is better than deltacellular.",
]

Output:
["betacellular", "anacell"]

Explanation:
"betacellular" is occuring in 3 different reviews. "anacell" and "deltacellular" are occuring in 2 reviews, but "anacell" is lexicographically smaller.
"""
from collections import Counter
class Solution:
    def findTopKeywords(self, reviews, keywords, k):
        counter = Counter()
        counter.update({key: 0 for key in keywords})
        for review in reviews:
            words = review.lower().split(" ")
            common = set(words) & set(keyowrds)
            counter.update(Counter(common))
        return [key for key, value in counter.most_common(k)]
            
                

if __name__ == "__main__":
    test_cases = [
        [["Anacell provides the best services in the city", "betacellular has awesome services", "Best services provided by anacell, everyone should use anacell"], ["anacell", "cetracular", "betacellular"], 2],
        [["I love anacell Best services; Best services provided by anacell", "betacellular has great services", "deltacellular provides much better services than betacellular", "cetracular is worse than anacell", "Betacellular is better than deltacellular."], ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"], 2]
    ]
    solution = Solution()
    for reviews, keyowrds, k in test_cases:
        print(solution.findTopKeywords(reviews, keyowrds, k))