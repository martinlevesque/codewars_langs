
def hashtag_normalize_word(word):

    if not word:
        return ""

    return word.capitalize()

def generate_hashtag(input_str):
    
    if not input_str:
        return False

    normalized_items = [
        hashtag_normalize_word(x)
        for x in input_str.split(" ")
        if hashtag_normalize_word(x)
    ]

    final_result = f"#{''.join(normalized_items)}"

    if len(final_result) > 140:
        return False

    return final_result

assert generate_hashtag('') == False
assert generate_hashtag('Do We have A Hashtag')[0] == '#'
assert generate_hashtag('Codewars') == '#Codewars'
assert generate_hashtag('Codewars      ') == '#Codewars'
assert generate_hashtag('Codewars Is Nice') == '#CodewarsIsNice'
assert generate_hashtag('codewars is nice') == '#CodewarsIsNice'
assert generate_hashtag('CodeWars is nice') == '#CodewarsIsNice'
assert generate_hashtag('c i n') == '#CIN'
assert generate_hashtag('codewars  is  nice') == '#CodewarsIsNice'
assert generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat') == False