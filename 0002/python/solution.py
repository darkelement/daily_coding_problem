#!/bin/python

def with_division(array):
    """
    This is a simple solution with division.
    """

    # Calculate the product of all numbers.
    product = 1
    for element in array:
        product *= element

    # Create a result array by dividing product of all numbers by element at index `i`.
    # Catch: because of how floating-point number are represented, division may lose some presision,
    # so we should round the results to the closest integer.
    return [round(product / element) for element in array]

def without_division(array):
    """
    This is more complex solution without division.
    """

    # In this solution we first create two arrays:
    # First one containing on `i`th place the product of all numbers to the left from `i`th element
    # of the input array (and 1 in the left-most element).
    product = 1
    left = [1]
    for element in array[:-1:1]:
        product *= element
        left.append(product)

    # The second containing on `i`th place the product of all numbers to the right from `i`th
    # element of the input array (and 1 in the right-most element).
    product = 1
    right = [1]
    for element in array[-1:0:-1]:
        product *= element
        right.append(product)
    right.reverse()

    # Then it's enough multiply `i`th elements of both arrays to obtain the result
    return [i * j for i, j in zip(left, right)]

