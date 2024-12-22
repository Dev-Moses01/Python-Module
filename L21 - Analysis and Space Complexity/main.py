# import math
# print(math.log(10,2))
#O(log n) = logarithm time complexity
#recursive function = a func that calls itself inside the function

import time

def recursive_test(n):
    if (n <= 1):
        return
    print("Moses rules!!")
    recursive_test(n/2)

recursive_test(60)

#space complexity = space/memory required to complete an algorithm
#auxiliary space = extra space required by an algorithm(variables), excluding input

#O(1)
def sum(n):
    return n * (n+1)/2
# space complexity O(1), auxiliary space also O(1)

#O(n)
def array_sum(a):
    sum = 0
    for i in a:
        sum += i
    return sum
# space complexity O(n), auxiliary space also O(1)

#example a = [1,2,3,4,5] = O(5)space = O(n), auxiliary space = sum and i require a fixed O(1)