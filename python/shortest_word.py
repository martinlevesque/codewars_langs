
import functools

def find_short(s):
    return functools.reduce(lambda a, b: a if len(a) < len(b) else b, s.split(" "))

print(find_short("bitcoin take over the world maybe who knows perhaps"))