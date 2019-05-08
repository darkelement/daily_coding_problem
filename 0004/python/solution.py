#!/bin/python

# The solution must be linear in time, so we cannot sort the array. The solution also has to be
# constant in space, but it's allowed to modify the array. The only possible solution is to iterate
# over the array (constant number of times) and rearrange the items. We should also notice that the
# solution will be smaller or equal to the length of the array.
#
# In this algorithm we reuse the array to mark which elements have bean found. We first iterate over
# elements in arrays and mark the elements (note that case where element is bigger than the current
# iteration index requires special handling). Then in the second iteration we search for the first
# entry that was not marked - its index is the result. For marking we use some not-integer value -
# `None`,
#
# We pass the array twice (three times if we count calculating the size of the array in languages
# that do not store it along the array) so the algorithm is linear in time.

def solve(array):
    length = len(array)
    array.append(0) #1

    i = 0
    while i < length:
        a = array[i]

        if a is None: #2
            i += 1

        elif a < 0: #3
            i += 1

        elif length < a: #4
            i += 1

        elif a <= i: #5
            array[a] = None
            i += 1

        elif i < a: #6
            if array[a] != a:
                array[i] = array[a]
                array[a] = None
            else:
                i += 1

    for i, a in enumerate(array):
        if (i != 0) and (a != None):
            return i
    return length + 1

# 1: Arrays in Python are indexed starting from `0`. We append one element (not marked and not
# positive) to make operations on the indices simpler. If we didn't do that we would have to
# remember to subtract `1` from `i` when comparing with `a`.
#
# 2: The element is already marked. Skip to the next one.
#
# 3: The element is not positive. Skip to the next one.
#
# 4: The element is bigger than the length of the array. There for sure exists smaller element.
# Skip to the next one.
#
# 5: The element is in the fragment of the array we already passed - simply mark it.
#
# 6: The element is in the fragment of the array we yet have to visit - mark it, but immediately
# process the value that was stored there (watch out for the infinite loop!)

