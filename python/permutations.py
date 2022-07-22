from itertools import permutations as perm


def permutations(in_str):
    all_permutations =  list(perm([x for x in in_str]))
    result = []
    history_added = {}

    for x in all_permutations:
        cur_str = "".join(x)

        if cur_str not in history_added:
            result.append(cur_str)
            history_added[cur_str] = True

    return result



#assert sorted(permutations("a")) == ["a"]
#assert sorted(permutations('ab')) == ['ab', 'ba']
assert sorted(permutations("aabb")) == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

