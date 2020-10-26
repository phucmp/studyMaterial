"""
Amazon Music Pairs

Amazon Music is working on a new "community radio station" feature which will allow users to iteratively populate
the playlist with their desired songs. Considering this radio station will also have other scheduled shows to be
aired, and to make sure the community soundtrack will not run over other scheduled shows, the user-submitted songs
will be organized in full-minute blocks. Users can choose any songs they want to add to the community list, but
only in pairs of songs with durations that add up to a multiple of 60 seconds (e.g. 60, 120, 180).

As an attempt to insist on the highest standards and avoid this additional burden on users, Amazon will let them
submit any number of songs they want, with any duration, and will handle this 60-second matching internally. Once
the user submits their list, given a list of song durations, calculate the total number of distinct song pairs that
can be chosen by Amazon Music.
"""
from itertools import combinations

def getSongPairCount(songs):
    """Returns the total number of songs pairs that add up to a multiple of 60 seconds. If there are no suitable pairs, return 0"""
    # Brute Force with O(1) space and (nlogn) time complexity
    # count = 0
    # if len(songs) < 2:
    #     return count

    # for i in range(len(songs)-1):
    #     for j in range(i+1, len(songs)):
    #         if (songs[i] + songs[j]) % 60 == 0:
    #             count += 1
    # return count

    #Using O(nlogn) space with O(n) time complexity   
    # count = 0
    # combos = combinations(songs, 2)  #2 represents the number of items in that combination
    # for combo in combos:
    #     if sum(combo) % 60 == 0: 
    #         count += 1
    # return count

    #Simplified code block above
    combos = combinations(songs, 2)
    return len([combo for combo in combos if sum(combo) % 60 == 0])
    


if __name__ == "__main__":
    test_cases = [
        [],
        [1],
        [37,23,60],
        [10,50,90,30],
        [30,20,150,100,40],
        [60,60,60]
    ]
    for case in test_cases:
        print(getSongPairCount(case))