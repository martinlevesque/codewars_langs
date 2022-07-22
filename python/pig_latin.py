# Move the first letter of each word to the end of it, 
# then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

import string

def pig_it(text):

    def format_word(word):

        if word in string.punctuation:
            return word

        return f"{word[1:]}{word[0]}ay"

    return ' '.join([
        format_word(w)
        for w
        in text.split(" ")
    ])

assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'
assert pig_it('This is my string') == 'hisTay siay ymay tringsay'
assert pig_it('Hello world !') == "elloHay orldway !"