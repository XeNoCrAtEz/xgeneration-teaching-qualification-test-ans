# This function checks whether the sum of the two
# number in the array match the total. If there are
# none, return false, else true
# e.g
# arr = [1, 2, 3, 4, 5], total = 9
# return true
def valid_sum(arr, total):
    # # simplest and most pythonic way, complexity O(n^2)
    # # arr = set(arr)        # slight optimization by removing duplicate numbers
    # for num in arr:
    #     if total-num in arr:
    #         return True
    # return False

    # optimized using a set, so python only needs to check "seen" numbers
    # worst-case scenario, complexity O(n^2), and space complexity O(n)
    seen = set()
    for num in arr:
        if total-num in seen:
            return True
        seen.add(num)
    return False

import random
print(valid_sum(arr=[random.randint(-5000, 5000) for _ in range(100000)], total=1092.1))