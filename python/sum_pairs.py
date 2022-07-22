
# Given a list of integers and a single sum value, return the first two values (parse from 
# the left please) in order of appearance that add up to form the sum.

def sum_pairs(ints, s):
    #print(f"ints {ints}, s={s}")
    result = None
    iterated = []
    history = {}

    for index, first_item in enumerate(ints):
        if first_item not in history:
            history[first_item] = [index]
        else:
            history[first_item].append(first_item)

        required_value = s - first_item
        #print(f"cur item {first_item}, required value {required_value}")

        if required_value in history:
            indexes_diff = [x for x in history[required_value] if x != index]
            #print(f"indexes_diff {indexes_diff}")

            if indexes_diff:
                #print(f"required value in history")
                #print(history[required_value])

                if indexes_diff[0] < index:
                    return [required_value, first_item]
                else:
                    return [first_item, required_value]


        #for second_index, second_item in enumerate(iterated):
        #    if first_item + second_item == s and index != second_index:
        #        if index < second_index:
        #            result = [first_item, second_item]
        #        else:
        #            result = [second_item, first_item]

        #        return result

l1= [1, 4, 8, 7, 3, 15]
l2= [1, -2, 3, 0, -6, 1]
l3= [20, -13, 40]
l4= [1, 2, 3, 4, 1, 0]
l5= [10, 5, 2, 3, 7, 5]
l6= [4, -2, 3, 3, 4]
l7= [0, 2, 0]
l8= [5, 9, 13, -3]

l9 = [13, 3] + [1]*10000000

assert sum_pairs(l1, 8) == [1, 7]
assert sum_pairs(l2, -6) == [0, -6]
assert sum_pairs(l3, -7) == None
assert sum_pairs(l4, 2) == [1, 1]
assert sum_pairs(l5, 10) == [3, 7]
assert sum_pairs(l6, 8) == [4, 4]
assert sum_pairs(l7, 0) == [0, 0]
assert sum_pairs(l8, 10) == [13, -3]
assert sum_pairs(l9, 0) == None
