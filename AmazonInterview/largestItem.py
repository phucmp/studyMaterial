"""
In order to improve customer experience, Amazon has developed a system to provide recommendations to the customers regarding the items they can purchase.
Based on historical customer purchase information, an item association can be defined as - if an item A is ordered by a customer, then item B is also likely to be ordered by the same customer
(e.g. Book 1 is frequently ordered with Book 2). All items that are linked together by an item association can be considered to be in the same group. An item without any association can be 
considered to be in the same group. An item without any association to any other item can be considered to be in its own item association group of size 1.

Given a list of item association relationships (i.e. group of items likely to be ordered together). Write an algorithm that outputs the largest item association group. 
If two groups have the same number of items then select the group which contains the item that appears first in lexicographic order. 

INPUT
The input to the function/method consists of an argument - itemAssociation, a list containing pairs of string representing the items that are ordered together.

OUTPUT
Return a list of strings representing the largest item association group, sorted lexicographically.

EXAMPLE
Input
itemAssociation
[[Item1, Item2], [Item3, Item4], [Item4, Item5]]

Output
[Item3. Item4. Item5]

EXPLANATION
There are two item association groups:
group1: [Item1, Item2]
group2: [Item3, Item4, Item5]
In the available item associations, group2 has the largest association
So, the output is [Item3, Item4, Item5]
"""

class Solution:
    def largestItemAssociation(self, itemAssociation):
        if len(itemAssociation) < 2:
            return itemAssociation
            
        all_sets = set()
        max_count = 0
        for i in range(len(itemAssociation)):
            for j in range(i+1, len(itemAssociation)):
                first_set = frozenset(itemAssociation[i])
                second_set = frozenset(itemAssociation[j])
                if first_set & second_set == frozenset():
                    all_sets.add(first_set)
                    all_sets.add(second_set)
                else:
                    all_sets.add(first_set.union(second_set))
        
        largest = []
        associations = sorted([sorted(list(s)) for s in all_sets])
        for assoc in associations:
            if len(assoc) > len(largest):
                largest = assoc
        return largest

if __name__ == "__main__":
    arr = [["Item3", "Item4"]]
    solution = Solution()
    print(solution.largestItemAssociation(arr))