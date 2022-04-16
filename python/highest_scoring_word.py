# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

import functools

def word_score(word):
    return sum(list(map(lambda x: ord(x)-96, list(word.lower()))))

def high(input_line):
    parts = input_line.split(" ")

    result = None

    for p in parts:
        word_value = word_score(p)

        if not result or word_value > word_score(result):
            result = p

    return result

print(word_score("a"))
assert high('what time are we climbing up the volcano') == "volcano"