'''
This Python File is to demonstrate the usage of A* Algorithm in Code. Only for study purposes.
'''

# Step 1: Generate a list of all possible next steps toward goal from current position
# Step 2: Store Children in Priority Queue based on distance of goal with closer one first
# Step 3: Select closest child and pop that open
# Step 4: Repeat Step 1-3 until goal is reached or no more Priority Queue is empty

from Queue import PriorityQueue

tree = {'S': [['A', 1], ['B', 5], ['C',8]],
        'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
        'B': [['S', 5], ['G', 4]],
        'C': [['S', 8], ['G', 5]],
        'D': [['A',3]],
        'E': [['A', 7]]}

heurisitc = {'S': 8,
            'A': 8,
            'B': 4,
            'C': 3,
            'D': 5000,
            'E': 5000,
            'G': 0}

cost = {'S': 0}


def AStarSearch():
    global tree, heurisitc
    q = PriorityQueue()
    
    return
    

if __name__ == "__main__":
    AStarSearch()