"""
Amazon Fresh is running a promotion in which customers receive prizes for purchasing a secret combination of fruits. The combination will change each day, and the team running the promotion wants to use a code list to make it easy to change the combination. The code list contains groups of fruits. Both the order of the groups within the code list and the order of the fruits within the groups matter. However, between the groups of fruits, any number, and type of fruit is allowable. The term "anything" is used to allow for any type of fruit to appear in that location within the group.
Consider the following secret code list: [[apple, apple], [banana, anything, banana]]
Based on the above secret code list, a customer who made either of the following purchases would win the prize:
orange, apple, apple, banana, orange, banana
apple, apple, orange, orange, banana, apple, banana, banana
Write an algorithm to output 1 if the customer is a winner else output 0.

Input
The input to the function/method consists of two arguments:
codeList, a list of lists of strings representing the order and grouping of specific fruits that must be purchased in order to win the prize for the day.
shoppingCart, a list of strings representing the order in which a customer purchases fruit.
Output
Return an integer 1 if the customer is a winner else return 0.
Note
'anything' in the codeList represents that any fruit can be ordered in place of 'anything' in the group. 'anything' has to be something, it cannot be "nothing."
'anything' must represent one and only one fruit.
If secret code list is empty then it is assumed that the customer is a winner.

Examples:
Input: codeList = [[apple, apple], [banana, anything, banana]] 
shoppingCart = [orange, apple, apple, banana, orange, banana]
Output: 1

Input: codeList = [[apple, apple], [banana, anything, banana]]
shoppingCart = [banana, orange, banana, apple, apple]
Output: 0

Input: codeList = [[apple, apple], [banana, anything, banana]] 
shoppingCart = [apple, banana, apple, banana, orange, banana]
Output: 0

Input: codeList = [[apple, apple], [apple, apple, banana]] 
shoppingCart = [apple, apple, apple, banana]
Output: 0
"""

def isWinner(codelist, shoppingCart):
    if not codelist:
        return 1
    if not shoppingCart:
        return 0

    group_index = 0
    code_index = 0
    for item in shoppingCart:
        code_item = codelist[group_index][code_index]
        if item == code_item or code_item == "anything":
            if code_index == len(codelist[group_index]) - 1:
                if group_index == len(codelist)-1:
                    return 1
                else:
                    group_index += 1
                    code_index = 0
            else:
                code_index += 1
        else:
            code_index = 0
    return 0


if __name__ == "__main__":

    test_cases = [
        ([["apple", "apple"], ["banana", "anything", "banana"]], ["orange", "apple", "apple", "banana", "orange", "banana"]),
        ([["apple", "apple"], ["banana", "anything", "banana"]], ["banana", "orange", "banana","orange", "apple", "apple"]),
        ([["apple", "apple"], ["banana", "anything", "banana"]], ["apple", "banana", "apple", "banana", "orange", "banana"]),
        ([["apple", "apple"], ["apple", "apple", "banana"]],  ["apple", "apple", "apple", "banana"]),
        ([],  ["apple", "apple", "apple", "banana"]),
        ([["apple", "apple"], ["apple", "apple", "banana"]],  []),
        ([], [])
    ]

    for codelist, shoppingCart in test_cases:
        print(isWinner(codelist, shoppingCart))