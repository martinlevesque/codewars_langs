# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
# Examples

# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]


def sort_array(arr):
    positions_even = {}
    result = []

    for index, elem in enumerate(arr):
        if elem % 2 == 0:
            positions_even[index] = elem
        else:
            result.append(elem)

    result.sort()

    for index, elem in positions_even.items():
        result.insert(index, elem)

    return result

assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]